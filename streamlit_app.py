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
audio_bytes = st_audiorec()

if audio_bytes:
    # Save audio to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        tmp_file.write(audio_bytes)
        audio_path = tmp_file.name

    st.success("Audio recorded! Processing...")
