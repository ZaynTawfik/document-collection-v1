import streamlit as st
from st_audiorec import st_audiorec
import whisper
import tempfile
import os
from PIL import Image
import pytesseract

# Set app title
st.title("AI Document Collection Agent 🗂️")
