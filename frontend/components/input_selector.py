import streamlit as st

def input_selector():
    option = st.radio(
        "Choose Input Mode",
        ["Text", "Image", "Audio"],
        horizontal=True
    )
    return option