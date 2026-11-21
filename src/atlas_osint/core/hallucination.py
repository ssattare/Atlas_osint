"""Hallucination control helpers and rules."""

FORBIDDEN_PHRASES = [
    "I accessed the private",
    "I logged into",
    "according to an unnamed source inside",
    "I found their home address",
    "personal phone number is",
]

def contains_forbidden_claim(text: str) -> bool:
    text_lower = text.lower()
    for phrase in FORBIDDEN_PHRASES:
        if phrase.lower() in text_lower:
            return True
    return False

INSUFFICIENT_EVIDENCE_STATEMENT = "Insufficient evidence to establish this conclusion."
