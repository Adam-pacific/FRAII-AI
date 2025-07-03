import os
import speech_recognition as sr
from gtts import gTTS
import tempfile

def speech_to_text(lang_code='en'):
    # Skip voice on Streamlit Cloud
    if os.environ.get("STREAMLIT_SERVER_HEADLESS", "") == "1":
        return "Voice input not supported on Streamlit Cloud."

    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source, timeout=5)
            return r.recognize_google(audio, language=lang_code)
    except Exception as e:
        return f"Error: {e}"

def text_to_speech(text, lang='en'):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tf:
            gTTS(text=text, lang=lang).save(tf.name)
            audio = open(tf.name, 'rb').read()
        os.remove(tf.name)
        return audio
    except:
        return None
