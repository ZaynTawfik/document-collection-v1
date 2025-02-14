import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import speech_recognition as sr

# Audio-only configuration
media_stream_constraints = {
    "video": False,  # Disable camera
    "audio": True,   # Enable microphone
}

def audio_frame_callback(frame: av.AudioFrame) -> av.AudioFrame:
    # Process audio here (if needed)
    return frame

ctx = webrtc_streamer(
    key="voice_input",
    mode="sendonly",  # Only send audio (no video)
    media_stream_constraints=media_stream_constraints,
    rtc_configuration={"iceServers": []},  # No STUN/TURN servers for simplicity
    audio_frame_callback=audio_frame_callback,
)

# Speech recognition logic
if ctx.audio_receiver:
    st.write("Speak now...")
    audio_frames = []
    try:
        for frame in ctx.audio_receiver.iter_frames():
            audio_frames.append(frame)
            if len(audio_frames) > 20:  # Process after 20 frames (adjust as needed)
                break
        if audio_frames:
            recognizer = sr.Recognizer()
            audio_data = b"".join([f.to_ndarray().tobytes() for f in audio_frames])
            text = recognizer.recognize_google(audio_data)
            st.session_state.user_text = text
    except Exception as e:
        st.error(f"Error: {e}")
