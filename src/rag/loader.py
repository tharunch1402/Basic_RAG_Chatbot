import logging
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader

logger = logging.getLogger(__name__)


def load_documents(file_path: str):
    '''Load one PDF file and return its pages'''
    data_path = Path(file_path)

    if not data_path.exists():
        raise FileNotFoundError(f'File not found: {data_path}')

    if data_path.suffix.lower() != '.pdf':
        raise ValueError(f'{data_path} is not a PDF file')

    loader = PyPDFLoader(str(data_path))
    return loader.load()


def load_folder(folder_path: str):
    '''Load every PDF in a folder. A broken file is skipped, not fatal.'''
    folder = Path(folder_path)

    if not folder.is_dir():
        raise FileNotFoundError(f'Folder not found: {folder}')

    all_documents = []

    for pdf in sorted(folder.glob('*.pdf')):
        try:
            documents = load_documents(str(pdf))
            all_documents.extend(documents)
            logger.info(f'Loaded {pdf.name} ({len(documents)} pages)')
        except Exception as error:
            logger.error(f'Could not load {pdf.name}: {error}')

    if not all_documents:
        raise ValueError(f'No PDFs could be loaded from {folder}')

    return all_documents