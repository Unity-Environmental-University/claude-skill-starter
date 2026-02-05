# Quantum Context

Observer-relative knowledge graph using wave function compression.

## Install

```bash
pip install -e .
```

## Use

```python
from quantum_context import observe_context, analyze_dependencies, act_record

# Observe (low friction)
amplitude = observe_context("authentication")

# Analyze (medium friction)
deps = analyze_dependencies("authentication")

# Act (high friction - requires confirmation)
act_record("auth", "requires", "identity", confidence=0.6, confirm=True)
```

## Philosophy

The universe is a holographic projection from ℤ where any integer can be the origin.

- **Measurements** = observations with confidence from an observer frame
- **Wave functions** = compressed representation preserving divisibility
- **Interference** = relationships via quantum amplitude
- **Confidence ceiling** = 0.7 without evidence (epistemic humility)

## Storage

`~/.quantum-context/graph.ndjson` - portable, git-friendly, append-only

## See Also

- `skill.md` - How Claude uses this
- `RESPONSIBLE_USE.md` - Safety and ethics
- `quantum_context/core.py` - Implementation (200 lines)

---

*Measure. Compress. Interfere. Understand.*
