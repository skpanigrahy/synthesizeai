# 🧠 SynthesizeAI

A Streamlit-powered suite of AI agents to summarize and analyze documents, audio, video, web pages, GitHub repos, and even generate system architecture — all locally and with ease.

---

## 🚀 Features

- 🎧 Summarize audio & video using Whisper
- 📄 Summarize documents and PDFs
- 🌐 Extract and summarize content from webpages
- 💻 Understand GitHub repositories
- 🏗️ Generate system architecture & prototype ideas
- 🧩 Modular & local — no API key needed

---

## 🛠️ Setup Instructions

```bash
git clone https://github.com/skpanigrahy/SynthesizeAI.git
cd SynthesizeAI
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## 📁 Agents Inside

| **Agent Name**            | **Description**                                                              |
|---------------------------|-------------------------------------------------------------------------------|
| Audio/Video Summarizer    | Upload `.mp3`, `.mp4`, `.wav` for transcription & summary                    |
| Document Summarizer       | Upload `.txt` or `.pdf` documents for quick summaries                        |
| Web Page Analyzer         | Enter any URL and get a short summary                                        |
| Codebase Explainer        | Enter a raw `README.md` link or file for summary                             |
| Architecture Generator    | Describe a product or idea & get a basic blueprint                           |


## 📘 Notes

<details> <summary><strong>Click to expand notes & tips</strong></summary> <br>
<strong>⚙️ Whisper runs locally:</strong> 
Uses openai/whisper. For better performance on low-resource machines, switch to lighter models like tiny or base.

<strong>📄 PDF Support:</strong> 
Extend the Document Summarizer using libraries like pdfplumber or PyMuPDF to extract text effectively from .pdf files.

<strong>🤖 Hugging Face Compatibility:</strong>
All agents are powered by Hugging Face pipelines. You can plug in your own models with minimal effort.

<strong>🧱 Modular by Design:</strong>
Each agent is standalone and can be integrated, replaced, or extended independently.

<strong>🌐 UI Optional:</strong>
The system works with or without the Streamlit UI. You can use the agents via CLI or embed them in API services.

<strong>🔒 Local-first Philosophy:</strong>
All model inference is designed to run locally by default, unless you configure external APIs like Hugging Face Hub or OpenAI.

</details>

## 🤝 Contributing
We welcome contributions from the community! Here's how you can get involved:
- Fork the repository
- Create a new branch for your feature or bugfix<br>
- Commit your changes
- Push to your forked repo
- Open a Pull Request – and feel free to tag us for review 🚀

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

💬 Contact
For questions or feedback, reach out to skpanigrahy.