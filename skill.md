# github-issues

Observe, analyze, and act on GitHub issues using cybernetic principles.

## Core Concepts

- **Issue Flow**: Issues move through states (open → triaged → closed)
- **Velocity**: Rate of issue creation vs resolution
- **Friction**: Deliberate barriers prevent hasty actions

## Operations

### observe issues [repo]
Check current issue state without side effects.

**Returns:** Issue counts, velocity metrics, health indicators

**When:** Always start here. Observation is cheap.

### analyze patterns [repo]
Identify trends in issue creation, closure, and staleness.

**Returns:** Pattern analysis, recommendations, warnings

**When:** After observing. Before acting.

### act create-issue [repo] [title] [body]
Create a new issue (requires confirmation).

**Returns:** Created issue details

**When:** Only after observation + analysis. With explicit confirmation.

## Example Interaction

**Human:** "Check what's happening with issues in anthropics/claude-code"

**Claude:**
```python
# 1. Observe first (low friction)
state = observe_issues("anthropics/claude-code")
# → Shows: 42 open, 8 created this week, velocity: +2/week

# 2. Analyze if needed (medium friction)
patterns = analyze_patterns("anthropics/claude-code")
# → Shows: Increasing bug reports, feature requests stable

# 3. Only act if appropriate (high friction)
# User must explicitly request creation
```

## Procedural Rhetoric

Using this skill teaches:
- **Observe before action** - Can't act without seeing first
- **Understanding before intervention** - Analysis precedes action
- **Deliberate participation** - Confirmation required for writes

## Technical

Wraps GitHub API via `httpx`. Observation uses unauthenticated endpoints. Analysis and actions require `GITHUB_TOKEN`.

Python client embodies wu wei through:
- `extra="allow"` in models (API evolves, we accept it)
- Read operations frictionless
- Write operations require confirmation

## Usage Context

Appropriate for:
- Researching issue patterns
- Monitoring project health
- Responsible issue creation
- Educational use

NOT for:
- Mass issue creation
- Automated closing without human oversight
- Circumventing rate limits

---

*Observe the system. Understand the patterns. Act deliberately.*
