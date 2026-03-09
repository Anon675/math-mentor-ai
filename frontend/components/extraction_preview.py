import streamlit as st
import easyocr
import numpy as np
from PIL import Image
import re


reader = easyocr.Reader(['en'], gpu=False)


def normalize_math_text(text: str):

    text = text.strip()

    # Replace common OCR symbol mistakes
    replacements = {
        "÷": "/",
        "×": "*",
        "–": "-",
        "—": "-",
        "＝": "=",
        "＋": "+",
        "−": "-",
        "S": "5",
        "O": "0",
        "l": "1"
    }

    for k, v in replacements.items():
        text = text.replace(k, v)

    # Convert patterns like x2 → x^2
    text = re.sub(r'([a-zA-Z])\s*2\b', r'\1^2', text)

    # Insert multiplication when number touches variable
    text = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', text)

    # Remove repeated spaces
    text = re.sub(r'\s+', ' ', text)

    return text


def extract_text_from_image(uploaded_file):

    image = Image.open(uploaded_file)
    image_np = np.array(image)

    results = reader.readtext(image_np)

    raw_text = " ".join([item[1] for item in results])

    cleaned_text = normalize_math_text(raw_text)

    return cleaned_text


def render_extraction(problem_input):

    if isinstance(problem_input, str):

        st.text_area(
            "Extracted Problem",
            value=problem_input,
            height=150,
            key="extraction_text"
        )

        return problem_input

    else:

        extracted_text = extract_text_from_image(problem_input)

        st.text_area(
            "Extracted Problem",
            value=extracted_text,
            height=150,
            key="extraction_image"
        )

        return extracted_text