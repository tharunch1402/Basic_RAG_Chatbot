from rag.llm import get_llm
from rag.prompts import RAG_PROMPT
from rag.retriever import get_retriever


def format_docs(docs):
    '''Join the retrieved chunks into one text, with page numbers'''
    return "\n\n".join(
        f"[Page {doc.metadata.get('page', 0) + 1}]\n{doc.page_content}"
        for doc in docs
        )


def ask_question(question: str):
    '''Question → find chunks → send to LLM → answer'''
    # 1. Retrieve the most relevant chunks
    retriever = get_retriever()
    docs = retriever.invoke(question)

    # 2. Fill the prompt with the chunks and the question
    context = format_docs(docs)
    messages = RAG_PROMPT.invoke({"context": context, "question": question})

    # 3. Ask the LLM
    response = get_llm().invoke(messages)

    # 4. Return the answer and the pages it came from
    pages = sorted({doc.metadata.get('page', 0) + 1 for doc in docs})
    return {"answer": response.content, "pages": pages}