from rag.config import settings
from rag.vector_store import load_vectorstore


def get_retriever():
    ''' Returns the retreiver '''

    vector_store = load_vectorstore()
    return  vector_store.as_retriever(search_kwargs = {'k':settings.TOP_K})