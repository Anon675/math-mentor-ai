import streamlit as st

def show_extraction_preview(text, confidence=None):

    st.markdown("### Extraction Preview")

    st.text_area(
        "Extracted Text",
        value=text,
        height=150
    )

    if confidence is not None:
        st.caption(f"OCR/ASR Confidence: {round(confidence,3)}")