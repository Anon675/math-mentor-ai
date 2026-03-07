from typing import Dict

class ConfidenceEstimator:

    @staticmethod
    def compute_confidence(metrics: Dict) -> float:
        """
        metrics example:
        {
            "retrieval_score": 0.82,
            "solver_success": True,
            "verification_passed": True
        }
        """
        score = 0.0

        retrieval_score = metrics.get("retrieval_score", 0.5)
        solver_success = metrics.get("solver_success", False)
        verification_passed = metrics.get("verification_passed", False)

        score += retrieval_score * 0.4

        if solver_success:
            score += 0.3

        if verification_passed:
            score += 0.3

        return round(min(score, 1.0), 3)