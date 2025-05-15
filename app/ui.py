import streamlit as st
import requests

st.set_page_config(page_title="MediGuide", page_icon="💊", layout="centered")

# Use transparent background with readable text colors
st.markdown(
    """
    <style>
        html, body, [class*="css"]  {
            font-family: 'Segoe UI', sans-serif;
        }
        .title {
            font-size: 2.2em;
            font-weight: 700;
            color: #fafafa;
        }
        .subtitle {
            font-size: 1.05em;
            color: #cccccc;
        }
        .answer-box {
            background-color: #1f1f1f;
            padding: 1rem;
            border-radius: 10px;
            margin-top: 1rem;
            color: #f1f1f1;
            font-size: 1.05em;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='title'>🩺 MediGuide — Your Medication Q&A Assistant</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Ask any question about common medications and get quick, AI-powered guidance based on medical sources.</div>", unsafe_allow_html=True)

query = st.text_input("💬 Enter your medication question:")

if st.button("🔍 Ask MediGuide") and query:
    with st.spinner("🧠 Thinking..."):
        try:
            response = requests.post("http://localhost:8000/ask", json={"query": query})
            if response.status_code == 200:
                result = response.json().get("answer")
                st.markdown(f"<div class='answer-box'>💡 <strong>Answer:</strong><br>{result}</div>", unsafe_allow_html=True)
            else:
                st.error("⚠️ The API didn't return a valid response.")
        except Exception as e:
            st.error(f"❌ Failed to connect to the MediGuide API.\n\n{e}")

st.markdown("---")
st.caption("MediGuide is a local AI-powered app and does not replace professional medical advice.")
