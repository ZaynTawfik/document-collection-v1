import streamlit as st
from st_audiorec import st_audiorec
import whisper
import tempfile
import os
from PIL import Image
import pytesseract

# Set app title
st.title("AI Document Collection Agent 🗂️")

# Record audio using st_audiorec
audio_file = st_audiorec()

if audio_file:
    # Save audio to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        tmp_file.write(audio_file.read())
        audio_path = tmp_file.name

    st.success("Audio recorded! Processing...")

# Load Whisper model (use "tiny" for low RAM, "base" for better accuracy)
model = whisper.load_model("tiny")

# Transcribe audio
if audio_file:
    result = model.transcribe(audio_path)
    transcript = result["text"]
    st.write(f"**You said:** {transcript}")
    os.unlink(audio_path)  # Delete temp file
