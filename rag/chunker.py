from typing import List
from utils.config_loader import load_settings

settings = load_settings()

class TextChunker:

    def __init__(self):
        self.chunk_size = settings["rag"]["chunk_size"]
        self.chunk_overlap = settings["rag"]["chunk_overlap"]

    def chunk(self, documents: List[str]) -> List[str]:
        chunks = []

        for doc in documents:
            start = 0
            length = len(doc)

            while start < length:
                end = start + self.chunk_size
                chunk = doc[start:end]
                chunks.append(chunk)
                start = end - self.chunk_overlap

        return chunks