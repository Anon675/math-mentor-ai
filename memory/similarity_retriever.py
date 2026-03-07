from typing import List, Dict
from difflib import SequenceMatcher
from utils.config_loader import load_settings
from utils.logger import get_logger
from memory.memory_store import MemoryStore

logger = get_logger()
settings = load_settings()


class SimilarityRetriever:

    def __init__(self):
        self.memory = MemoryStore()
        self.threshold = settings["memory"]["similarity_threshold"]
        self.max_results = settings["memory"]["max_similar_results"]

    def similarity(self, a: str, b: str) -> float:
        return SequenceMatcher(None, a, b).ratio()

    def search(self, query: str) -> List[Dict]:
        records = self.memory.fetch_all()

        scored = []

        for r in records:
            problem = r.get("parsed_problem", "")
            score = self.similarity(query, problem)

            if score >= self.threshold:
                r["similarity"] = score
                scored.append(r)

        scored.sort(key=lambda x: x["similarity"], reverse=True)

        return scored[: self.max_results]