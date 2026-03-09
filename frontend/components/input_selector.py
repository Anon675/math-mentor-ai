import streamlit as st


def input_selector():

    mode = st.radio(
        "Choose Input Method",
        ["Text", "Image", "Audio"],
        horizontal=True
    )

    text_input = None
    uploaded_file = None

    if mode == "Text":

        text_input = st.text_area(
            "Enter Math Problem",
            height=120
        )

    elif mode == "Image":

        uploaded_file = st.file_uploader(
            "Upload Image",
            type=["png", "jpg", "jpeg"]
        )

    elif mode == "Audio":

        uploaded_file = st.file_uploader(
            "Upload Audio",
            type=["wav", "mp3", "m4a"]
        )

    return mode, text_input, uploaded_file