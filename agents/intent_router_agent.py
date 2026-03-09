import requests
from utils.config_loader import load_settings, load_prompts, get_env
from utils.logger import get_logger

logger = get_logger()
settings = load_settings()
prompts = load_prompts()


class IntentRouterAgent:

    def __init__(self):
        self.api_key = get_env("GROQ_API_KEY")
        self.base_url = settings["api"]["grok_base_url"]
        self.model = settings["api"]["model"]

    def classify(self, problem_text: str):

        system_prompt = prompts["intent_router_agent"]["system_prompt"]
        user_prompt = prompts["intent_router_agent"]["user_prompt_template"].format(
            problem=problem_text
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

        return response.json()["choices"][0]["message"]["content"].strip()