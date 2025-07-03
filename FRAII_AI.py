import streamlit as st
import pandas as pd
from utils.voice import speech_to_text, text_to_speech
from utils.healer import analyze_and_heal, apply_fix
from utils.memory import init_memory, log_event, show_memory
from utils.agent import auto_fill_form
from langdetect import detect

st.set_page_config(page_title="FRAII AI",page_icon="🏔️", layout="wide")
st.title("🤖 FRAII AI — Self-Healing + Voice + Automation")

init_memory()

# Upload CSV or Excel
uploaded = st.file_uploader("📂 Upload CSV or Excel", type=["csv", "xlsx"])
if uploaded and 'df' not in st.session_state:
    if uploaded.name.endswith(".csv"):
        df = pd.read_csv(uploaded)
    elif uploaded.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded)

    st.session_state.df = df
    log_event("uploads", uploaded.name)

# Display and fix data
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

# Ask queries
st.markdown("### 💬 Ask a question (voice or type)")
display = st.empty()
user_input = st.chat_input("Ask about profit, fixes...")

if st.button("🎙️ Speak"):
    result = speech_to_text()
    if result:
        st.success(f"You said: {result}")
        user_input = result

if user_input:
    log_event("queries", user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    lang = detect(user_input)

    if "profit" in user_input.lower() or "லாபம்" in user_input or "मुनाफा" in user_input:
        reply = "Your profit is good. Keep increasing your margins!"
    elif "fix" in user_input.lower():
        reply = "Missing values are already fixed."
    elif "file" in user_input.lower():
        reply = f"You uploaded: {', '.join(st.session_state.memory['uploads'])}"
    elif "automate" in user_input.lower():
        reply = auto_fill_form()
    else:
        reply = "Try asking about profit, fixes, or file uploads."

    st.session_state.chat_history.append({"role": "assistant", "content": reply})
    st.markdown(f"**🤖 AI**: {reply}")
    st.audio(text_to_speech(reply, lang), format='audio/mp3')

if st.checkbox("🧠 Show Memory"):
    show_memory()
