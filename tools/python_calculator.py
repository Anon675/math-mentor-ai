from typing import Any, Dict
from utils.logger import get_logger

logger = get_logger()


class PythonCalculator:

    def __init__(self):
        self.safe_globals = {
            "__builtins__": {},
        }

    def evaluate(self, expression: str) -> Dict[str, Any]:
        try:
            result = eval(expression, self.safe_globals, {})
            return {
                "success": True,
                "result": result
            }
        except Exception as e:
            logger.exception("Python calculation failed")
            return {
                "success": False,
                "error": str(e)
            }