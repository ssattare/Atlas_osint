"""Confidence and Admiralty helpers."""

from typing import Optional

ADMIRALTY_RELIABILITY = {
    "A": "Completely reliable",
    "B": "Usually reliable",
    "C": "Fairly reliable",
    "D": "Not usually reliable",
    "E": "Unreliable",
    "F": "Reliability cannot be judged",
}

ADMIRALTY_CREDIBILITY = {
    "1": "Confirmed by other independent sources",
    "2": "Probably true",
    "3": "Possibly true",
    "4": "Doubtful",
    "5": "Improbable",
    "6": "Truth cannot be judged",
}

def parse_admiralty(code: str) -> dict:
    code = code.strip().upper()
    if len(code) < 2:
        return {"raw": code, "reliability": None, "credibility": None}
    letter = code[0]
    number = code[1]
    return {
        "raw": code,
        "reliability": ADMIRALTY_RELIABILITY.get(letter, "Unknown"),
        "credibility": ADMIRALTY_CREDIBILITY.get(number, "Unknown"),
    }

def recommend_confidence(verification_status: str, admiralty: Optional[str] = None) -> str:
    if verification_status == "VERIFIED":
        return "High"
    if verification_status == "PARTIALLY_VERIFIED":
        return "Medium"
    if verification_status in ("DISPUTED", "CONTRADICTED"):
        return "Low"
    return "Insufficient"
