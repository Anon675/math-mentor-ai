import faiss
import numpy as np
from pathlib import Path
from utils.config_loader import load_settings
from utils.logger import get_logger

logger = get_logger()
settings = load_settings()

class VectorStore:

    def __init__(self):
        self.store_path = Path(settings["rag"]["vector_store_path"])
        self.index = None
        self.documents = []

    def build(self, embeddings: np.ndarray, documents):
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings)
        self.documents = documents

        self.store_path.mkdir(parents=True, exist_ok=True)

        faiss.write_index(self.index, str(self.store_path / "index.faiss"))

        with open(self.store_path / "documents.txt", "w", encoding="utf-8") as f:
            for doc in documents:
                f.write(doc.replace("\n", " ") + "\n")

        logger.info("Vector store built successfully")

    def load(self):
        index_file = self.store_path / "index.faiss"
        docs_file = self.store_path / "documents.txt"

        if not index_file.exists():
            raise FileNotFoundError("Vector index not found")

        self.index = faiss.read_index(str(index_file))

        with open(docs_file, "r", encoding="utf-8") as f:
            self.documents = f.readlines()

    def search(self, query_embedding, k=5):
        distances, indices = self.index.search(query_embedding, k)

        results = []
        for idx in indices[0]:
            if idx < len(self.documents):
                results.append(self.documents[idx])

        return results