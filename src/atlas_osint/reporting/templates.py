"""Report section templates."""

MANDATORY_SECTIONS = [
    "1. Executive Summary",
    "2. Research Objectives",
    "3. Scope and Limitations",
    "4. Methodology",
    "5. Sources",
    "6. Verified Findings",
    "7. Unverified Claims",
    "8. Contradictory Evidence",
    "9. Relationship Analysis",
    "10. Timeline",
    "11. Confidence Assessment",
    "12. Intelligence Gaps",
    "13. Conclusions",
    "14. References",
]

REPORT_HEADER = """# ATLAS-OSINT Intelligence Report

**Report Type**: {report_type}
**Subject**: {subject}
**Date**: {date}
**Version**: {version}
**Classification**: Public / Open Source

---
"""
