from rag.loader import load_folder
from rag.splitter import text_splitter
from rag.vector_store import vector_stores

import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s"
)


def main():
    documents = load_folder("data")
    print("Pages loaded:", len(documents))

    chunks = text_splitter(documents)
    print("Chunks created:", len(chunks))

    vector_stores(chunks)
    print("Stored in Chroma ✅")


if __name__ == "__main__":
    main()
