# Model Adapters

This directory contains guidance for loading ATLAS-OSINT on different AI platforms.

## Supported Platforms (Planned / Documented)

- Claude / Claude Code
- OpenAI Codex / ChatGPT (via skills or manual)
- Cursor
- Gemini CLI
- Open-source local models (via system prompt + file loading)

## Common Pattern

1. Place the repository (or symlink) in the platform’s skills directory.
2. Ensure the main `SKILL.md` is discoverable.
3. Load specific modules on demand for progressive disclosure.
4. Respect context window limits by loading only needed modules.

## Notes

Native compatibility should only be claimed after testing on each platform.
