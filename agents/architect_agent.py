import streamlit as st
from transformers import pipeline

def generate_architecture():
    st.subheader("Architecture & Prototype Generator")
    input_text = st.text_area("Describe your product or idea")
    if st.button("Generate"):
        generator = pipeline("text-generation")
        output = generator(f"Create an architectural blueprint and prototype plan for: {input_text}",
                           max_length=300, do_sample=True)[0]['generated_text']
        st.success("Generated Architecture:")
        st.write(output)
