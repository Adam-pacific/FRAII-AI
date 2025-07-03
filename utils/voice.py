import speech_recognition as sr
from gtts import gTTS
import tempfile
import os

def speech_to_text(lang='en'):
    try:
        lang_map = {'en': 'en-US', 'ta': 'ta-IN', 'hi': 'hi-IN'}
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source, timeout=5)
            text = r.recognize_google(audio, language=lang_map.get(lang, 'en-US'))
            return text
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
