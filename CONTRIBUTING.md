# Contributing to ATLAS-OSINT

Thank you for your interest in contributing.

## Principles

1. Evidence-first design
2. Respect the privacy boundaries defined in `docs/PRIVACY.md`
3. Keep modules modular and independently understandable
4. Prefer clear documentation over clever code
5. Add tests for new functionality

## Development Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

## Pull Requests

- Describe the change clearly
- Reference any related issue
- Ensure privacy rules are not violated
