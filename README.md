# 🗳️ CivicGuide AI

An interactive AI assistant that helps users understand the **election process in India 🇮🇳** in a simple, structured, and conversational way.

---

## 🚀 Live Demo
🔗 [Add your Streamlit link here]

---

## 📌 Problem Statement
Build an assistant that explains election processes, timelines, and steps in an **interactive and easy-to-follow manner**.

---

## 💡 Solution

CivicGuide AI is a **chat-based assistant** that:
- Explains elections step-by-step
- Answers user questions dynamically
- Supports follow-up questions (context-aware)
- Provides structured, beginner-friendly responses

---

## ✨ Features

### 🧠 AI Chat Assistant
- Ask anything about elections
- Handles follow-up queries like “yes”, “how?”, “tell more”

### 📚 Guided Learning
- Predefined topics:
  - How elections work  
  - How to vote  
  - Eligibility  
  - Election timeline  

### 🇮🇳 India-Focused Context
- Election Commission of India (ECI)
- Voter ID (EPIC)
- EVM voting system

### 💬 Conversational Memory
- Maintains short chat history
- Enables multi-turn interaction

### ⚡ Clean UI
- Dropdown for quick learning
- Chat interface for deeper exploration
- Dynamic UI (dropdown hides after chat starts)

---

## 🛠️ Tech Stack

- **Frontend & App**: Streamlit  
- **AI Model**: Google Gemini API  
- **Deployment**: Streamlit Community Cloud  

---

## 🧩 How It Works

1. User selects a topic or asks a question  
2. The system builds a structured prompt  
3. Gemini model generates a response  
4. Chat history is maintained using session state  
5. Follow-up questions are handled using context  

---

## ⚙️ Installation (Local Setup)

```bash
git clone https://github.com/adilashaharban/civicguide-ai.git
cd civicguide-ai
pip install -r requirements.txt
streamlit run app.py

## 📄 License

This project is licensed under the MIT License.