import pytest
from agents.parser_agent import ParserAgent


@pytest.fixture
def parser():
    return ParserAgent()


def test_parser_output_structure(monkeypatch, parser):

    mock_response = {
        "problem_text": "Solve x^2 + 5x + 6 = 0",
        "topic": "algebra",
        "variables": ["x"],
        "constraints": [],
        "needs_clarification": False
    }

    def mock_parse(problem):
        return mock_response

    monkeypatch.setattr(parser, "parse", mock_parse)

    result = parser.parse("Solve x^2 + 5x + 6 = 0")

    assert isinstance(result, dict)
    assert "problem_text" in result
    assert "topic" in result
    assert "variables" in result
    assert "constraints" in result
    assert "needs_clarification" in result