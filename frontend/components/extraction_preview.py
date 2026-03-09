import streamlit as st
import easyocr
import numpy as np
from PIL import Image
import re


reader = easyocr.Reader(['en'], gpu=False)


def normalize_math_text(text: str):

    text = text.strip()

    # Replace math symbols
    symbol_map = {
        "÷": "/",
        "×": "*",
        "–": "-",
        "—": "-",
        "＝": "=",
        "＋": "+",
        "−": "-"
    }

    for k, v in symbol_map.items():
        text = text.replace(k, v)

    # Fix powers like x2 → x^2
    text = re.sub(r'([a-zA-Z])\s*2\b', r'\1^2', text)

    # Fix multiplication: 5x → 5*x
    text = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', text)

    # Fix OCR mistake only in math terms
    text = re.sub(r'\bSx\b', '5x', text)
    text = re.sub(r'\bS\s*=\s*', '5 = ', text)

    # Clean spaces
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