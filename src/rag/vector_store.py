import shutil
from pathlib import Path

from langchain_chroma import Chroma

from rag.config import settings
from rag.embeddings import embeddings_model


def vector_stores(chunks):

    ''' Storing the chunks in the vector store DB '''


    if Path(settings.PERSIST_DIR).exists():
        shutil.rmtree(settings.PERSIST_DIR)

    embeddings = embeddings_model()

    vector_store = Chroma(
        embedding_function = embeddings,
        persist_directory = settings.PERSIST_DIR,
        collection_name = settings.COLLECTION_NAME)

    vector_store.add_documents(chunks)

    return vector_store


def load_vectorstore():

    ''' Loading the vector stores'''

    if not Path(settings.PERSIST_DIR).exists():
        raise FileNotFoundError('No vector DB found. Run scripts/ingest.py first')

    return Chroma(
        embedding_function=embeddings_model(),
        persist_directory=settings.PERSIST_DIR,
        collection_name=settings.COLLECTION_NAME,
    )


