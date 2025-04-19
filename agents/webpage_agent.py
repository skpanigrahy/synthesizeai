import streamlit as st
import requests
from bs4 import BeautifulSoup
from transformers import pipeline

def process_webpage():
    st.subheader("Web Page Analyzer")
    url = st.text_input("Enter webpage URL")
    if url:
        html = requests.get(url).text
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text()
        summarizer = pipeline("summarization")
        summary = summarizer(text, max_length=150, min_length=40, do_sample=False)
        st.success("Summary:")
        st.write(summary[0]['summary_text'])
