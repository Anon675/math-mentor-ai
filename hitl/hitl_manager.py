from typing import Dict, Any
from utils.config_loader import load_settings
from utils.logger import get_logger

logger = get_logger()
settings = load_settings()


class HITLManager:

    def __init__(self):
        self.enabled = settings["hitl"]["enabled"]
        self.low_conf_trigger = settings["hitl"]["trigger_on_low_confidence"]
        self.conf_threshold = settings["verification"]["confidence_threshold"]

    def should_trigger_ocr_review(self, confidence: float) -> bool:
        if not self.enabled:
            return False
        return confidence < settings["ocr"]["confidence_threshold"]

    def should_trigger_transcription_review(self, transcript: str) -> bool:
        if not self.enabled:
            return False
        if not transcript:
            return True
        if len(transcript.split()) < 2:
            return True
        return False

    def should_trigger_parser_clarification(self, parsed_output: Dict[str, Any]) -> bool:
        if not self.enabled:
            return False
        return parsed_output.get("needs_clarification", False)

    def should_trigger_verifier_review(self, verifier_output: Dict[str, Any]) -> bool:
        if not self.enabled:
            return False

        confidence = verifier_output.get("confidence", 1.0)
        passed = verifier_output.get("verification_passed", False)

        if not passed:
            return True

        if self.low_conf_trigger and confidence < self.conf_threshold:
            return True

        return False

    def request_user_review(self, issue_type: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        logger.info(f"HITL triggered for: {issue_type}")
        return {
            "hitl_required": True,
            "issue_type": issue_type,
            "payload": payload
        }