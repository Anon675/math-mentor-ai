import streamlit as st
from audio_recorder_streamlit import audio_recorder
import whisper
import tempfile


@st.cache_resource
def load_whisper():
    return whisper.load_model("tiny")


model = load_whisper()


def transcribe_audio(audio_bytes):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(audio_bytes)
            path = tmp.name

        result = model.transcribe(path)
        return result["text"]

    except Exception:
        return ""


def render_upload():

    mode = st.radio("Choose Input Mode", ["Text", "Image", "Audio"])

    text_input = None
    uploaded_file = None

    # ---- TEXT ----
    if mode == "Text":

        text_input = st.text_area(
            "Enter your math problem",
            height=120
        )

    # ---- IMAGE ----
    elif mode == "Image":

        uploaded_file = st.file_uploader(
            "Upload image",
            type=["png", "jpg", "jpeg"]
        )

        if uploaded_file:
            st.image(uploaded_file)

    # ---- AUDIO ----
    elif mode == "Audio":

        st.subheader("Record or Upload Audio")

        audio_bytes = audio_recorder()

        uploaded_audio = st.file_uploader(
            "Upload audio file",
            type=["wav", "mp3", "m4a", "webm"]
        )

        if audio_bytes:

            st.audio(audio_bytes)

            transcription = transcribe_audio(audio_bytes)

            if transcription:
                st.text_area("Transcribed Problem", transcription, height=120)
                text_input = transcription
            else:
                st.warning("Could not transcribe audio.")

        elif uploaded_audio:

            audio_bytes = uploaded_audio.read()

            st.audio(audio_bytes)

            transcription = transcribe_audio(audio_bytes)

            if transcription:
                st.text_area("Transcribed Problem", transcription, height=120)
                text_input = transcription
            else:
                st.warning("Could not transcribe audio.")

    return mode, text_input, uploaded_file