# Changelog

All notable changes to ATLAS-OSINT will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0-alpha] - 2026-11-21

### Added
- Complete repository structure for a professional modular OSINT skill
- Main `SKILL.md` with mandatory evidence-first and privacy rules
- All 15 intelligence modules with dedicated SKILL.md files
- JSON Schemas: Evidence, Entity, Relationship, Timeline
- Python package skeleton (`atlas_osint`)
  - Evidence model (Pydantic)
  - Confidence / Admiralty helpers
  - Hallucination control helpers
  - Passive DNS collector
  - Certificate Transparency (crt.sh) collector
  - Reporting section templates
- Documentation: README, INSTALLATION, PRIVACY, SECURITY, CONTRIBUTING
- Knowledge base stubs (Admiralty Code, ACH)
- Adapters guidance
- Example configuration
- Basic pytest for Evidence model
- Apache 2.0 License

### Privacy Boundaries (Enforced)
- Full public research allowed for companies and organizations
- Individuals limited to professional and voluntarily published public information
- Residential addresses, personal phones, and private-life dossier building are out of scope
