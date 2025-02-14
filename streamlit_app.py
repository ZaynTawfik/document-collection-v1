import streamlit as st
from streamlit_webrtc import webrtc_streamer
import speech_recognition as sr
import av

def transcribe_audio(audio_frame):
    recognizer = sr.Recognizer()
    audio_data = av.AudioFrame.from_ndarray(
        audio_frame.to_ndarray(), format="f32le", layout="mono"
    )
    text = recognizer.recognize_google(audio_data.to_wav_bytes())
    return text

ctx = webrtc_streamer(key="voice_input", rtc_configuration={"iceServers": []})
if ctx.audio_receiver:
    audio_frames = []
    for frame in ctx.audio_receiver.iter_frames():
        audio_frames.append(frame)
    if audio_frames:
        user_text = transcribe_audio(audio_frames[-1])  # Process last frame
        st.session_state.user_text = user_text

if "user_text" in st.session_state:
    st.write(f"**You said:** {st.session_state.user_text}")
