import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# =========================
# ENV
# =========================
load_dotenv()

# =========================
# LLM (from your backend)
# =========================
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2,
    max_tokens=500
)

# =========================
# AI SEARCH LOGIC
# (merged backend.service)
# =========================
def ai_search(query: str) -> str:
    prompt = f"""
You are an AI search engine.
Answer the user's question clearly and accurately.

Question: {query}
"""
    response = llm.invoke(prompt)
    return response.content

# =========================
# STREAMLIT UI (same as yours)
# =========================
st.set_page_config(page_title="AI Search Engine", layout="centered")
st.title("AI Search Engine by Prince Raut")
st.caption("AI: OpenAI | Framework: LangChain")

query = st.text_input("Ask your question")

if st.button("Search"):
    if query:
        with st.spinner("Iam Giving you one of the best answer for your Question....."):
            answer = ai_search(query)

        st.subheader("Answer")
        st.write(answer)
    else:
        st.warning("Please enter a question")
