import streamlit as st
import google.generativeai as genai
import os

# 🔑 API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# 🤖 Model
model = genai.GenerativeModel("models/gemini-flash-latest")

# 🧠 Chat memory (stored in session)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 🎨 UI
st.set_page_config(page_title="CivicGuide AI", page_icon="🗳️")

# ✅ Sticky Header (SAFE)
st.markdown("""
<style>

/* Target Streamlit top bar */
header[data-testid="stHeader"] {
    position: relative;
}

/* Add custom title inside top bar */
header[data-testid="stHeader"]::before {
    content: "🗳️ CivicGuide AI";
    position: absolute;
    left: 20px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 18px;
    font-weight: 600;
    color: inherit;
}

/* Optional: adjust spacing so it doesn't overlap */
header[data-testid="stHeader"] {
    padding-left: 180px;
}

</style>
""", unsafe_allow_html=True)
#st.title("🗳️ CivicGuide AI")
st.subheader("Understand Elections in India 🇮🇳")

# ✅ Show dropdown ONLY before chat starts
if len(st.session_state.chat_history) == 0:
    topic = st.selectbox(
        "Or choose a topic:",
        ["None", "How elections work", "How to vote", "Eligibility", "Election timeline"],
        key="topic_selector"
    )
else:
    topic = "None"


# ✅ SHOW CONTENT BASED ON SELECTION
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

# 💬 Show chat history
for role, msg in st.session_state.chat_history:
    if role == "user":
        st.markdown(f"**You:** {msg}")
    else:
        st.markdown(f"**CivicGuide AI:** {msg}")

# 💬 Chat input (bottom)
user_input = st.chat_input("Ask anything about elections...")

if user_input:
    # Save user message
    st.session_state.chat_history.append(("user", user_input))

    with st.spinner("Thinking..."):

        # 🧠 Build conversation context (last few messages)
        history_text = ""
        for role, msg in st.session_state.chat_history[-4:]:
            history_text += f"{role}: {msg}\n"

        prompt = f"""
You are CivicGuide AI, an interactive assistant for Indian elections 🇮🇳.

RULES:
1. If the question is about elections → explain clearly with structure.
2. If the question is NOT related to elections:
   - Answer normally in a simple way
   - Do NOT force election context
3. If unsure about a person or fact:
   - Say "I'm not sure" instead of guessing

INSTRUCTIONS:
- Continue conversation naturally
- Understand follow-ups like "yes", "how?", "tell more"
- Use previous context
- Keep answers simple
- Use bullet points (max 5)

FORMAT:
📌 Topic  
🔹 Point 1  
🔹 Point 2  

💡 Tip  

❓ Ask next question

CONVERSATION:
{history_text}

USER:
{user_input}
"""

        try:
            response = model.generate_content(prompt)

            # ✅ Safe response handling
            if response and hasattr(response, "text") and response.text:
                reply = response.text
            else:
                reply = "⚠️ Sorry, I couldn't generate a response. Please try again."

            # Save AI response
            st.session_state.chat_history.append(("bot", reply))

        except Exception as e:
            st.error(f"Error: {e}")