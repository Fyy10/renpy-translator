import argparse
import os
import re
from pathlib import Path

from openai import OpenAI

# ========================
# Configuration
# ========================
LLM_BASE_URL = 'https://api.deepseek.com'  # Replace with your API base url
LLM_API_KEY = os.environ['LLM_API_KEY']
MAX_RETRIES = 3
TIMEOUT = 120  # seconds

# LLM client
client = OpenAI(api_key=LLM_API_KEY, base_url=LLM_BASE_URL, max_retries=MAX_RETRIES, timeout=TIMEOUT)


# ========================
# Core Functions
# ========================
def extract_translatable_blocks(content):
    """
    Splits .rpy content into translatable blocks (dialogue + metadata).
    Returns list of dicts with keys: 'text', 'line_number', 'tags'.
    """
    blocks = []
    lines = content.split('\n')

    for i, line in enumerate(lines):
        # Match dialogue lines (e.g., `e "Hello{w=0.5}, world!"`)
        match = re.match(r'^(\s*[a-zA-Z0-9_]*\s*)"(.*)"\s*', line)
        if not match:
            continue

        speaker = match.group(1).strip()
        # do not translate what 'old' says, it is a keyword
        if speaker == 'old':
            continue
        text = match.group(2)
        tags = re.findall(r'\{.*?\}|\[.*?\]', text)
        # s "What is a visual novel?" nointeract
        stmt_args = re.findall(r'^\s*[a-zA-Z0-9_]*\s*"(?:\\.|[^"\\])*"\s*(\S+(?:\s+\S+)*)', line)

        blocks.append(
            {
                'original': line,
                'speaker': speaker,
                'text': text,
                'tags': tags,
                'stmt_args': stmt_args,
                'line_number': i + 1,
            }
        )

    return blocks


def generate_llm_prompt(blocks, target_lang):
    """
    Formats blocks into an LLM prompt with strict instructions.
    """
    examples = '''
Example Input:  e "Hello{w=0.5}, world!{fast}"
Example Output: e "你好{w=0.5}, 世界!{fast}"

Example Input: "Score: %s points"
Example Output: "得分: %s 分"
    '''.strip()

    instructions = f'''
Translate these Ren'Py game dialogues to {target_lang}. Follow these rules:
1. Preserve ALL tags ({{...}}, [...], etc.), speaker labels, and formatting EXACTLY.
2. Keep placeholders like %s unchanged.
3. Never add/remove quotes or line breaks.

{examples}

Now translate these:
    '''.strip()

    text_to_translate = '\n'.join(
        f'{block['speaker']} "{block['text']}"' for block in blocks
    )

    return f'{instructions}\n{text_to_translate}'


def call_llm_api(prompt):
    """
    Calls the LLM API with the constructed prompt.
    Adjust according to your API's requirements.
    """
    try:
        response = client.chat.completions.create(
            model='deepseek-reasoner',
            messages=[
                {'role': 'system', 'content': 'You are a professional game translator.'},
                {'role': 'user', 'content': prompt},
            ],
            temperature=0.3,
            # max_tokens=4000,
            stream=False,
        )

        return response.choices[0].message.content
    except Exception as e:
        print(f'Retrying... Error: {e}')

    raise Exception('LLM API failed after retries')


def validate_translation(original_block, translated_line):
    """
    Checks if tags/speakers are preserved.
    """
    # Check speaker
    orig_speaker = original_block['speaker']
    trans_speaker = (
        re.match(r'^(\s*[a-zA-Z0-9_]*\s*)', translated_line).group(1).strip()
    )
    if orig_speaker != trans_speaker:
        print(f'Speaker mismatch: {orig_speaker} vs {trans_speaker}')
        return False

    # Check tags
    orig_tags = original_block['tags']
    trans_tags = re.findall(r'\{.*?\}|\[.*?\]', translated_line)
    if set(orig_tags) != set(trans_tags):
        print(f'Tag mismatch:\nOriginal: {orig_tags}\nTranslated: {trans_tags}')
        return False

    return True


def process_rpy_file(in_path, out_path, target_lang):
    """
    Main pipeline: Read -> Extract -> Translate -> Validate -> Write.
    """
    print(f'Processing {in_path} -> {out_path} ({target_lang})')

    # Read input file
    with open(in_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract translatable blocks
    blocks = extract_translatable_blocks(content)
    if not blocks:
        print('No translatable dialogue found.')
        return

    # Generate LLM prompt and call API
    prompt = generate_llm_prompt(blocks, target_lang)
    translated_response = call_llm_api(prompt)

    # Parse LLM response
    translated_lines = [
        line.strip()
        for line in translated_response.split('\n')
        if line.strip() and '"' in line
    ]

    # check if all blocks are translated
    if len(blocks) != len(translated_lines):
        print(f'Warning: {len(translated_lines)} lines translated, but there are {len(blocks)} translate blocks.')

    # Reintegrate translations
    output_lines = content.split('\n')
    err_cnt = 0
    for block, translated_line in zip(blocks, translated_lines):
        if not validate_translation(block, translated_line):
            err_cnt += 1
            print(f'Validation failed for block: {block}\nTranslated line: {translated_line}')
        output_lines[block['line_number'] - 1] = '    ' + ' '.join([translated_line, *block['stmt_args']])
    if err_cnt:
        print(f'{err_cnt} errors encountered.')

    # Write output
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines))

    print(f'Successfully translated {len(blocks)} lines.')


# ========================
# CLI Interface
# ========================
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Automatically translate Ren'Py (.rpy) scripts using an LLM API."
    )
    parser.add_argument('input_folder', help='Path to the input folder that contains the .rpy files to be translated.')
    parser.add_argument('output_folder', help='Path to the output folder for the translated .rpy files.')
    parser.add_argument(
        '--lang', required=True, help='Target language (e.g., "chinese")'
    )
    args = parser.parse_args()

    # Verify paths
    input_path = Path(args.input_folder)
    if not input_path.exists():
        raise FileNotFoundError(f'Input folder not found: {input_path}')

    output_path = Path(args.output_folder)
    output_path.mkdir(parents=True, exist_ok=True)

    for in_file_path in input_path.glob('**/*.rpy'):
        out_file_path = output_path.joinpath(in_file_path.name)

        # run translation
        process_rpy_file(in_file_path, out_file_path, args.lang)
