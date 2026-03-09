import requests

from rag.retriever import Retriever
from tools.sympy_solver import SympySolver

from utils.config_loader import load_settings, load_prompts, get_env
from utils.logger import get_logger


logger = get_logger()

settings = load_settings()
prompts = load_prompts()


class SolverAgent:

    def __init__(self):

        self.api_key = get_env("GROQ_API_KEY")
        self.base_url = settings["api"]["groq_base_url"]
        self.model = settings["api"]["model"]
        self.timeout = settings["api"]["timeout_seconds"]

        self.retriever = Retriever()
        self.sympy = SympySolver()

    def solve(self, problem_text: str):

        try:

            # ----------------------------------
            # 1. Try symbolic solve first
            # ----------------------------------

            try:

                symbolic_solution = self.sympy.solve(problem_text)

                if symbolic_solution:

                    logger.info("Solved using Sympy")

                    return {
                        "solution": str(symbolic_solution),
                        "steps": ["Solved using symbolic math (Sympy)."],
                        "retrieved_context": []
                    }

            except Exception:

                logger.warning("Sympy solver failed, falling back to LLM")

            # ----------------------------------
            # 2. Retrieve RAG context
            # ----------------------------------

            retrieved_docs = self.retriever.retrieve(problem_text)

            context = "\n".join(retrieved_docs)

            # ----------------------------------
            # 3. Prepare LLM prompt
            # ----------------------------------

            system_prompt = prompts["solver_agent"]["system_prompt"]

            user_prompt = prompts["solver_agent"]["user_prompt_template"].format(
                problem=problem_text,
                context=context
            )

            payload = {
               "model": self.model,
    "messages": [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    "temperature": 0,
    "max_tokens": 1024,
    "stream": False
}

            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            # ----------------------------------
            # 4. Call Groq API
            # ----------------------------------

            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=headers,
                json=payload,
                timeout=self.timeout
            )

            response.raise_for_status()

            data = response.json()

            if "choices" not in data:
                raise ValueError("Invalid API response format")

            solution_text = data["choices"][0]["message"]["content"]

            return {
                "solution": solution_text,
                "steps": [],
                "retrieved_context": retrieved_docs
            }

        except Exception as e:

            logger.exception("SolverAgent failed")

            return {
                "solution": f"Solver error: {str(e)}",
                "steps": [],
                "retrieved_context": []
            }