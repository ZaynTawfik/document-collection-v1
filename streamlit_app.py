import streamlit as st
from st_audiorec import st_audiorec
import speech_recognition as sr
import io

# Title
st.title("AI Document Collection Agent 🗂️")

# Audio recorder widget
audio_bytes = st_audiorec()

# Speech-to-text processing
if audio_bytes:
    # Convert bytes to AudioFile
    audio_data = io.BytesIO(audio_bytes)
    audio_data.name = "recording.wav"  # Filename needed for recognizer
    
    # Transcribe using Google ASR
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_data) as source:
        audio = recognizer.record(source)
        try:
            user_text = recognizer.recognize_google(audio)
            st.session_state.user_text = user_text
            st.write(f"**You said:** {user_text}")
        except sr.UnknownValueError:
            st.error("Could not understand audio")
        except sr.RequestError:
            st.error("API unavailable")
