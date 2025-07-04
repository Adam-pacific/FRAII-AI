import streamlit as st
import pandas as pd  # optional, but good to include

def generate_summary(df):
    st.markdown("### 📊 Dataset Summary")
    st.write("🧮 Number of Rows:", df.shape[0])
    st.write("🧾 Number of Columns:", df.shape[1])
    st.write("🧠 Column Names:", list(df.columns))
    st.write("🔍 Missing Values:", df.isnull().sum())
    st.write("📈 Basic Stats:")
    st.write(df.describe())
