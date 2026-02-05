"""
Models with extra="allow" - the API evolves, we accept it.
"""

from pydantic import BaseModel, ConfigDict


class IssueState(BaseModel):
    """What we observe - current state, no side effects."""

    model_config = ConfigDict(extra="allow")  # Wu wei

    repo: str
    open_count: int
    closed_count: int
    velocity: float  # Issues per week (+ = growing, - = shrinking)


class IssuePattern(BaseModel):
    """What we analyze - patterns over time."""

    model_config = ConfigDict(extra="allow")  # API might add fields

    repo: str
    trend: str  # "increasing" | "decreasing" | "stable"
    confidence: float
    recommendations: list[str] = []


class Issue(BaseModel):
    """An actual issue (created by act_create_issue)."""

    model_config = ConfigDict(extra="allow")  # GitHub API has many fields

    number: int
    title: str
    state: str
    html_url: str
