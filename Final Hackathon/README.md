# 🧠 Agentic AI – Multi-Agent Feedback & Competitor Review System

An Agentic AI system that streamlines **peer feedback analysis** and **competitor discovery** using a multi-agent LangChain pipeline powered by Google Gemini and RAG. Built with Streamlit for interactive input via text, PDFs, images, or URLs.

---

## 🚀 Features

✅ **5 Modular Agents**:
- 🤖 Feedback Collection Agent (cleans & standardizes input)
- 🧾 Feedback Summarization Agent (extracts insights)
- 🔍 Competitor Discovery Agent (RAG-enabled)
- 🧩 Review Analysis Agent (processes competitor reviews)
- ✨ Refinement Suggestion Agent (improves the idea)

✅ Supports:
- 🔤 Text, 📄 PDF, 🖼 Image, 🌐 URL inputs
- 📎 OCR for PDFs and images
- 🔎 Web scraping from URLs
- 📚 Dynamic RAG-based retrieval (ChromaDB + SentenceTransformers)

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io)
- **Backend**: [LangChain](https://www.langchain.com), [Gemini API](https://ai.google.dev)
- **Vector DB**: [ChromaDB](https://www.trychroma.com)
- **Embeddings**: `all-MiniLM-L6-v2` (Hugging Face)
- **OCR**: `pytesseract`, `pdf2image`
- **Search**: `requests`, `BeautifulSoup` for web scraping

---

## 📦 Installation

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/agentic-feedback-system.git
cd agentic-feedback-system
```

### Create a Virtual Environment

```bash
python3.12 -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔐 Environment Setup

- Create a .env file in the root folder:

```bash
GOOGLE_API_KEY=your_google_gemini_api_key_here
```
You can get your Gemini API key from: https://aistudio.google.com/app/apikey

## 🧪 Running the App

```bash
streamlit run main.py
```
Then open the browser at http://localhost:8501

## 📁 Project Structure
.
├── main.py                 # Streamlit frontend + agent pipeline
├── agents.py              # All 5 agent functions (LLM + prompt chains)
├── rag_utils.py           # ChromaDB, embedding, OCR, and web scraping
├── utils.py               # Copy-to-clipboard helper
├── requirements.txt       # All Python dependencies
├── .env                   # (Not committed) API keys
├── uploads/               # Temp file uploads
├── README.md              # You're here

## 📌 Example Use Cases

- 💡 Startup project feedback refinement
- 🏫 Peer review analysis in classrooms
- 🕵️ Competitor discovery for app/product ideas
- 🛠 UX & feature gap identification from reviews

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

- Fork this repo
- Create a new branch: git checkout -b feature-name
- Commit your changes: git commit -am 'Add new feature'
- Push and open a PR: git push origin feature-name

## 🧼 TODO

 Add auto-review scraping from App Store / Play Store
 Enable persona-based refinement suggestions
 Export reports to PDF or Notion

## Video Link
<video controls src="Screen Recording 2025-06-20 at 7.36.25 PM.mov" title="Title"></video>

Reference Link : [Reference Link of my Project](https://drive.google.com/file/d/1uD-UFcN3-1mTjlsnEMz0p3l-OsigClmV/view?usp=sharing)

## 📜 License

MIT License © 2025 Sanjai S.

By Sanjai S
---
