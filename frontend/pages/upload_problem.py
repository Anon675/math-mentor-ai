import streamlit as st
from frontend.components.input_selector import input_selector

def render_upload():

    mode = input_selector()

    problem_text = None
    uploaded_file = None

    if mode == "Text":
        problem_text = st.text_area("Enter your math problem")

    elif mode == "Image":
        uploaded_file = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"])

    elif mode == "Audio":
        uploaded_file = st.file_uploader("Upload audio", type=["wav", "mp3"])

    return mode, problem_text, uploaded_file