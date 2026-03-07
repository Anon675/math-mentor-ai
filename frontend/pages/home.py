import streamlit as st
from frontend.styles.ui_styles import apply_global_styles

def render_home():

    apply_global_styles()

    st.markdown(
        '<div class="main-title">Reliable Multimodal Math Mentor</div>',
        unsafe_allow_html=True
    )

    st.write(
        """
        Upload or type a math problem and let the AI mentor solve it step-by-step.
        Supported Inputs:
        - Image (OCR)
        - Audio (Speech-to-Text)
        - Text
        """
    )