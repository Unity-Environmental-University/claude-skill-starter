"""
Skill that shows philosophy through structure.
Read the code. The order teaches.
"""

from my_skill.core import observe_issues, analyze_patterns, act_create_issue

__version__ = "0.1.0"

# Export order = priority order
# Observation first, action last
__all__ = [
    "observe_issues",      # Low friction
    "analyze_patterns",    # Medium friction
    "act_create_issue",    # High friction
]
