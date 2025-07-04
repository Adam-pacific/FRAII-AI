import openai
import os
import streamlit as st

# Load your OpenAI API key
openai.api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")

def summarize_dataframe(df):
    try:
        sample_text = df.head(10).to_string(index=False)
        prompt = f"Summarize the key insights from this data:\n{sample_text}"

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
        )
        return response.choices[0].message["content"]

    except Exception as e:
        return f"❌ GPT summarization failed: {e}"
