import streamlit as st

def feedback_buttons():

    st.markdown("### Feedback")

    col1, col2 = st.columns(2)

    correct = col1.button("✅ Correct")
    incorrect = col2.button("❌ Incorrect")

    comment = None

    if incorrect:
        comment = st.text_area("Explain what was wrong")

    return correct, incorrect, comment