# 🛡️ Hercules AI 2.0

**Your AI-Powered Cybersecurity Copilot**

Hercules AI 2.0 is an advanced, open-source vulnerability scanner designed to detect OWASP Top 10 vulnerabilities, misconfigurations, and insecure patterns in modern web apps — especially those built with low-code/no-code platforms and JavaScript frameworks like MERN.

It leverages:

- 🧠 **LLMs (ChatGPT, Gemini)** for code insight and natural explanations  
- 🔎 **RAG (Retrieval-Augmented Generation)** with ExploitDB for enriched vulnerability analysis  
- 📦 **FastAPI** backend with a modular architecture  
- 🧬 **ChromaDB** vector store for semantic search  
- 💬 **Chatbot assistant** to interact with scanned results

---

## 🚀 Features

- ✅ **Scan Source Code & Detect OWASP Top 10**
- 🔐 **Sanitize and Preprocess User Code**
- 🤖 **LLM-powered Analysis Engine** (ChatGPT / Gemini switchable)
- 📚 **ExploitDB + RAG Integration** for real-world context
- 🗂️ **Modular, Extendable Folder Structure**
- 🧠 **Chatbot Assistant** to explain vulnerabilities
- 🐳 **Dockerized Setup** for fast deployment
- 🌐 Optional React Frontend (WIP)

---

## 📁 Project Structure

```
hercules-ai-2.0/
│
├── backend/
│   ├── api/
│   │   └── scan.py               # API endpoint for scan requests
│   ├── rag/
│   │   └── embed.py              # Embed code & store in ChromaDB
│   ├── utils/
│   │   └── sanitizer.py          # Code sanitization & preprocessing
│   └── main.py                   # FastAPI app entry point
│
├── retriever.py                  # RAG retrieval pipeline
├── analyzer.py                   # LLM-based vulnerability analyzer
├── loader.py                     # Load corpus & build index
│
├── data/
│   ├── corpus/                   # Text or exploit documents
│   └── index/                    # ChromaDB persistent index
│
├── requirements.txt              # Python dependencies
├── Dockerfile                    # Docker build file
├── README.md                     # This file ✨
└── .env                          # API keys & configs
```

---

## ⚙️ Installation

### 🔧 Local Setup

```bash
git clone https://github.com/yourname/hercules-ai-2.0.git
cd hercules-ai-2.0
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Add your API keys to `.env`:

```env
OPENAI_API_KEY=your-openai-key
GEMINI_API_KEY=your-gemini-key
USE_LLM=gemini  # or openai
```

Then run the app:

```bash
uvicorn backend.main:app --reload
```

### 🐳 Docker

```bash
docker build -t hercules-ai .
docker run -p 8000:8000 --env-file .env hercules-ai
```

---

## 🧪 Usage

Send a `POST` request to `/scan/`:

```json
{
  "code": "<your source code here>",
  "tech_stack": "MERN"
}
```

Get back:

- Vulnerability details
- Severity
- Mitigation steps
- Links to ExploitDB if found
- Chatbot-ready explanations

---

## 🗣️ Chat Assistant (Beta)

Ask follow-up questions like:

- “Explain this XSS vulnerability”
- “Is this code safe?”
- “How can I fix this SQL injection?”

---

## 📌 Roadmap

- [x] RAG + LLM vulnerability insights  
- [x] ExploitDB integration  
- [x] Chat assistant  
- [ ] Frontend dashboard (React)  
- [ ] Real-time file upload scanning  
- [ ] GitHub integration

---

## 🤝 Contributing

PRs welcome! Open an issue first to discuss what you want to contribute.

---

## 🧠 Credits

- Powered by **FastAPI**, **ChromaDB**, **OpenAI / Gemini LLMs**  
- Vulnerability corpus from **ExploitDB**  
- Created by [Your Name or Team Name]

---

## 📜 License

MIT License. Use it. Fork it. Make the web safer. 🔐
