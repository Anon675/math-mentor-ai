import streamlit as st
from audio_recorder_streamlit import audio_recorder
import whisper
import tempfile

# Load Whisper model once
model = whisper.load_model("base")


def transcribe_audio(audio_bytes):

    try:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(audio_bytes)
            tmp_path = tmp.name

        result = model.transcribe(tmp_path)

        return result["text"]

    except Exception:
        return ""


def render_upload():

    mode = st.radio(
        "Choose Input Mode",
        ["Text", "Image", "Audio"]
    )

    text_input = None
    uploaded_file = None

    # -------------------------
    # TEXT INPUT
    # -------------------------

    if mode == "Text":

        text_input = st.text_area(
            "Enter your math problem",
            height=120,
            placeholder="Example: Solve x^2 + 5x + 6 = 0"
        )

    # -------------------------
    # IMAGE INPUT
    # -------------------------

    elif mode == "Image":

        uploaded_file = st.file_uploader(
            "Upload an image",
            type=["png", "jpg", "jpeg"]
        )

        if uploaded_file:

            st.image(uploaded_file)

            text_input = uploaded_file

    # -------------------------
    # AUDIO INPUT
    # -------------------------

    elif mode == "Audio":

        st.subheader("Record or Upload Audio")

        audio_bytes = audio_recorder()

        uploaded_audio = st.file_uploader(
            "Or upload audio file",
            type=["wav", "mp3", "m4a", "webm"]
        )

        # Recorded audio
        if audio_bytes:

            st.audio(audio_bytes)

            transcription = transcribe_audio(audio_bytes)

            if transcription:

                st.success("Audio transcribed successfully")

                st.text_area(
                    "Transcribed Problem",
                    value=transcription,
                    height=120
                )

                text_input = transcription

            else:
                st.warning("Could not transcribe audio.")

        # Uploaded audio
        elif uploaded_audio:

            audio_bytes = uploaded_audio.read()

            st.audio(audio_bytes)

            transcription = transcribe_audio(audio_bytes)

            if transcription:

                st.success("Audio transcribed successfully")

                st.text_area(
                    "Transcribed Problem",
                    value=transcription,
                    height=120
                )

                text_input = transcription

            else:
                st.warning("Could not transcribe audio.")

    return mode, text_input, uploaded_file