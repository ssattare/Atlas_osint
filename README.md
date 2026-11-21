# ATLAS-OSINT

**Universal Multi-Model Intelligence & Open-Source Investigation Framework**

[![Version](https://img.shields.io/badge/version-0.1.0--alpha-blue.svg)](VERSION)
[![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)

> A professional, modular, model-agnostic OSINT skill ecosystem designed for evidence-driven intelligence research across multiple AI platforms.

---

## Vision

ATLAS-OSINT is not a simple prompt collection.  
It is a structured, extensible, evidence-first intelligence research framework that can operate across ChatGPT, Claude, Gemini, Kimi, and open-source LLMs.

### Core Principles

1. Model Agnostic Architecture
2. Modular Intelligence Design
3. Evidence-First Analysis
4. Multi-Source Verification
5. Source Provenance Tracking
6. Reproducible Research
7. Transparent Confidence Assessment (Admiralty Code + custom levels)
8. Temporal Intelligence
9. Structured Data Management
10. Secure & Privacy-Aware Tool Integration
11. Version-Controlled Development
12. Cross-Platform Compatibility

### Privacy & Scope Boundaries (Strict)

- **Companies & Organizations**: Full public-domain research (ownership, structure, filings, contracts, official addresses, organizational contacts, etc.).
- **Individuals**: Only **professional and voluntarily published public information** (career history, official roles, public interviews, professional social profiles, published statements, articles, etc.).
- **Explicitly excluded**: Residential addresses, personal telephone numbers, personal non-professional emails, real-time private location tracking, and aggregation of sensitive personal attributes for private individuals.

---

## Architecture Overview

```
ATLAS-OSINT/
├── SKILL.md                     # Main entry skill
├── modules/                     # 15 specialized intelligence modules
├── schemas/                     # JSON schemas (Evidence, Entity, Relationship, Timeline)
├── src/atlas_osint/              # Python utilities & core engine
│   ├── core/                    # Orchestrator, ACH, confidence, hallucination control
│   ├── collectors/              # Passive public-source collectors
│   ├── reporting/               # Report generation
│   └── utils/
├── adapters/                    # Model-specific adapters
├── knowledge/                   # Methodologies & reference materials
├── docs/                        # Full documentation
├── tests/                       # Functional, hallucination, citation tests
├── config/                      # Configuration templates
└── scripts/                     # Installation & helper scripts
```

### 15 Intelligence Modules

| ID | Module                              | Focus                                      |
|----|-------------------------------------|--------------------------------------------|
| 01 | Strategic & Geopolitical            | Events, actors, policy, conflict           |
| 02 | Media & Information                 | Narrative, framing, ownership, influence   |
| 03 | Technical & Cyber                   | DNS, CT logs, public infrastructure, CVEs  |
| 04 | Corporate                           | Ownership, structure, filings, partnerships|
| 05 | Public Person (Professional only)   | Career, public statements, official roles  |
| 06 | Social Media                        | Public accounts & content analysis         |
| 07 | Geospatial                          | Public infrastructure & event locations    |
| 08 | Image & Video Verification          | Provenance, metadata, manipulation indicators |
| 09 | Network & Relationship              | Evidence-based entity graphs               |
| 10 | Historical & Archival               | Wayback, version comparison, timelines     |
| 11 | Financial & Business                | Public statements, filings, procurement    |
| 12 | Disinformation & Propaganda         | Techniques, coordinated messaging          |
| 13 | Event Reconstruction                | Chronology, multi-source comparison        |
| 14 | Source Verification Engine          | Admiralty Code, provenance, contradiction  |
| 15 | Intelligence Reporting              | Structured professional reports            |

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/atlas-osint.git
cd atlas-osint
```

### 2. Python environment (recommended)

```bash
python -m venv .venv
source .venv/bin/activate          # Linux / macOS
# .venv\Scripts\activate           # Windows

pip install -r requirements.txt
```

### 3. Use as AI Skill

Depending on your platform:

- **Claude / Claude Code**: Place or symlink into `~/.claude/skills/atlas-osint/` or project `.claude/skills/`
- **OpenAI Codex / Cursor / compatible agents**: Place into `.agents/skills/atlas-osint/` or `~/.agents/skills/`
- **Manual**: Load the main `SKILL.md` and relevant module files into context.

Detailed adapter instructions are in `adapters/`.

---

## Quick Start (AI Usage)

1. Load the main `SKILL.md`.
2. Specify the research objective and target (company / organization / professional public figure / event).
3. The orchestrator selects relevant modules.
4. All findings are bound to Evidence records with provenance and confidence.
5. Final output is a structured intelligence report following the 14 mandatory sections.

---

## Evidence & Confidence

Every important claim must be linked to an `evidence_id` with:

- Source name & URL
- Publication / event / collection dates
- Verification status (`VERIFIED`, `PARTIALLY_VERIFIED`, `UNVERIFIED`, `DISPUTED`, `CONTRADICTED`)
- Admiralty Code (e.g. `B2`)
- Confidence level and explicit limitations

When evidence is insufficient the system **must** state:

> “Insufficient evidence to establish this conclusion.”

---

## Development Status

**Current version**: `0.1.0-alpha`  
This is the initial structured release focused on architecture, schemas, module specifications, and core Python scaffolding.

Roadmap:
- [x] Phase 1 – Architecture
- [x] Phase 2 – Detailed Specification
- [ ] Phase 3 – Full Implementation (in progress)
- [ ] Phase 4 – Testing & Evaluation
- [ ] Phase 5 – Stable Release

---

## Contributing

Contributions that respect the privacy boundaries and evidence-first principles are welcome.  
Please open an issue first for major changes.

---

## License

Licensed under the **Apache License 2.0**. See [LICENSE](LICENSE).

---

## Disclaimer

ATLAS-OSINT is designed for legitimate open-source intelligence research on public-interest subjects, organizations, and professional public activities.  
Users are solely responsible for complying with all applicable laws and platform terms of service in their jurisdiction.
