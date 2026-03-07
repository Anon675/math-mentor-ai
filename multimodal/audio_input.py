from typing import Dict
from multimodal.speech_to_text import SpeechToTextEngine
from utils.logger import get_logger

logger = get_logger()

class AudioInputProcessor:

    def __init__(self):
        self.stt = SpeechToTextEngine()

    def process(self, audio_path: str) -> Dict:
        try:
            transcript = self.stt.transcribe(audio_path)

            return {
                "type": "audio",
                "transcript": transcript,
                "confidence": 1.0
            }

        except Exception as e:
            logger.exception("Audio input processing failed")
            raise e