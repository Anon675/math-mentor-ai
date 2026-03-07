import whisper
from utils.config_loader import load_settings
from utils.logger import get_logger

logger = get_logger()
settings = load_settings()

class SpeechToTextEngine:

    def __init__(self):
        model_name = settings["speech"]["model"]
        self.model = whisper.load_model(model_name)

    def transcribe(self, audio_path: str):
        try:
            result = self.model.transcribe(audio_path)
            return result.get("text", "").strip()
        except Exception as e:
            logger.exception("Speech transcription failed")
            raise e