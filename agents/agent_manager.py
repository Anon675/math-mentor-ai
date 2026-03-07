from agents.parser_agent import ParserAgent
from agents.intent_router_agent import IntentRouterAgent
from agents.solver_agent import SolverAgent
from agents.verifier_agent import VerifierAgent
from agents.explainer_agent import ExplainerAgent
from memory.learning_engine import LearningEngine
from utils.logger import get_logger

logger = get_logger()


class AgentManager:

    def __init__(self):

        self.parser = ParserAgent()
        self.router = IntentRouterAgent()
        self.solver = SolverAgent()
        self.verifier = VerifierAgent()
        self.explainer = ExplainerAgent()

        self.memory = LearningEngine()

    def run_pipeline(self, problem_text: str):

        parsed = self.parser.parse(problem_text)

        topic = self.router.classify(problem_text)

        solution_output = self.solver.solve(problem_text)

        verification = self.verifier.verify(problem_text, solution_output["solution"])

        explanation = self.explainer.explain(problem_text, solution_output["solution"])

        self.memory.record_interaction(
            original_input=problem_text,
            parsed_problem=str(parsed),
            retrieved_context=str(solution_output["retrieved_context"]),
            solution=solution_output["solution"],
            verifier_result=verification,
            feedback=None
        )

        return {
            "parsed_problem": parsed,
            "topic": topic,
            "solution": solution_output["solution"],
            "context": solution_output["retrieved_context"],
            "verification": verification,
            "explanation": explanation
        }