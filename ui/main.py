import os

import httpx
import streamlit as st

# Where the API runs. Docker will change this later using an environment variable.
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

st.set_page_config(page_title="Basic RAG Chatbot", page_icon="📄")
st.title("📄 Basic RAG Chatbot")
st.caption("Ask questions about the ingested research paper")

# Keep the chat history while the page is open
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input box at the bottom
if question := st.chat_input("Ask a question about the document"):
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Searching the document..."):
            try:
                response = httpx.post(
                    f"{API_URL}/ask", json={"question": question}, timeout=60
                )
                response.raise_for_status()
                data = response.json()
                pages = ", ".join(str(page) for page in data["pages"])
                answer = f"{data['answer']}\n\n*Sources: pages {pages}*"
            except httpx.HTTPError as error:
                answer = f"⚠️ Could not get an answer from the API: {error}"
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})