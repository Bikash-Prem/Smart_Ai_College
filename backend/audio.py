import pyttsx3
import threading
import speech_recognition as sr

# ==============================

# SAFE SPEAK (no shared engine)

# ==============================

def _speak(text):
    try:
        engine = pyttsx3.init()  # NEW engine every time
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print("TTS Error:", e)

def speak(text):
    thread = threading.Thread(target=_speak, args=(text,))
    thread.start()

# ==============================

# LISTEN

# ==============================

def listen():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("🎤 Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text.lower()

    except Exception as e:
        print("Speech Error:", e)
        return "Could not understand"
