import streamlit as st
from agents.audio_video_agent import process_av_file
from agents.document_agent import process_document
from agents.webpage_agent import process_webpage
from agents.repo_agent import process_code_repo
from agents.architect_agent import generate_architecture
from utils.ui import show_header

st.set_page_config(page_title="SynthesizeAI", layout="wide")
show_header()

menu = ["Audio/Video Summarizer", "Document Summarizer", "Web Page Analyzer",
        "Codebase Explainer", "Architecture Generator"]
choice = st.sidebar.selectbox("Choose an Agent", menu)

if choice == "Audio/Video Summarizer":
    process_av_file()
elif choice == "Document Summarizer":
    process_document()
elif choice == "Web Page Analyzer":
    process_webpage()
elif choice == "Codebase Explainer":
    process_code_repo()
elif choice == "Architecture Generator":
    generate_architecture()
