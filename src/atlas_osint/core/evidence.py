"""
Evidence management utilities for ATLAS-OSINT.
"""

from __future__ import annotations

import uuid
from datetime import date
from typing import Any, Optional

from pydantic import BaseModel, Field, HttpUrl


class Evidence(BaseModel):
    evidence_id: str = Field(default_factory=lambda: f"ATLAS-EV-{date.today().isoformat()}-{uuid.uuid4().hex[:6].upper()}")
    claim: str
    source_name: str
    source_url: Optional[HttpUrl] = None
    source_type: str = "other"
    original_source: Optional[str] = None
    publication_date: Optional[date] = None
    event_date: Optional[date] = None
    collection_date: date = Field(default_factory=date.today)
    supporting_evidence: list[str] = Field(default_factory=list)
    contradictory_evidence: list[str] = Field(default_factory=list)
    verification_status: str = "UNVERIFIED"
    confidence_level: str = "Low"
    admiralty_code: Optional[str] = None
    limitations: list[str] = Field(default_factory=list)
    module_origin: Optional[str] = None

    def to_dict(self) -> dict[str, Any]:
        return self.model_dump(mode="json")
