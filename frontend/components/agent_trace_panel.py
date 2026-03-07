import streamlit as st

def show_agent_trace(trace):

    st.markdown("### Agent Execution Trace")

    for step in trace:
        st.write(f"• {step}")