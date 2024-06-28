import os
from pathlib import Path


DATA_PATH = Path(os.environ["DATA_PATH"])
DATA_PATH.mkdir(exist_ok=True)

############## DEFAULT RAG CONFIG ################
DEFAULT_RAG_CHUNK_SIZE = 128
DEFAULT_RAG_CHUNK_OVERLAP = 10
DEFAULT_RAG_SIMILARITY_TOP_K = 4
DEFAULT_RAG_WINDOW_SIZE = 1
DEFAULT_RAG_TOKEN_LIMIT = 2000


#USE FAKE LLMS
USE_MOCK_MODELS = False
USE_LOCAL_MODELS = False # If true, use bge large for embedding, llama3_8b 4bit for generation
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")