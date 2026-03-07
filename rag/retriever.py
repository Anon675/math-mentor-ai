from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore
from utils.config_loader import load_settings
from utils.logger import get_logger

logger = get_logger()
settings = load_settings()

class Retriever:

    def __init__(self):
        self.embedding_model = EmbeddingModel()
        self.vector_store = VectorStore()
        self.top_k = settings["rag"]["top_k"]

        try:
            self.vector_store.load()
        except Exception:
            logger.warning("Vector store not found. Build it before retrieval.")

    def retrieve(self, query: str):
        query_embedding = self.embedding_model.encode([query])
        results = self.vector_store.search(query_embedding, self.top_k)

        return results