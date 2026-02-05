# Claude Skill Starter

Minimal template for making Claude skills. Philosophy is in the structure, not the docs.

## Use It

```bash
cp -r skill-starter your-skill
cd your-skill
# Rename my_skill → your_skill everywhere
pip install -e .
```

## Three Principles (in code, not words)

1. **Observe before act** → See `__init__.py` export order
2. **Types flex** → See `extra="allow"` in models
3. **Friction teaches** → See confirmation in `act_*()`

## Structure

```
your-skill/
├── skill.md           # What Claude sees (example included, just edit)
├── pyproject.toml     # Metadata
└── my_skill/
    ├── __init__.py    # Export order = priority
    ├── models.py      # extra="allow" everywhere
    └── core.py        # observe → analyze → act
```

## Testing (property-based)

```bash
pip install -e ".[dev]"
pytest
```

Tests validate the **paradigm**, not just the code:
- Friction gradient is enforced (observe never requires confirmation, act always does)
- Wu wei is structural (models accept extra fields via `extra="allow"`)
- Export order reflects priority (observe → analyze → act)
- Transparency is default (all operations log)

## The Pattern (shown in code)

Look at the actual files. The structure teaches.

That's it.
