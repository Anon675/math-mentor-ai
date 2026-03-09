import json
import requests

from utils.config_loader import load_settings, load_prompts, get_env
from utils.logger import get_logger


logger = get_logger()
settings = load_settings()
prompts = load_prompts()


class ParserAgent:

    def __init__(self):
        self.api_key = get_env("GROQ_API_KEY")
        self.base_url = settings["api"]["grok_base_url"]
        self.model = settings["api"]["model"]
        self.timeout = settings["api"]["timeout_seconds"]

    def parse(self, problem_text: str):

        system_prompt = prompts["parser_agent"]["system_prompt"]

        user_prompt = prompts["parser_agent"]["user_prompt_template"].format(
            problem=problem_text
        )

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            "temperature": 0
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:

            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=headers,
                json=payload,
                timeout=self.timeout
            )

            response.raise_for_status()

            data = response.json()

            content = data["choices"][0]["message"]["content"]

            try:
                parsed = json.loads(content)
                return parsed

            except Exception:

                logger.warning("Parser response was not valid JSON")

                return {
                    "problem_text": problem_text,
                    "topic": "algebra",
                    "variables": ["x"],
                    "constraints": [],
                    "needs_clarification": False
                }

        except Exception:

            logger.exception("ParserAgent failed")

            return {
                "problem_text": problem_text,
                "topic": "algebra",
                "variables": ["x"],
                "constraints": [],
                "needs_clarification": False
            }