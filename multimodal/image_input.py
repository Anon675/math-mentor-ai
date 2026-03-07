from PIL import Image
from typing import Dict
from multimodal.ocr_engine import OCREngine
from utils.logger import get_logger

logger = get_logger()

class ImageInputProcessor:

    def __init__(self):
        self.ocr = OCREngine()

    def process(self, image_path: str) -> Dict:
        try:
            image = Image.open(image_path).convert("RGB")

            extracted_text, confidence, raw = self.ocr.extract_text(image)

            return {
                "type": "image",
                "extracted_text": extracted_text,
                "confidence": confidence,
                "raw_ocr": raw,
            }

        except Exception as e:
            logger.exception("Image input processing failed")
            raise e