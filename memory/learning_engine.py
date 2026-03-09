from utils.logger import get_logger
from memory.memory_store import MemoryStore

logger = get_logger()


class LearningEngine:

    def __init__(self):
        self.memory_store = MemoryStore()

    def record_interaction(
        self,
        original_input: str,
        parsed_problem: str,
        retrieved_context: str,
        solution: str,
        verifier_result: str,
        feedback: str = None
    ):

        record = {
            "original_input": original_input,
            "parsed_problem": parsed_problem,
            "retrieved_context": retrieved_context,
            "solution": solution,
            "verifier_result": verifier_result,
            "feedback": feedback
        }

        try:
            self.memory_store.store(record)
        except Exception:
            logger.exception("Failed to record interaction")

    def record_feedback(
        self,
        original_input: str,
        solution: str,
        feedback: str
    ):

        try:
            self.memory_store.update_feedback(original_input, feedback)
            logger.info(f"Feedback recorded: {feedback}")
        except Exception:
            logger.exception("Failed to record feedback")