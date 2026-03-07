import streamlit as st
from frontend.components.context_panel import show_context
from frontend.components.solution_panel import show_solution
from frontend.components.agent_trace_panel import show_agent_trace

def render_results(result):

    st.markdown("## Results")

    show_agent_trace([
        "Parser Agent",
        "Intent Router",
        "Solver Agent",
        "Verifier Agent",
        "Explainer Agent"
    ])

    show_context(result["context"])

    show_solution(
        result["solution"],
        result["explanation"],
        result["verification"]
    )