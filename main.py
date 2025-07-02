import re
import argparse
from pathlib import Path
import requests  # For API calls (replace with your LLM's SDK if needed)

# ========================
# Configuration
# ========================
LLM_API_ENDPOINT = (
    "https://your-llm-api-endpoint/v1/completions"  # Replace with your API
)
LLM_API_KEY = "your-api-key"  # Replace with your key
MAX_RETRIES = 3
TIMEOUT = 30  # seconds


# ========================
# Core Functions
# ========================
def extract_translatable_blocks(content):
    """
    Splits .rpy content into translatable blocks (dialogue + metadata).
    Returns list of dicts with keys: 'text', 'line_number', 'tags'.
    """
    blocks = []
    lines = content.split("\n")

    for i, line in enumerate(lines):
        # Match dialogue lines (e.g., `e "Hello{w=0.5}, world!"`)
        match = re.match(r'^(\s*[a-zA-Z0-9_]*\s*)"(.*)"\s*$', line)
        if not match:
            continue

        speaker = match.group(1).strip()
        text = match.group(2)
        tags = re.findall(r"\{.*?\}", text)

        blocks.append(
            {
                "original": line,
                "speaker": speaker,
                "text": text,
                "tags": tags,
                "line_number": i + 1,
            }
        )

    return blocks


def generate_llm_prompt(blocks, target_lang):
    """
    Formats blocks into an LLM prompt with strict instructions.
    """
    examples = """
Example Input:  e "Hello{w=0.5}, world!{fast}"
Example Output: e "你好{w=0.5}, 世界!{fast}"

Example Input: "Score: %s points"
Example Output: "得分: %s 分"
    """.strip()

    instructions = f"""
Translate these Ren'Py game dialogues to {target_lang}. Follow these rules:
1. Preserve ALL tags ({{...}}), speaker labels, and formatting EXACTLY.
2. Keep placeholders like %s unchanged.
3. Never add/remove quotes or line breaks.

{examples}

Now translate these:
    """.strip()

    text_to_translate = "\n".join(
        f'{block["speaker"]} "{block["text"]}"' for block in blocks
    )

    return f"{instructions}\n{text_to_translate}"


def call_llm_api(prompt):
    """
    Calls the LLM API with the constructed prompt.
    Adjust according to your API's requirements.
    """
    headers = {
        "Authorization": f"Bearer {LLM_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "your-model-name",  # e.g., "gpt-4"
        "messages": [
            {"role": "system", "content": "You are a professional game translator."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.3,  # Lower for consistency
        "max_tokens": 4000,
    }

    for _ in range(MAX_RETRIES):
        try:
            response = requests.post(
                LLM_API_ENDPOINT, headers=headers, json=payload, timeout=TIMEOUT
            )
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"Retrying... Error: {e}")

    raise Exception("LLM API failed after retries")


def validate_translation(original_block, translated_line):
    """
    Checks if tags/speakers are preserved.
    """
    # Check speaker
    orig_speaker = original_block["speaker"]
    trans_speaker = (
        re.match(r"^(\s*[a-zA-Z0-9_]*\s*)", translated_line).group(1).strip()
    )
    if orig_speaker != trans_speaker:
        raise ValueError(f"Speaker mismatch: {orig_speaker} vs {trans_speaker}")

    # Check tags
    orig_tags = original_block["tags"]
    trans_tags = re.findall(r"\{.*?\}", translated_line)
    if set(orig_tags) != set(trans_tags):
        raise ValueError(
            f"Tag mismatch:\nOriginal: {orig_tags}\nTranslated: {trans_tags}"
        )


def process_rpy_file(input_path, output_path, target_lang):
    """
    Main pipeline: Read -> Extract -> Translate -> Validate -> Write.
    """
    print(f"Processing {input_path} -> {output_path} ({target_lang})")

    # Read input file
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract translatable blocks
    blocks = extract_translatable_blocks(content)
    if not blocks:
        print("No translatable dialogue found.")
        return

    # Generate LLM prompt and call API
    prompt = generate_llm_prompt(blocks, target_lang)
    translated_response = call_llm_api(prompt)

    # Parse LLM response
    translated_lines = [
        line.strip()
        for line in translated_response.split("\n")
        if line.strip() and '"' in line
    ]

    # Reintegrate translations
    output_lines = content.split("\n")
    for block, translated_line in zip(blocks, translated_lines):
        validate_translation(block, translated_line)
        output_lines[block["line_number"] - 1] = translated_line

    # Write output
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))

    print(f"Successfully translated {len(blocks)} lines.")


# ========================
# CLI Interface
# ========================
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Automatically translate Ren'Py (.rpy) files using an LLM API."
    )
    parser.add_argument("input_file", help="Path to the input .rpy file")
    parser.add_argument("output_file", help="Path to the output translated file")
    parser.add_argument(
        "--lang", required=True, help="Target language (e.g., 'chinese')"
    )
    args = parser.parse_args()

    # Verify paths
    input_path = Path(args.input_file)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    output_path = Path(args.output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Run translation
    process_rpy_file(input_path, output_path, args.lang)
