import json
import os
from typing import Dict, List, Optional
from difflib import SequenceMatcher

MEMORY_FILE = "memory_store.json"


class MemoryStore:

    def __init__(self):

        if not os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "w") as f:
                json.dump([], f)

    def _load_memory(self) -> List[Dict]:

        try:
            with open(MEMORY_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return []

    def _save_memory(self, data: List[Dict]):

        with open(MEMORY_FILE, "w") as f:
            json.dump(data, f, indent=2)

    # ------------------------------------------------
    # Store interaction
    # ------------------------------------------------

    def store(self, record: Dict):

        data = self._load_memory()
        data.append(record)
        self._save_memory(data)

    # ------------------------------------------------
    # Update human feedback (HITL)
    # ------------------------------------------------

    def update_feedback(self, original_input: str, feedback: str):

        data = self._load_memory()

        for item in reversed(data):
            if item.get("original_input") == original_input:
                item["feedback"] = feedback
                break

        self._save_memory(data)

    # ------------------------------------------------
    # Search for similar past question
    # ------------------------------------------------

    def search_similar(self, query: str, threshold: float = 0.75) -> Optional[Dict]:

        data = self._load_memory()

        best_match = None
        best_score = 0

        for item in data:

            stored_question = item.get("original_input", "")

            score = SequenceMatcher(
                None,
                query.lower(),
                stored_question.lower()
            ).ratio()

            if score > best_score:
                best_score = score
                best_match = item

        if best_score >= threshold:
            return best_match

        return None