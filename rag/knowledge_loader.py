from pathlib import Path
from typing import List
from utils.logger import get_logger

logger = get_logger()

class KnowledgeLoader:
    def __init__(self, base_path: str = "data"):
        self.base_path = Path(base_path)

    def load_documents(self) -> List[str]:
        documents = []

        if not self.base_path.exists():
            logger.warning("Knowledge base directory does not exist.")
            return documents

        for file_path in self.base_path.rglob("*.md"):
            try:
                content = file_path.read_text(encoding="utf-8")
                documents.append(content)
            except Exception as e:
                logger.exception(f"Failed loading document: {file_path}")

        logger.info(f"{len(documents)} documents loaded from knowledge base")
        return documents