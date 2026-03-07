import easyocr
import numpy as np
from PIL import Image
from typing import Tuple, List
from utils.logger import get_logger
from utils.config_loader import load_settings

logger = get_logger()
settings = load_settings()

class OCREngine:
    def __init__(self):
        langs = settings["ocr"]["languages"]
        self.reader = easyocr.Reader(langs, gpu=False)
        self.conf_threshold = settings["ocr"]["confidence_threshold"]

    def extract_text(self, image: Image.Image) -> Tuple[str, float, List]:
        try:
            img_array = np.array(image)
            results = self.reader.readtext(img_array)

            texts = []
            confidences = []

            for bbox, text, conf in results:
                texts.append(text)
                confidences.append(conf)

            combined_text = " ".join(texts)
            avg_conf = float(np.mean(confidences)) if confidences else 0.0

            return combined_text.strip(), avg_conf, results

        except Exception as e:
            logger.exception("OCR extraction failed")
            raise e