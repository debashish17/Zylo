"""
NLP-powered compliance detection using transformers
Will be implemented with BERT fine-tuning in Phase 2
"""

import re
from typing import List, Dict, Tuple

class ComplianceNLP:
    """
    Text compliance checker
    Phase 1: Rule-based (regex patterns)
    Phase 2: Fine-tuned BERT model
    """

    # Prohibited patterns (Phase 1 implementation)
    PROHIBITED_PATTERNS = {
        "terms_conditions": [
            r"\*",
            r"T&Cs?",
            r"terms\s+and\s+conditions",
            r"see\s+website",
            r"subject\s+to\s+availability",
        ],
        "competition": [
            r"enter\s+to\s+win",
            r"competition",
            r"prize\s+draw",
            r"win\s+\w+",
            r"giveaway",
        ],
        "sustainability_claim": [
            r"eco-?friendly",
            r"sustainable",
            r"green",
            r"carbon\s+neutral",
            r"environmentally\s+friendly",
        ],
        "money_back_guarantee": [
            r"money-?back\s+guarantee",
            r"100%\s+refund",
            r"satisfaction\s+guaranteed",
        ],
        "health_claim": [
            r"cures?",
            r"treats?",
            r"prevents?",
            r"reduces?\s+risk",
        ],
        "price_mention": [
            r"£\d+",
            r"\d+%\s+off",
            r"save\s+£\d+",
            r"discount",
        ],
    }

    def __init__(self):
        self.model_loaded = False
        # Will load BERT model in Phase 2

    def detect_violations(self, text: str, threshold: float = 0.7) -> List[Dict]:
        """
        Detect compliance violations in text

        Args:
            text: Text to analyze
            threshold: Confidence threshold (not used in regex mode)

        Returns:
            List of violations with type, confidence, and suggestions
        """
        violations = []

        for violation_type, patterns in self.PROHIBITED_PATTERNS.items():
            for pattern in patterns:
                if re.search(pattern, text, re.IGNORECASE):
                    violations.append({
                        "type": violation_type,
                        "confidence": 1.0,  # Regex matches are 100% confident
                        "severity": "critical",
                        "matched_text": re.search(pattern, text, re.IGNORECASE).group(),
                        "suggestion": self._get_suggestion(violation_type)
                    })

        return violations

    def _get_suggestion(self, violation_type: str) -> str:
        """Get fix suggestion for violation type"""
        suggestions = {
            "terms_conditions": "Remove asterisks and T&C references. State benefits directly.",
            "competition": "Remove competition language. Focus on product benefits.",
            "sustainability_claim": "Remove environmental claims unless certified.",
            "money_back_guarantee": "Remove guarantee language. Emphasize quality instead.",
            "health_claim": "Remove health claims unless approved by regulatory body.",
            "price_mention": "Move price information to value tiles only.",
        }
        return suggestions.get(violation_type, "Please review this text for compliance.")

# Singleton instance
compliance_nlp = ComplianceNLP()
