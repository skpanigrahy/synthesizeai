import streamlit as st
from transformers import pipeline

def process_document():
    st.subheader("Document Summarization")
    uploaded_file = st.file_uploader("Upload document", type=["txt", "pdf"])
    if uploaded_file:
        text = uploaded_file.read().decode("utf-8", errors="ignore")
        summarizer = pipeline("summarization")
        summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
        st.success("Summary:")
        st.write(summary[0]['summary_text'])
