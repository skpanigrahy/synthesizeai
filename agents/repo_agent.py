import streamlit as st
import requests
from transformers import pipeline

def process_code_repo():
    st.subheader("GitHub Repo Explainer")
    url = st.text_input("Enter GitHub repo URL (raw .md or README)")
    if url:
        content = requests.get(url).text
        summarizer = pipeline("summarization")
        summary = summarizer(content, max_length=150, min_length=40, do_sample=False)
        st.success("Explanation:")
        st.write(summary[0]['summary_text'])
