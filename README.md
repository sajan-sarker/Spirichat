# 👻 SPIRICHAT
## 📌 Project Overview
**SPIRICHAT** is a Retrieval-Augmented Generation (RAG) chatbot that combines the power of a language model with external knowledge retrieval to generate more accurate and context-aware response. It answers queries about supernatural topics like ghosts, spirits, and haunted places by retrieving context from PDF books. Built with LLMs, vector databases, and document parsing for accurate, spooky, and insightful responses.

## ✨ Features
- 🔎 Context-aware document retrieval using embeddings
- 🧠 Language model response generation
- 📚 Knowledge base built from PDF documents
- 🗂️ Pinecone-powered vector storage 
- ⚙️ Configurable RAG pipeline
- 💬 Persistent Chat history support
- 🌐 Minimal web UI using Flask

## Requirements
* 🐍 Python 3.10+
* 🧩 LangChain 0.3+
* 📦 All other dependencies in `requirements.txt`

## 🛠️ Tech Stack

| Tool               | Purpose                                       |
|-------------------------|------------------------------------------|
| Python 3.12         |    Programming Language |
| OpenAI GPT-3.5         | Language model for generating responses   |
| Embedding         | Text embedding via HuggingFace `sentence-transformers/all-MiniLM-L6-v2` |
| Pinecone         | Vector database to store and search embeddings    |
| LangChain         | PAG pipeline framework    |
| Flask         | Lightweight backend and frontend web framework    |

## 🧠 How It Works (RAG Overview)
```bash
  📄 Document Upload → 🧬 Chunk & Embed → 📦 Store in Pinecone →
❓ User Query → 🔍 Retrieve Context → 🤖 Generate Answer via OpenAI

```
1. 📄 Input documents are parsed and chunked using LangChain.
2. 🧬 Each chunk is embedded using HuggingFace's MiniLM model.
3. 🧠 Embeddings are stored in Pinecone vector DB.
4. ❓ User asks a question via the UI.
5. 🔍 Most relevant 5 chunks are retrieved from Pinecone and select best 3 chunks and clean it.
6. 🤖 OpenAI's GPT model generates an answer using both context and the query.


## 🚀 Getting Started
1. Clone the repository:
  ```bash
    git clone https: https://github.com/sajan-sarker/Spirichat.git
    cd Spirichat
  ```
2. Create virtual environment and activate it:
  ```bash
    python3.12 -m venv spirichat
    spirichat\Scripts\Activate
  ```
3. Install dependencies:
  ```bash
    pip install -r requirements.txt
  ```

## ⚙️ Setup Instructions
1. Rename `.env.example` to `.env` and configure your API keys (OpenAI/HuggingFace, Pinecone).

2. Prepare the Knowledge Base:
  ```bash
    python -m app.init_knowledge_base
  ```
3. Run the Chatbot:
  ```bash
  python main.py
  ```
4. Access the Chatbot via the web interface at `http://localhost:5000` (or the configured port).

## 📁 Project Directory Structure
```
Spirichat/
├── app/                          # 🔧 Core backend logic for RAG-based QA chatbot
│   ├── __init__.py               # Initializes the app package
│   ├── config.py                 # Configuration loader (e.g., env vars like API keys, model names)
│   ├── init_knowledge_base.py    # Script to load, chunk, and embed documents into Pinecone Vector Database
│   ├── prompt.py                 # Prompt template used in the retrieval-augmented generation chain
│   ├── qa_chain.py               # Builds and exposes the LangChain QA chain using vector store
│   └── utils.py                  # Utility functions (load PDFs, text chunking, prompt formatting)
├── data/                         # 📂 Directory to store knowledge base documents (PDF, text, etc.)
│   └── ...                       # Source documents
├── notebook/                     # 📓 Jupyter notebooks for testing and experimentation
│   └── implement.ipynb           # Example notebook for prototyping or debugging the chain
├── static/                       # 🎨 Static assets served by Flask
│   ├── css/                      # Custom CSS files for styling the UI
│   ├── img/                      # Images used in the web interface (e.g., logos, icons)
│   └── js/                       # JavaScript files 
├── templates/                    # 🖼 HTML templates for rendering frontend pages
│   └── index.html                # Main UI for chatbot interaction
├── .env.example                  # 🌱 Example environment file (rename to `.env` and update with keys)
├── LICENSE                       # 📜 License file (e.g., MIT, Apache 2.0 — for open source publishing)
├── main.py                       # 🚀 Main Flask app entry point (runs the web server)
├── README.md                     # 📘 Project overview, setup guide, usage, and contribution details
├── requirements.txt              # 📦 Python dependencies for the whole project (LangChain, Flask, etc.)
```


## 🔍 Spirichat Demo
### 🖼️ Image Previews

<table>
  <tr>
    <td><img src="https://github.com/sajan-sarker/Spirichat/blob/main/uploads/Demo_0.png?raw=true" width="100%"/></td>
    <td><img src="https://github.com/sajan-sarker/Spirichat/blob/main/uploads/Demo_1.png?raw=true" width="100%"/></td>
  </tr>
</table>

---

### 📹 Video Demonstration

<p align="center">
  <a href="https://youtu.be/MgRCnwNbePg" target="_blank">
    <img src="https://img.youtube.com/vi/MgRCnwNbePg/0.jpg" alt="Watch the demo" width="100%"/>
  </a>
</p>

## 👨‍💻 Author

Developed by [Sajan Sarker](https://github.com/sajan-sarker)  
🌟 If you found this project helpful or spooky — give it a ⭐ star!
