from langchain_openai import ChatOpenAI

from rag.config import settings


def get_llm():
    '''The chat model that writes the final answer'''
    if not settings.OPENAI_API_KEY:
        raise ValueError('OPENAI_API_KEY not found. Check your .env file')

    return ChatOpenAI(
        api_key=settings.OPENAI_API_KEY,
        model=settings.LLM_MODEL,
        temperature=0,  # 0 = factual, no creativity
    )

