# main.py
import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from agents import feedback_agent, persona_agent, refinement_agent, analysis_agent
from rag_utils import (
    extract_text_from_pdf, extract_text_from_image,
    embed_docs, query_docs, web_search_text
)
from utils import copy_to_clipboard

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

st.set_page_config(page_title="Agentic AI Workshop", layout="centered")
st.title("🧠 Agentic Multi-Agent Feedback System")

# Input
mode = st.radio("Input Type:", ["Text", "Upload PDF", "Upload Image", "URL"])
text_input = ""
if mode == "Text":
    text_input = st.text_area("Enter feedback or project idea")
elif mode in ["Upload PDF", "Upload Image"]:
    file = st.file_uploader("Upload file", type=("pdf" if mode=="Upload PDF" else ["png","jpg","jpeg"]))
    if file:
        tmp = "uploads/tmp" + (".pdf" if mode=="Upload PDF" else ".png")
        with open(tmp, "wb") as f:
            f.write(file.read())
        text_input = extract_text_from_pdf(tmp) if mode=="Upload PDF" else extract_text_from_image(tmp)
elif mode == "URL":
    url = st.text_input("Enter URL")
    if url:
        text_input = web_search_text(url)

persona = st.selectbox("Persona Lens:", ["Generic", "Developer", "Marketer", "Investor"])

if st.button("Analyze"):
    if not text_input:
        st.error("No input")
        st.stop()

    # RAG: persist + query
    embed_docs([text_input], ["doc1"])
    rag_msgs = query_docs(text_input)

    # Apply agents
    fb = feedback_agent(llm).invoke({"feedback": text_input}).content
    per = persona_agent(llm, persona).invoke({"feedback": text_input}).content
    ref = refinement_agent(llm).invoke({"idea": text_input, "feedback": fb}).content
    ana = analysis_agent(llm).invoke({"idea": text_input, "feedback": fb}).content

    # Display with copy button
    st.markdown("### 🧾 Feedback Summary")
    st.write(fb)
    if st.button("Copy Feedback"):
        copy_to_clipboard(fb) and st.success("Copied!")

    st.markdown("### 👥 Persona Perspective")
    st.write(per)
    if st.button("Copy Persona"):
        copy_to_clipboard(per) and st.success("Copied!")

    st.markdown("### ✨ Project Refinement")
    st.write(ref)
    if st.button("Copy Refinement"):
        copy_to_clipboard(ref) and st.success("Copied!")

    st.markdown("### 🚀 Strategic Analysis")
    st.write(ana)
    if st.button("Copy Analysis"):
        copy_to_clipboard(ana) and st.success("Copied!")

    st.markdown("### 📊 RAG Insights")
    if isinstance(rag_msgs, dict):
        st.write(rag_msgs.get(0, "No insights found."))
    elif isinstance(rag_msgs, list):
        st.write(rag_msgs[0])
    else:
        st.write(str(rag_msgs))
