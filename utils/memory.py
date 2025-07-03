import streamlit as st

def init_memory():
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'memory' not in st.session_state:
        st.session_state.memory = {'uploads': [], 'fixes': [], 'queries': []}

def log_event(key, value):
    st.session_state.memory[key].append(value)

def show_memory():
    st.json(st.session_state.memory)
