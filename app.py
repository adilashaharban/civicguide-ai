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
    topic = st.selectbox(
    "Or choose a topic:",
    ["None", "How elections work", "How to vote", "Eligibility", "Election timeline"]
)

if topic == "How elections work":
    st.markdown("""
📌 **Election Process**
🔹 Voter Registration (Get Voter ID via Election Commission of India)  
🔹 Political Campaigning  
🔹 Voting using EVM machines  
🔹 Vote Counting  
🔹 Results Announcement  

💡 Tip: Always verify your name in the voter list before election day.  
❓ Want to learn how to register?
""")

elif topic == "How to vote":
    st.markdown("""
📌 **How to Vote**
🔹 Carry your Voter ID (EPIC)  
🔹 Visit your assigned polling booth  
🔹 Verify identity  
🔹 Cast vote using EVM  
🔹 Confirm your vote  

💡 Tip: Reach early to avoid long queues.  
❓ Want to know eligibility criteria?
""")

elif topic == "Eligibility":
    st.markdown("""
📌 **Eligibility to Vote**
🔹 Must be 18 years or older  
🔹 Must be an Indian citizen  
🔹 Must be registered with Election Commission of India  

💡 Tip: Apply for Voter ID early to avoid delays.  
❓ Want to learn how to register?
""")

elif topic == "Election timeline":
    st.markdown("""
📌 **Election Timeline**
🔹 Election announcement  
🔹 Campaign period  
🔹 Voting day  
🔹 Vote counting  
🔹 Results declaration  

💡 Tip: Follow official updates from Election Commission of India.  
❓ Want to explore voting steps?
""")

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