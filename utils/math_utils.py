import sympy as sp
from typing import Dict, Any

def parse_expression(expr: str):
    try:
        return sp.sympify(expr)
    except Exception as e:
        raise ValueError(f"Invalid mathematical expression: {expr}") from e

def solve_equation(equation: str, variable: str = "x"):
    try:
        var = sp.symbols(variable)
        eq = sp.sympify(equation)
        solutions = sp.solve(eq, var)
        return solutions
    except Exception as e:
        raise ValueError(f"Failed solving equation: {equation}") from e

def simplify_expression(expr: str):
    try:
        return sp.simplify(expr)
    except Exception as e:
        raise ValueError(f"Cannot simplify expression: {expr}") from e

def evaluate_expression(expr: str, variables: Dict[str, Any] = None):
    try:
        sym_expr = sp.sympify(expr)
        if variables:
            sym_expr = sym_expr.subs(variables)
        return float(sym_expr.evalf())
    except Exception as e:
        raise ValueError(f"Evaluation failed for expression: {expr}") from e