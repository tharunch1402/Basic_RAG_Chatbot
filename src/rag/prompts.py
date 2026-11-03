from langchain_core.prompts import ChatPromptTemplate

RAG_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a helpful assistant that answers questions using ONLY the "
        context below. If the answer is not in the context, say: 
        I don't know based on the document.
        "Keep answers clear and concise.\n\n
        "Context:\n{context}""",
        ),
        ("human", "{question}"),
    ]
)
