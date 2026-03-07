import sympy as sp
from typing import Dict
from utils.logger import get_logger

logger = get_logger()


class MathValidator:

    def __init__(self):
        pass

    def validate_equation(self, equation: str) -> Dict:
        try:
            sp.sympify(equation)
            return {
                "valid": True
            }
        except Exception as e:
            logger.exception("Equation validation failed")
            return {
                "valid": False,
                "error": str(e)
            }

    def check_solution(self, equation: str, variable: str, solution) -> Dict:
        try:
            var = sp.symbols(variable)
            expr = sp.sympify(equation)

            test_value = expr.subs(var, solution)

            if test_value == 0:
                return {"valid": True}
            else:
                return {"valid": False}

        except Exception as e:
            logger.exception("Solution verification failed")
            return {
                "valid": False,
                "error": str(e)
            }