from sentence_transformers import SentenceTransformer
from utils.config_loader import load_settings
from utils.logger import get_logger

logger = get_logger()
settings = load_settings()

class EmbeddingModel:

    def __init__(self):
        model_name = settings["rag"]["embedding_model"]
        self.model = SentenceTransformer(model_name)

    def encode(self, texts):
        try:
            return self.model.encode(texts, convert_to_numpy=True)
        except Exception as e:
            logger.exception("Embedding generation failed")
            raise e