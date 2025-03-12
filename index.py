import os
from pathlib import Path
import time
import sys
from prompt_toolkit import prompt
from llama_cpp import Llama
from model_handler import ModelHandler
from config import MODEL_PATH  # Add this import

def initialize_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"Model not found at {MODEL_PATH}\n"
            "Please ensure the model file is in the correct location"
        )
    
    try:
        return Llama(
            model_path=MODEL_PATH,
            n_ctx=4096,         # Increased context window
            n_threads=os.cpu_count(),
            n_gpu_layers=0,    # Set to 0 if no GPU, or higher (35-40) if you have a GPU
            verbose=False       # Reduce noise in output
        )
    except Exception as e:
        raise RuntimeError(f"Failed to initialize model: {str(e)}")

def format_duration(seconds: float) -> str:
    return f"{seconds:.2f}s" if seconds < 60 else f"{int(seconds//60)}m {seconds%60:.2f}s"

def main():
    try:
        print("Initializing model (optimized for local use)...")
        model = ModelHandler()
        print("Model loaded successfully!")
        
        while True:
            try:
                user_input = prompt(">>> ")
                print("\nThinking...", flush=True)
                
                start_time = time.time()
                sys.stdout.write("\033[A\033[K")  # Clear thinking message
                
                # Stream the response
                print("")
                for text_chunk in model.generate_response(user_input):
                    print(text_chunk, end="", flush=True)
                
                duration = time.time() - start_time
                print(f"\n\n⏱️  Generated in: {format_duration(duration)}\n")
                
            except (EOFError, KeyboardInterrupt):
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {str(e)}")
    
    except Exception as e:
        print(f"Fatal error: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())

