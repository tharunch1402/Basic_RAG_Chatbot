import os

from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # Models
    EMBEDDING_MODEL = 'text-embedding-3-small'
    LLM_MODEL = 'gpt-4o-mini'

    # Chunking
    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 50

    # Vector database
    PERSIST_DIR = "chroma_db"
    COLLECTION_NAME = "Production_RAG"

    # Retrieval: how many chunks to send to the LLM
    TOP_K = 3

    # Embedding size
    EMBEDDING_SIZE = 1536
settings = Settings()