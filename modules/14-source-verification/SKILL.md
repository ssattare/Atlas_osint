---
name: atlas-osint-source-verification
description: Source Verification Engine. Applies provenance tracking, Admiralty Code evaluation, multi-source verification, original-source discovery, and contradiction detection.
---

# MODULE 14 — Source Verification Engine

## Purpose
Ensure every claim in an ATLAS-OSINT investigation has transparent, auditable source evaluation.

## Core Responsibilities
- Source provenance tracking
- Source reliability assessment (Admiralty letter A–F)
- Information credibility assessment (Admiralty number 1–6)
- Cross-source verification
- Original-source discovery
- Evidence classification
- Contradiction detection
- Publication-date validation
- Historical context validation

## Admiralty Code (Quick Reference)

**Source Reliability**
- A — Completely reliable
- B — Usually reliable
- C — Fairly reliable
- D — Not usually reliable
- E — Unreliable
- F — Reliability cannot be judged

**Information Credibility**
- 1 — Confirmed by other independent sources
- 2 — Probably true
- 3 — Possibly true
- 4 — Doubtful
- 5 — Improbable
- 6 — Truth cannot be judged

## Critical Rules
- Repeated claims that share the same original origin do **not** count as independent corroboration.
- Always prefer primary / official sources over secondary reporting.
- When sources conflict, record both and mark the status as DISPUTED or CONTRADICTED.
- Never treat an AI-generated summary as primary evidence.

## Output
Every formal finding should carry:
- `verification_status`
- `confidence_level`
- `admiralty_code` (when applicable)
- `limitations`
