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

        trace = []

        # ------------------------------------------------
        # 1. Check memory for similar problem
        # ------------------------------------------------

        try:
            similar = self.memory.memory_store.search_similar(problem_text)

            if similar:

                trace.append({
                    "agent": "MemoryStore",
                    "action": "Reused similar past solution",
                    "output": similar.get("solution")
                })

                return {
                    "parsed_problem": similar.get("parsed_problem"),
                    "topic": "memory_reuse",
                    "solution": similar.get("solution"),
                    "steps": [],
                    "context": similar.get("retrieved_context", []),
                    "verification": similar.get("verifier_result"),
                    "explanation": "Solution reused from previous similar question.",
                    "trace": trace
                }

        except Exception:
            logger.exception("Memory lookup failed")

        # ------------------------------------------------
        # 2. Normal pipeline
        # ------------------------------------------------

        parsed = self.parser.parse(problem_text)

        trace.append({
            "agent": "ParserAgent",
            "action": "Parsed input",
            "output": str(parsed)
        })

        topic = self.router.classify(problem_text)

        trace.append({
            "agent": "IntentRouterAgent",
            "action": "Classified topic",
            "output": topic
        })

        solution_output = self.solver.solve(problem_text)

        solution = solution_output.get("solution")
        steps = solution_output.get("steps", [])
        context = solution_output.get("retrieved_context", [])

        trace.append({
            "agent": "SolverAgent",
            "action": "Generated solution",
            "output": solution
        })

        verification = self.verifier.verify(problem_text, solution)

        trace.append({
            "agent": "VerifierAgent",
            "action": "Verified result",
            "output": verification
        })

        explanation = self.explainer.explain(problem_text, solution)

        trace.append({
            "agent": "ExplainerAgent",
            "action": "Generated explanation",
            "output": explanation
        })

        # ------------------------------------------------
        # 3. Store interaction in memory
        # ------------------------------------------------

        try:

            self.memory.record_interaction(
                original_input=problem_text,
                parsed_problem=str(parsed),
                retrieved_context=str(context),
                solution=solution,
                verifier_result=verification,
                feedback=None
            )

        except Exception:
            logger.exception("Memory recording failed")

        return {
            "parsed_problem": parsed,
            "topic": topic,
            "solution": solution,
            "steps": steps,
            "context": context,
            "verification": verification,
            "explanation": explanation,
            "trace": trace
        }