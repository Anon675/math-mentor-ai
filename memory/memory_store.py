import sqlite3
from pathlib import Path
from typing import Dict, List, Any
from utils.config_loader import load_settings
from utils.logger import get_logger

logger = get_logger()
settings = load_settings()


class MemoryStore:

    def __init__(self):
        db_path = Path(settings["memory"]["database_path"])
        db_path.parent.mkdir(parents=True, exist_ok=True)

        self.conn = sqlite3.connect(db_path)
        self._create_tables()

    def _create_tables(self):
        query = """
        CREATE TABLE IF NOT EXISTS problem_memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_input TEXT,
            parsed_problem TEXT,
            retrieved_context TEXT,
            solution TEXT,
            verifier_result TEXT,
            feedback TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def store(self, record: Dict[str, Any]):
        query = """
        INSERT INTO problem_memory
        (original_input, parsed_problem, retrieved_context, solution, verifier_result, feedback)
        VALUES (?, ?, ?, ?, ?, ?)
        """

        values = (
            record.get("original_input"),
            record.get("parsed_problem"),
            record.get("retrieved_context"),
            record.get("solution"),
            record.get("verifier_result"),
            record.get("feedback"),
        )

        self.conn.execute(query, values)
        self.conn.commit()

    def fetch_all(self) -> List[Dict]:
        cursor = self.conn.cursor()
        rows = cursor.execute("SELECT * FROM problem_memory").fetchall()

        columns = [col[0] for col in cursor.description]

        results = []
        for row in rows:
            results.append(dict(zip(columns, row)))

        return results