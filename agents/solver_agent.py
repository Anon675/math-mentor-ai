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
        self.api_key = get_env("GROK_API_KEY")
        self.base_url = settings["api"]["grok_base_url"]
        self.model = settings["api"]["model"]

        self.retriever = Retriever()
        self.sympy = SympySolver()

    def solve(self, problem_text: str):

        retrieved_docs = self.retriever.retrieve(problem_text)
        context = "\n".join(retrieved_docs)

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
            ]
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        response = requests.post(
            f"{self.base_url}/chat/completions",
            headers=headers,
            json=payload,
            timeout=settings["api"]["timeout_seconds"]
        )

        response.raise_for_status()

        solution = response.json()["choices"][0]["message"]["content"]

        return {
            "solution": solution,
            "retrieved_context": retrieved_docs
        }