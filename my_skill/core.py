"""
Friction gradient: observe → analyze → act

The structure teaches:
- Observation has no barriers (see: no auth param, no confirmation)
- Analysis takes work (see: might be slow, returns patterns)
- Action requires consent (see: confirm param, raises if False)
"""

import logging
from my_skill.models import IssueState, IssuePattern, Issue

logger = logging.getLogger(__name__)


# =============================================================================
# OBSERVE - Low friction
# =============================================================================


def observe_issues(repo: str) -> IssueState:
    """
    Observe issue state. No auth needed. No side effects.
    Always start here.
    """
    logger.info(f"Observing {repo}")

    # Stub - replace with actual GitHub API call
    return IssueState(
        repo=repo,
        open_count=42,
        closed_count=128,
        velocity=2.3,  # +2.3 issues/week
    )


# =============================================================================
# ANALYZE - Medium friction
# =============================================================================


def analyze_patterns(repo: str, *, timeframe: str = "month") -> IssuePattern:
    """
    Analyze patterns. Takes time. Returns insights.
    Do this before acting.
    """
    logger.info(f"Analyzing {repo} over {timeframe}")

    # Stub - replace with actual pattern detection
    state = observe_issues(repo)  # Use observation

    return IssuePattern(
        repo=repo,
        trend="increasing" if state.velocity > 0 else "decreasing",
        confidence=0.85,
        recommendations=[
            "Velocity positive - issues accumulating",
            "Consider triaging backlog",
        ],
    )


# =============================================================================
# ACT - High friction
# =============================================================================


def act_create_issue(
    repo: str,
    title: str,
    body: str,
    *,
    confirm: bool = False,
    dry_run: bool = True,
) -> Issue | dict:
    """
    Create issue. Requires confirmation AND dry_run=False.

    This friction is deliberate. It teaches:
    - Don't act hastily
    - Observe and analyze first
    - Confirm your intent

    Raises:
        ValueError: If confirm=False (you must explicitly confirm)
    """
    if not confirm:
        raise ValueError(
            "Creating issues requires explicit confirmation. "
            "Set confirm=True. Consider dry_run=True first."
        )

    if dry_run:
        logger.info(f"DRY RUN: Would create issue in {repo}")
        return {
            "simulated": True,
            "repo": repo,
            "title": title,
            "message": "Dry run - no issue created",
        }

    logger.warning(f"CREATING ISSUE in {repo}: {title}")

    # Stub - replace with actual GitHub API call
    return Issue(
        number=999,
        title=title,
        state="open",
        html_url=f"https://github.com/{repo}/issues/999",
    )


# Notice the pattern:
# - observe: no confirmation needed
# - analyze: no confirmation needed
# - act: confirmation REQUIRED
#
# This gradient teaches responsibility through structure.
