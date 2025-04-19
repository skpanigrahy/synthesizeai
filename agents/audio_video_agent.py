import streamlit as st
from transformers import pipeline
import whisper
import tempfile

def process_av_file():
    st.subheader("Audio/Video Summarization")
    uploaded_file = st.file_uploader("Upload audio/video file", type=["mp3", "mp4", "wav"])
    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(uploaded_file.read())
            audio_path = tmp.name

        model = whisper.load_model("base")
        result = model.transcribe(audio_path)
        st.success("Transcript:")
        st.text_area("", result["text"], height=200)

        summarizer = pipeline("summarization")
        summary = summarizer(result["text"], max_length=100, min_length=30, do_sample=False)
        st.success("Summary:")
        st.write(summary[0]['summary_text'])
