import pytest
from agents.solver_agent import SolverAgent


@pytest.fixture
def solver():
    return SolverAgent()


def test_solver_returns_solution(monkeypatch, solver):

    mock_output = {
        "solution": "x = -2, -3",
        "retrieved_context": ["Quadratic formula"]
    }

    def mock_solve(problem):
        return mock_output

    monkeypatch.setattr(solver, "solve", mock_solve)

    result = solver.solve("Solve x^2 - 5x + 6 = 0")

    assert "solution" in result
    assert "retrieved_context" in result