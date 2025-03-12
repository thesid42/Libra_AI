import os
from pathlib import Path

HOME_DIR = Path.home()
MODELS_DIR = HOME_DIR / ".libra_models"
os.makedirs(MODELS_DIR, exist_ok=True)

MODEL_PATH = os.getenv(
    "LIBRA_MODEL_PATH", 
    str(MODELS_DIR / "model.gguf")
)

MODEL_CONFIG = {
    'model_path': MODEL_PATH,
    'n_ctx': 2048,          # Reduced for faster responses
    'n_threads': 4,         # Specific thread count for better control
    'n_gpu_layers': 35,     # Maximum GPU usage for local
    'seed': 42,
    'n_batch': 512,         # Increased batch size
    'verbose': False,
    'f16_kv': True,         # Use float16 for key/value cache
    'use_mmap': True,       # Use memory mapping
    'use_mlock': True,      # Lock memory to prevent swapping
}

GENERATION_CONFIG = {
    'max_tokens': 1024,     # Reduced for faster responses
    'temperature': 0.7,
    'top_p': 0.95,
    'repeat_penalty': 1.1,
    'echo': False,
    'stream': True          # Enable streaming responses
}

SEARCH_CONFIG = {
    'enabled': True,
    'results_count': 2,     # Reduced for faster searches
    'cache_size': 100,      # Number of searches to cache
    'cache_ttl': 3600,      # Cache TTL in seconds
}

PROMPT_TEMPLATE = """[INST] Based on the following information and your knowledge, please provide a comprehensive answer:

{search_results}

User Question: {user_input} [/INST]"""
