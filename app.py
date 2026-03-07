import streamlit as st
import tempfile
from agents.agent_manager import AgentManager
from multimodal.image_input import ImageInputProcessor
from multimodal.audio_input import AudioInputProcessor
from multimodal.text_input import TextInputProcessor
from frontend.pages.home import render_home
from frontend.pages.upload_problem import render_upload
from frontend.pages.results import render_results
from frontend.components.extraction_preview import show_extraction_preview
from frontend.components.feedback_buttons import feedback_buttons
from hitl.feedback_handler import FeedbackHandler
from utils.logger import get_logger

logger = get_logger()


st.set_page_config(
    page_title="Math Mentor AI",
    layout="wide"
)

if "result" not in st.session_state:
    st.session_state.result = None

if "problem_text" not in st.session_state:
    st.session_state.problem_text = None


render_home()

mode, text_input, uploaded_file = render_upload()

agent_manager = AgentManager()
image_processor = ImageInputProcessor()
audio_processor = AudioInputProcessor()
text_processor = TextInputProcessor()

problem_text = None
confidence = None


if mode == "Text" and text_input:
    processed = text_processor.process(text_input)
    problem_text = processed["text"]
    confidence = processed["confidence"]

elif mode == "Image" and uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        path = tmp.name

    processed = image_processor.process(path)
    problem_text = processed["extracted_text"]
    confidence = processed["confidence"]

elif mode == "Audio" and uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        path = tmp.name

    processed = audio_processor.process(path)
    problem_text = processed["transcript"]
    confidence = processed["confidence"]


if problem_text:
    show_extraction_preview(problem_text, confidence)

    if st.button("Solve Problem"):
        try:
            result = agent_manager.run_pipeline(problem_text)
            st.session_state.result = result
            st.session_state.problem_text = problem_text

        except Exception as e:
            logger.exception("Pipeline failed")
            st.error("Failed to process problem.")


if st.session_state.result:

    render_results(st.session_state.result)

    correct, incorrect, comment = feedback_buttons()

    if correct or incorrect:

        feedback_handler = FeedbackHandler()

        feedback = "correct" if correct else "incorrect"

        if incorrect and comment:
            feedback = f"incorrect: {comment}"

        feedback_handler.record_feedback(
            original_input=st.session_state.problem_text,
            parsed_problem=str(st.session_state.result["parsed_problem"]),
            retrieved_context=str(st.session_state.result["context"]),
            solution=st.session_state.result["solution"],
            verifier_result=st.session_state.result["verification"],
            feedback=feedback
        )

        st.success("Feedback recorded.")