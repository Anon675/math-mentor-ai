import streamlit as st
from frontend.components.input_selector import input_selector
from audio_recorder_streamlit import audio_recorder

def render_upload():

    mode = st.radio("Choose Input Mode", ["Text", "Image", "Audio"])

    text_input = None
    uploaded_file = None
    audio_bytes = None   # IMPORTANT: initialize

    if mode == "Text":
        text_input = st.text_area("Enter your math problem")

    elif mode == "Image":
        uploaded_file = st.file_uploader("Upload an image", type=["png","jpg","jpeg"])

    elif mode == "Audio":

     st.subheader("Record or Upload Audio")

    audio_bytes = audio_recorder(
        text="Record",
        recording_color="#e8b62c",
        neutral_color="#6aa36f",
        icon_name="microphone",
        icon_size="2x"
    )

    uploaded_audio = st.file_uploader(
        "Or upload audio file",
        type=["wav", "mp3", "m4a"]
    )

    if audio_bytes:
        st.audio(audio_bytes, format="audio/wav")

        with open("temp_audio.wav", "wb") as f:
            f.write(audio_bytes)

        uploaded_file = "temp_audio.wav"

    elif uploaded_audio is not None:
        uploaded_file = uploaded_audio

    return mode, text_input, uploaded_file