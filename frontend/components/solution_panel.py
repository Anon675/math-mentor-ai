import streamlit as st


def render_solution(result):

    if not isinstance(result, dict):
        st.warning("Invalid result format.")
        return

    solution = result.get("solution")
    explanation = result.get("explanation")

    st.markdown("## 🧮 Step-by-Step Solution")

    if explanation:
        st.markdown("### Explanation")
        st.write(explanation)

    if solution:
        st.success(f"Final Answer: {solution}")
        st.success(f"Final Answer: {solution}")