# Renpy Translator

Translate your Renpy game with LLM.

## Usage

Show help message:

```bash
python main.py -h
```

Create a `.env` file with the following content:

```bash
LLM_API_KEY=your-api-key
```

Load API key:

```bash
set -a && source .env && set +a
```

Run translation:

```bash
python main.py ./test_data/ ./test_out/ --lang chinese
```
