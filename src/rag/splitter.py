from langchain_text_splitters import RecursiveCharacterTextSplitter
from rag.config import settings

def text_splitter(documents):
    """
    Splits the documents into smaller chunks using RecursiveCharacterTextSplitter.

    Args:
        documents (list): List of documents to be split.

    Returns:
        list: List of split documents.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.CHUNK_SIZE,
        chunk_overlap=settings.CHUNK_OVERLAP,
        length_function=len
    )
    return text_splitter.split_documents(documents)

    