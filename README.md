# Agentic AI Workshop

This repository contains a collection of mini‑projects developed as part of an **Agentic AI Workshop**. Each mini‑project explores a unique aspect of intelligent agent systems—from report generation to multi‑agent pipelines.

## 🚀 Features

This workshop showcases:

- **Business & Financial Reporting**: AI‑generated business summaries and financial analysis.
- **RAG Systems**: Retrieval‑Augmented Generation pipelines for information‑augmented outputs.
- **Web Research Agents**: AI agents conducting web research and synthesizing findings.
- **Travel Assistants**: AI tools to assist with travel planning and travel‑related Q&A.
- **Early Adopter Outreach Strategist**: Persona identification, personalized outreach, and timing recommendations for startups.
- **Multi‑Agent Feedback & Competitor Review System**: Agent pipelines for peer feedback, competitor analysis, and decision support.

## 🛠 Tech Stack

### Backend
- Python 3.10+
- FastAPI (used in Day 7)
- LangChain (for orchestrating agentic workflows)
- Gemini API (Google Generative AI)
- Ollama + Mistral 7B (for local model inference)
- `requests`, `BeautifulSoup` (web scraping support)

### Frontend
- Streamlit (used in Day 6 & Hackathon UI)

### Optional Database
- ChromaDB (for vector‑store storage during Hackathon)

## 📁 Project Structure

Each daily mini‑project is self‑contained:

| Day             | Focus                                         | Contents                                       |
|---------------- |-----------------------------------------------|------------------------------------------------|
| Day 1           | Business Report on Generative AI              | .md, PDF documents                             |
| Day 2           | Financial Report Assignment                   | .md, PDF documents                             |
| Day 3           | RAG Dataset Creation                          | Jupyter Notebooks, Python scripts              |
| Day 4           | Agent‑based Web Research                      | Jupyter Notebooks, Python scripts, PDF report  |
| Day 5           | Travel Assistant & Study Tool                 | Jupyter Notebooks, Python scripts, PDF outputs |
| Day 6           | Early Adopter Outreach Strategist (Streamlit) | Multi‑agent persona, outreach, and feedback UI |
| Day 7           | Outreach API‑driven Strategist (FastAPI)      | API server + RAG‑driven endpoints              |
| Final Hackathon | Multi‑Agent Feedback & Competitor Review      | Streamlit UI + LangChain + Gemini + ChromaDB   |

## ⚙️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/Sanjai-SNS/Agentic_AI_Workshop.git
   cd Agentic_AI_Workshop
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   Navigate into each day's folder and run:
   ```bash
   pip install -r requirements.txt
   ```

4. **(Optional) Set up local LLMs**
   - Install Ollama: https://ollama.ai
   - Pull `mistral-7b`:
     ```bash
     ollama pull mistral:7b
     ```

5. **(Optional) Set up Gemini API**
   Create a `.env` file with:
   ```
   GOOGLE_API_KEY=<your_gemini_key>
   ```

## 🏃 Running Projects

### Day 6 (Streamlit App)
```bash
cd Day6
streamlit run main.py
```

### Day 7 (FastAPI Endpoints)
```bash
cd Day7
uvicorn api:app --reload
```
Endpoints:
- `POST /persona`
- `POST /outreach`
- `POST /templates`
- `POST /engagement`
- `POST /full`

Example:
```bash
curl -X POST http://localhost:8000/persona \
  -H "Content-Type: application/json" \
  -d '{"name":"YourStartup","description":"We help creators monetize faster."}'
```

### Final Hackathon
```bash
cd Final_Hackathon
streamlit run main.py
```

## 🧑‍💻 Contribution

Contributions are welcome:

1. Fork the repo  
2. Create a feature branch: `git checkout -b feature-name`  
3. Commit changes with clear messages  
4. Push to your fork and open a PR

## 📄 License

Licensed under the MIT License. See [LICENSE](LICENSE) for details.

## 🆘 Support

For issues or questions, please open an issue in this repository.

---

**Happy Hacking with Agentic AI! 🤖✨**
