import streamlit as st

st.set_page_config(page_title="CivicGuide AI", page_icon="🗳️")

st.title("🗳️ CivicGuide AI")
st.subheader("Understand Elections in India — Step by Step 🇮🇳")

menu = st.selectbox(
    "Choose what you want to learn:",
    ["How elections work", "How to vote", "Eligibility", "Election timeline"]
)

if menu == "How elections work":
    st.markdown("""
📌 **Election Process**
🔹 Voter Registration (Get Voter ID)  
🔹 Political Campaigning  
🔹 Voting using EVM  
🔹 Vote Counting  
🔹 Results Announcement  

💡 Tip: Always check your name in the voter list before voting.  
❓ Want to learn how to register?
""")

elif menu == "How to vote":
    st.markdown("""
📌 **How to Vote**
🔹 Carry your Voter ID  
🔹 Go to polling booth  
🔹 Verify identity  
🔹 Cast vote using EVM  
🔹 Confirm vote  

💡 Tip: Voting is your right — don’t skip it!  
❓ Want eligibility details?
""")

elif menu == "Eligibility":
    st.markdown("""
📌 **Eligibility**
🔹 Must be 18+  
🔹 Indian citizen  
🔹 Registered voter  

💡 Tip: Apply early for your Voter ID.  
❓ Want to know registration steps?
""")

elif menu == "Election timeline":
    st.markdown("""
📌 **Timeline**
🔹 Election announcement  
🔹 Campaign period  
🔹 Voting day  
🔹 Counting  
🔹 Results  

💡 Tip: Follow official updates from ECI.  
❓ Want to explore voting steps?
""")