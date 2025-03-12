# Libra - Local LLM CLI Interface

A lightweight command-line interface for running LLaMA-based models locally.

## Features
- Local model inference with no external API dependencies
- Efficient memory usage and optimized performance
- Interactive command-line interface with response streaming
- Support for multiple LLaMA-based models

## Prerequisites
- Python 3.8 or higher
- llama.cpp Python bindings
- Compatible LLaMA model (GGUF format)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/thesid42/Libra_AI.git
cd Libra_AI/libra_main/llama_env/cli
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up model:
   - Create a models directory in your home folder:
   ```bash
   mkdir ~/.libra_models
   ```
   - Place your GGUF model file in `~/.libra_models/`
   - Set the model path in environment variable (optional):
   ```bash
   export LIBRA_MODEL_PATH=~/.libra_models/your-model.gguf
   ```

## Usage

Run the CLI:
```bash
python index.py
```

Type your prompts at the `>>>` prompt. Use Ctrl+C or Ctrl+D to exit.

## Configuration
- Default model path: `~/.libra_models/model.gguf`
- Context window: 4096 tokens
- Thread count: Automatically uses all available CPU cores
- GPU layers: Configurable in `index.py` (default: 0)

## Project Structure
```
cli/
├── __init__.py          # Package initializer
├── index.py             # Main CLI interface and entry point
├── model_handler.py     # Core model interaction and response generation
├── config.py            # Configuration settings and parameters
├── cache.py            # Search results caching implementation
├── search_utils.py     # Web search utilities for context enhancement
├── requirements.txt    # Project dependencies
└── .gitignore         # Git ignore rules
```

