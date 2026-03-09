import streamlit as st
import easyocr
import numpy as np
from PIL import Image

reader = easyocr.Reader(['en'], gpu=False)


def extract_text_from_image(uploaded_file):

    image = Image.open(uploaded_file)
    image_np = np.array(image)

    result = reader.readtext(image_np)

    text = " ".join([item[1] for item in result])

    return text


def render_extraction(problem_input):

    if isinstance(problem_input, str):

        st.text_area(
            "Extracted Problem",
            value=problem_input,
            height=150,
            key="extraction_text_preview"
        )

        return problem_input

    else:

        extracted_text = extract_text_from_image(problem_input)

        st.text_area(
            "Extracted Problem",
            value=extracted_text,
            height=150,
            key="extraction_image_preview"
        )

        return extracted_text