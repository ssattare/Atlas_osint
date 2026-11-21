# Installation Guide — ATLAS-OSINT

## 1. Clone from GitHub

```bash
git clone https://github.com/YOUR_USERNAME/atlas-osint.git
cd atlas-osint
```

## 2. Create virtual environment

```bash
python3.11 -m venv .venv
source .venv/bin/activate          # Linux / macOS
# .venv\Scripts\activate           # Windows
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Using as an AI Skill

### Claude / Claude Code
Copy or symlink the whole repository into:
- Project: `.claude/skills/atlas-osint/`
- User: `~/.claude/skills/atlas-osint/`

### OpenAI Codex / Cursor / compatible agents
Place into:
- `.agents/skills/atlas-osint/`
- or `~/.agents/skills/atlas-osint/`

### Manual loading
Load `SKILL.md` + the relevant module `SKILL.md` files into the model context.

## 5. Update

```bash
git pull origin main
pip install -r requirements.txt --upgrade
```

## 6. Uninstall

Simply delete the cloned directory and remove any skill symlinks.
