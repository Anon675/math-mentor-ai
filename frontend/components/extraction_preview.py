import streamlit as st


def render_extraction(problem_input):

    if problem_input is None:
        st.info("No input detected.")
        return

    extracted_text = None

    if isinstance(problem_input, str):
        extracted_text = problem_input

    else:
        extracted_text = getattr(problem_input, "name", "Uploaded file detected")

    st.text_area(
        label="Extracted Problem",
        value=extracted_text,
        height=150,
        disabled=True
    )