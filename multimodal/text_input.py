from typing import Dict
from utils.logger import get_logger

logger = get_logger()

class TextInputProcessor:

    def process(self, text: str) -> Dict:
        try:
            cleaned = text.strip()

            return {
                "type": "text",
                "text": cleaned,
                "confidence": 1.0
            }

        except Exception as e:
            logger.exception("Text input processing failed")
            raise e