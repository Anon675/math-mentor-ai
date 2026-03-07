from typing import Dict, Any
from utils.logger import get_logger
from memory.learning_engine import LearningEngine

logger = get_logger()


class FeedbackHandler:

    def __init__(self):
        self.learning_engine = LearningEngine()

    def record_feedback(
        self,
        original_input: str,
        parsed_problem: str,
        retrieved_context: str,
        solution: str,
        verifier_result: str,
        feedback: str
    ) -> Dict[str, Any]:

        try:
            self.learning_engine.record_interaction(
                original_input=original_input,
                parsed_problem=parsed_problem,
                retrieved_context=retrieved_context,
                solution=solution,
                verifier_result=verifier_result,
                feedback=feedback
            )

            return {
                "success": True,
                "message": "Feedback recorded successfully"
            }

        except Exception as e:
            logger.exception("Failed to store user feedback")
            return {
                "success": False,
                "error": str(e)
            }