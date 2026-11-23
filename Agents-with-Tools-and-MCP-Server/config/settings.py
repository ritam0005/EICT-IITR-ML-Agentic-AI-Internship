import os
from dotenv import load_dotenv

load_dotenv()

MODEL = os.getenv("MODEL_NAME", "llama3.2:latest")
BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

APP_NAME = "Multi-Agent Analytics Assistant"

TEMPERATURE = 0.2
MAX_ITER = 3
VERBOSE = True