
---


# 🤖 AI-Powered Personal Assistant Agent

A conversational AI agent that serves as your intelligent personal assistant. Built with **LangChain**, **FastAPI**, **OpenAI API**, **Docker**, and a **React** frontend, this assistant understands natural language, maintains memory, and offers smart, context-aware responses.

---

## 🚀 Features

- 💬 **Natural Language Understanding** powered by OpenAI
- 🧠 **Memory Management** for personalized, context-aware replies
- 🔗 Seamless **LangChain** integration for advanced reasoning workflows
- 🖥️ **FastAPI** backend and **React** frontend for a smooth user experience
- 🐳 **Dockerized Deployment** for portability and scalability

---

## 🛠️ Tech Stack

- 🐍 **Python** with [LangChain](https://www.langchain.com/)
- ⚡ **FastAPI** – High-performance backend API
- 🌐 **React** – Responsive, modern frontend
- 🧠 **OpenAI API** – Core intelligence and LLM support
- 📦 **Docker** – Containerized setup for clean deployments



---

## ⚙️ Setup Instructions

### 🧠 Backend (FastAPI + LangChain)

```bash
cd backend
docker build -t ai-assistant .
docker run -d -p 8000:8000 ai-assistant
````

> The backend API will be accessible at: `http://localhost:8000`

---

### 🖥️ Frontend (React)

```bash
cd frontend
npm install
npm run dev
```

> The frontend will run at: `http://localhost:5173`

---

## 🔐 Environment Variables

Create a `.env` file in the `backend/` directory:

```env
OPENAI_API_KEY=your_openai_key_here
```

Make sure your OpenAI key is valid and has access to the required models.

---

## 📬 Contact

Built with ❤️ by [Hasvanth Kalyan Gundu](https://www.linkedin.com/in/hasvanth-kalyan-g-13538a148)
📧 [hasvanthkalyan9@gmail.com](mailto:hasvanthkalyan9@gmail.com)

---

## 🙌 Contributions Welcome!

* Add voice input or speech synthesis
* Integrate calendar, weather, or productivity tools
* Improve memory and retrieval mechanisms with vector databases (e.g., Pinecone, FAISS)

---

