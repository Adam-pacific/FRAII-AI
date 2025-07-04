import time
from openai import OpenAI, RateLimitError
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def summarize_text(prompt):
    retries = 3
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except RateLimitError:
            if attempt < retries - 1:
                time.sleep(5 * (attempt + 1))  # exponential backoff
            else:
                return "❌ GPT API Rate Limit reached. Please try again later."
