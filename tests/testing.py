from rag.loader import load_documents
from rag.splitter import text_splitter
from rag.vector_store import vector_stores


def main():
    documents = load_documents('data/AI.pdf')
    print('Pages loaded:', len(documents))

    chunks = text_splitter(documents)
    print('Chunks created:', len(chunks))

    vector_stores(chunks)
    print('Stored in Chroma ✅')


if __name__ == '__main__':
    main()