import streamlit as st

def apply_global_styles():
    st.markdown(
        """
        <style>
        .main-title {
            font-size:32px;
            font-weight:700;
            color:#1f4e79;
        }
        .section-title {
            font-size:22px;
            font-weight:600;
            margin-top:20px;
        }
        .panel-box {
            padding:15px;
            border-radius:10px;
            border:1px solid #e6e6e6;
            background:#fafafa;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )