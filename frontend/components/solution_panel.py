import streamlit as st

def show_solution(solution, explanation, verification):

    st.markdown("### Final Answer")

    st.markdown("#### Solution")
    st.write(solution)

    st.markdown("#### Explanation")
    st.write(explanation)

    st.markdown("#### Verification")
    st.write(verification)