import speech_recognition as sr
from gtts import gTTS
import tempfile
import os

def speech_to_text():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source, timeout=5)
            text = r.recognize_google(audio, language='ta-IN')  # works for TA/HI too
            return text
    except Exception as e:
        return f"Error: {e}"

def text_to_speech(text, lang='en'):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tf:
            lang_code = 'en'
            if lang.startswith('ta'):
                lang_code = 'ta'
            elif lang.startswith('hi'):
                lang_code = 'hi'
            gTTS(text=text, lang=lang_code).save(tf.name)
            audio = open(tf.name, 'rb').read()
        os.remove(tf.name)
        return audio
    except:
        return None
