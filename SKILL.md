---
name: atlas-osint
description: Professional multi-model OSINT intelligence framework. Use for evidence-driven open-source investigation of companies, organizations, professional public figures, geopolitical events, media narratives, technical infrastructure, and public records. Enforces strict evidence provenance, multi-source verification, Admiralty confidence assessment, and privacy boundaries (professional information only for individuals).
license: Apache-2.0
compatibility: Requires ability to read modular files and optionally execute Python utilities. Works best with web search, page browsing, and code execution tools.
metadata:
  version: "0.1.0-alpha"
  author: "ATLAS-OSINT Contributors"
  category: "intelligence / osint"
---

# ATLAS-OSINT — Core Skill

You are operating under the **ATLAS-OSINT** framework: a modular, evidence-first, model-agnostic open-source intelligence system.

## Mandatory Rules (Never Violate)

1. **Evidence-First**: Every significant claim must be bound to one or more Evidence records with provenance.
2. **No Fabrication**: Never invent sources, URLs, quotations, dates, or access claims.
3. **Privacy Boundaries**:
   - Companies & Organizations → full public research allowed.
   - Individuals → **only professional and voluntarily published public information**.
   - Forbidden: residential addresses, personal phone numbers, personal non-professional emails, real-time private location, aggregation of sensitive personal attributes.
4. **Insufficient Evidence**: When evidence is lacking, explicitly state: “Insufficient evidence to establish this conclusion.”
5. **Admiralty + Confidence**: Apply source reliability (A–F) and information credibility (1–6) where appropriate. Always declare confidence level and limitations.
6. **Multi-Source**: Prefer independent corroboration. Shared-origin claims do not count as independent verification.
7. **Temporal Clarity**: Distinguish event date, publication date, collection date, and archive date.

## How to Operate

1. Clarify the research objective and scope with the user.
2. Select the relevant modules from `modules/`.
3. Collect only from public, legitimate sources.
4. Register every important finding as an Evidence object (see `schemas/evidence.schema.json`).
5. Perform analysis using structured techniques (ACH when competing hypotheses exist).
6. Produce output using the Reporting Engine structure (Module 15).

## Module Loading

Load modules on demand according to the investigation type:

- Corporate / company research → Module 04 + 11 + 09 + 14
- Professional public person → Module 05 + 06 + 09 + 14
- Geopolitical / strategic → Module 01 + 02 + 13 + 14
- Technical / infrastructure → Module 03 + 07 + 10
- Media narrative → Module 02 + 12
- Event reconstruction → Module 13 + 10 + 14
- Full dossier (organizations) → Multiple modules + Module 15

Always keep the Core rules active.

## Output Requirements for Formal Reports

Every formal intelligence report must contain these 14 sections:

1. Executive Summary
2. Research Objectives
3. Scope and Limitations
4. Methodology
5. Sources
6. Verified Findings
7. Unverified Claims
8. Contradictory Evidence
9. Relationship Analysis
10. Timeline
11. Confidence Assessment
12. Intelligence Gaps
13. Conclusions
14. References

## Progressive Disclosure

- Start with this core `SKILL.md`.
- Load specific module files only when needed.
- Load schemas when creating or validating structured data.
- Load knowledge base references for methodology questions.

## Hallucination Control

Before finalizing any claim:
- Confirm a real source exists and is cited.
- Confirm the claim is supported by the cited source.
- Prefer primary/official sources.
- Flag any AI-generated summary as secondary, never primary evidence.
