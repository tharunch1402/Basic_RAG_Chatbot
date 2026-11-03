# Loads PDF files for the RAG pipeline
from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path

def load_documents(file_path:str):

    """ Load the PDF Documents """

    data_path = Path(file_path)

    if not data_path.exists():
        raise FileNotFoundError(f'The file {data_path} is not exist')

    if data_path.suffix.lower() != '.pdf':
        raise ValueError(f'The Existing file {data_path} is not PDF Format')

    loader = PyPDFLoader(str(data_path))
    documents = loader.load()
    return documents

