import streamlit as st
from memory.learning_engine import LearningEngine

learning_engine = LearningEngine()


def render_feedback(problem_text, solution):

    st.markdown("### Human Feedback (Human-in-the-Loop)")

    if not problem_text or not solution:
        return

    col1, col2 = st.columns(2)

    with col1:
        if st.button("👍 Helpful", use_container_width=True):

            try:
                learning_engine.record_feedback(
                    original_input=problem_text,
                    solution=solution,
                    feedback="helpful"
                )
                st.success("Feedback recorded.")
            except Exception:
                st.warning("Feedback storage failed.")

    with col2:
        if st.button("👎 Not Helpful", use_container_width=True):

            try:
                learning_engine.record_feedback(
                    original_input=problem_text,
                    solution=solution,
                    feedback="not_helpful"
                )
                st.warning("Feedback recorded.")
            except Exception:
                st.warning("Feedback storage failed.")