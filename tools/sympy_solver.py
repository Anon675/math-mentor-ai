import sympy as sp
from typing import Dict, Any
from utils.logger import get_logger

logger = get_logger()


class SympySolver:

    def __init__(self):
        pass

    def solve_equation(self, equation: str, variable: str = "x") -> Dict[str, Any]:
        try:
            var = sp.symbols(variable)
            expr = sp.sympify(equation)

            solutions = sp.solve(expr, var)

            return {
                "success": True,
                "solutions": [str(sol) for sol in solutions]
            }

        except Exception as e:
            logger.exception("Sympy solving failed")
            return {
                "success": False,
                "error": str(e)
            }

    def simplify(self, expression: str) -> Dict[str, Any]:
        try:
            expr = sp.sympify(expression)
            simplified = sp.simplify(expr)

            return {
                "success": True,
                "result": str(simplified)
            }

        except Exception as e:
            logger.exception("Sympy simplify failed")
            return {
                "success": False,
                "error": str(e)
            }