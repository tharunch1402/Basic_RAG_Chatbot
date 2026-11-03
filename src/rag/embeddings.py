from langchain_openai import OpenAIEmbeddings

from rag.config import settings


def embeddings_model():
    ''' Creating the embedding model '''

    if not settings.OPENAI_API_KEY:
        raise ValueError('OPENAI_API_KEY not found. Check your .env file')

    embedding_model = OpenAIEmbeddings(
        model = settings.EMBEDDING_MODEL,
        api_key = settings.OPENAI_API_KEY,
        dimensions = settings.EMBEDDING_SIZE

    )

    return embedding_model
