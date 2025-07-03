import os
import speech_recognition as sr
from gtts import gTTS
import tempfile

def speech_to_text(lang_code='en'):
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source, timeout=5)
            return r.recognize_google(audio, language=lang_code)
    except Exception as e:
        # Graceful fallback message for PyAudio or mic errors
        return "🎙️ Voice input is disabled on Streamlit Cloud. Please use the text box."

def text_to_speech(text, lang='en'):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tf:
            gTTS(text=text, lang=lang).save(tf.name)
            with open(tf.name, 'rb') as f:
                return f.read()
    except:
        return None
