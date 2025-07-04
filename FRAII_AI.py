# FRAII_AI — Multilingual Voice AI Assistant with Self-Healing

import streamlit as st
st.set_page_config(page_title="FRAII AI", page_icon="🏔️", layout="wide")

import pandas as pd
from utils.voice import speech_to_text, text_to_speech
from utils.healer import analyze_and_heal, apply_fix
from utils.memory import init_memory, log_event, show_memory
from utils.agent import auto_fill_form
from utils.email_bot import send_report_email
from utils.news_scraper import get_ai_news
from utils.summary import generate_summary
from langdetect import detect
import os

# 🔧 Initialize session memory
init_memory()
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# 📧 Email Automation Panel
with st.expander("📧 Email Automation"):
    st.image("assets/email_banner.png", width=400)  # Path to your image
    email = st.text_input("Recipient Email")
    msg = st.text_area("Message")
    file_to_attach = st.file_uploader("Optional: Attach a file", type=["pdf", "csv", "xlsx", "txt"])

    if st.button("Send Email"):
        if file_to_attach:
            with open(file_to_attach.name, "wb") as f:
                f.write(file_to_attach.read())
            response = send_report_email(email, "FRAII AI Report", msg, file_to_attach.name)
            os.remove(file_to_attach.name)  # Clean up after sending
        else:
            response = send_report_email(email, "FRAII AI Report", msg)

        st.success(response)


# 📰 Latest AI News Panel
with st.expander("📰 Latest AI News"):
    news = get_ai_news()
    for item in news:
        st.markdown(f"- {item}")

# 🤖 Title
st.title("🤖 FRAII AI — Self-Healing + Voice + Automation")

# 📂 File Upload and Language
col1, col2 = st.columns([4, 1])
with col1:
    uploaded = st.file_uploader("📂 Upload CSV or Excel", type=["csv", "xlsx"])
with col2:
    selected_lang = st.selectbox("🌐 Language", options=["English", "Tamil", "Hindi"], index=0)

lang_code = {"English": "en", "Tamil": "ta", "Hindi": "hi"}[selected_lang]

# 🔄 Load Data
if uploaded and 'df' not in st.session_state:
    if uploaded.name.endswith(".csv"):
        df = pd.read_csv(uploaded)
    elif uploaded.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded)
    st.session_state.df = df
    log_event("uploads", uploaded.name)

# 🛠️ Display & Fix Data
if 'df' in st.session_state:
    df = st.session_state.df
    st.write(df.head())

    for fix in analyze_and_heal(df):
        col = fix.split("'")[1]
        if st.button(f"✅ {fix}"):
            df = apply_fix(df, col)
            st.session_state.df = df
            log_event("fixes", f"Fixed {col}")
            st.rerun()

# 📄 Generate Summary
if 'df' in st.session_state:
    df = st.session_state.df
    st.markdown("### 📄 Summary of Uploaded Data")
    generate_summary(df)

# 🎤 Ask Query
st.markdown("### 💬 Ask a question (voice or type)")
display = st.empty()
user_input = st.chat_input("Ask about profit, fixes...")

# 🧠 Voice Input for Local Only
IS_CLOUD = os.environ.get("STREAMLIT_SERVER_HEADLESS", None) == "1"
if not IS_CLOUD:
    if st.button("🎤 Speak"):
        result = speech_to_text(lang_code)
        if result:
            st.success(f"You said: {result}")
            user_input = result
else:
    st.info("🎙️ Voice input is not supported on Streamlit Cloud. Please use the chat input below.")

# 🧠 Handle Chat
if user_input:
    log_event("queries", user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    lower_input = user_input.lower()
    if any(k in lower_input for k in ["profit", "laabam", "munafa", "லாபம்", "मुनाफा"]):
        if "laabam" in lower_input or "லாபம்" in lower_input:
            reply = "இன்று விற்பனை லாபகரமாக இருக்கிறது. இன்னும் அதிக வருமானத்திற்காக வாடிக்கையாளர் தொடர்புகளை மேம்படுத்துங்கள்."
        elif "munafa" in lower_input or "मुनाफा" in lower_input:
            reply = "आज का मुनाफा स्थिर है। अधिक लाभ के लिए विपणन रणनीतियों में सुधार करें।"
        else:
            reply = "Profit looks stable. Consider maximizing during seasonal demand."
    elif "fix" in lower_input:
        reply = "I've already patched missing values."
    elif "file" in lower_input:
        reply = f"You uploaded: {', '.join(st.session_state.memory['uploads'])}"
    elif "automate" in lower_input:
        reply = auto_fill_form()
    else:
        reply = "Try asking about profit, fixes, uploads, or automation."

    st.session_state.chat_history.append({"role": "assistant", "content": reply})
    st.markdown(f"**🤖 AI**: {reply}")
    st.audio(text_to_speech(reply, lang=lang_code), format='audio/mp3')

# 🧠 Show Memory
if st.checkbox("📜 Show Memory"):
    show_memory()
