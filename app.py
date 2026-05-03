import streamlit as st
import google.generativeai as genai
import os

# 🔑 Load API key from Streamlit secrets
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-pro")

# UI
st.set_page_config(page_title="CivicGuide AI", page_icon="🗳️")

st.title("🗳️ CivicGuide AI")
st.subheader("Ask anything about elections in India 🇮🇳")

# Optional: Quick selection (nice UX)
topic = st.selectbox(
    "Or choose a topic:",
    ["None", "How elections work", "How to vote", "Eligibility", "Election timeline"]
)

if topic != "None":
    st.info(f"You selected: {topic}")

# 💬 MAIN CHAT INPUT (THIS IS THE IMPORTANT PART)
user_input = st.text_input("Ask anything about elections:")

if user_input:
    with st.spinner("Thinking..."):

        prompt = f"""
You are CivicGuide AI, an interactive assistant that explains elections in India 🇮🇳.

INSTRUCTIONS:
- Explain in simple language (like teaching a beginner)
- Use bullet points (max 5)
- Keep answers short and clear
- Include Indian context when relevant:
  - Election Commission of India
  - Voter ID (EPIC)
  - EVM voting system

FORMAT:
📌 Topic Title  
🔹 Point 1  
🔹 Point 2  
🔹 Point 3  

💡 Tip: (1 helpful tip)

❓ End with a question to continue conversation

USER QUESTION:
{user_input}
"""

        response = model.generate_content(prompt)

        st.markdown(response.text)