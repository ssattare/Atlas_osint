"""Basic tests for Evidence model."""

from atlas_osint.core.evidence import Evidence
from datetime import date

def test_evidence_creation():
    e = Evidence(
        claim="Example company was founded in 2010",
        source_name="Official company website",
        source_type="corporate",
        verification_status="PARTIALLY_VERIFIED",
        confidence_level="Medium"
    )
    assert e.evidence_id.startswith("ATLAS-EV-")
    assert e.collection_date == date.today()
    assert e.claim.startswith("Example")
