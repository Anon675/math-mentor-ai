import streamlit as st

from agents.agent_manager import AgentManager

from frontend.pages.upload_problem import render_upload
from frontend.components.extraction_preview import render_extraction
from frontend.components.agent_trace_panel import render_agent_trace
from frontend.components.context_panel import render_context
from frontend.components.solution_panel import render_solution
from frontend.components.feedback_buttons import render_feedback

from utils.logger import get_logger


logger = get_logger(__name__)


st.set_page_config(
    page_title="Reliable Multimodal Math Mentor",
    layout="wide",
    initial_sidebar_state="collapsed"
)


st.markdown(
"""
<style>

.block-container {
    padding-top: 2rem;
}

.section-box {
    padding: 1.5rem;
    border-radius: 12px;
    background-color: #0e1117;
    border: 1px solid #262730;
}

</style>
""",
unsafe_allow_html=True
)


st.title("Reliable Multimodal Math Mentor")

st.caption(
"Upload, speak, or type a math problem. The AI mentor parses the question, retrieves knowledge, solves it step-by-step, verifies the reasoning, and explains the result."
)


agent_manager = AgentManager()


st.markdown("---")


with st.container():

    st.subheader("Input")

    mode, text_input, uploaded_file = render_upload()


# ------------------------------------------------
# Normalize input so pipeline always receives text
# ------------------------------------------------

problem_text = None

if mode == "Text" and text_input:
    problem_text = text_input

elif mode == "Image" and uploaded_file:
    problem_text = uploaded_file

elif mode == "Audio" and text_input:
    problem_text = text_input


# ------------------------------------------------
# Extraction Preview
# ------------------------------------------------

st.markdown("### Extraction Preview")

if problem_text:
    render_extraction(problem_text)
else:
    st.info("No input detected.")


st.markdown("")


center_col1, center_col2, center_col3 = st.columns([1, 1, 1])

with center_col2:
    solve_clicked = st.button("Solve Problem", use_container_width=True)


# ------------------------------------------------
# Run pipeline
# ------------------------------------------------

if solve_clicked:

    if not problem_text:
        st.warning("Please provide a problem before solving.")
        st.stop()

    try:

        with st.spinner("AI agents are solving the problem..."):

            result = agent_manager.run_pipeline(problem_text)

        trace = result.get("trace", [])
        context = result.get("context", [])

        st.markdown("---")

        st.header("Results")


        left_col, right_col = st.columns([2, 1])


        # -------------------------
        # Solution
        # -------------------------

        with left_col:

            st.markdown("### Solution")

            if result:
                render_solution(result)
            else:
                st.warning("No solution produced by the pipeline.")


        # -------------------------
        # Right panel
        # -------------------------

        with right_col:

            st.markdown("### Agent Execution Trace")
            render_agent_trace(trace)

            st.markdown("")

            st.markdown("### Retrieved Knowledge")
            render_context(context)


        st.markdown("---")

        render_feedback(problem_text, result.get("solution"))


    except Exception as e:

        logger.exception("Pipeline failed")

        st.error(f"Pipeline error: {str(e)}")