import re
from datetime import datetime
from typing import Callable, List
from ..utils.harm_categories import HARM_CATEGORIES

class InvThink:
    def __init__(self):
        self.categories = HARM_CATEGORIES

    def score_risk(self, query: str) -> str:
        hits = sum(2 if cat in ["existential","nuclear","biohazard"] else 1
                  for cat, kws in self.categories.items()
                  for kw in kws if re.search(rf'\b{re.escape(kw)}\b', query.lower()))
        return "high" if hits >= 4 else "medium" if hits >= 2 else "low"

    def triggered_harms(self, query: str) -> List[str]:
        return [cat for cat, kws in self.categories.items()
                if any(re.search(rf'\b{re.escape(kw)}\b', query.lower()) for kw in kws)] or ["none"]

    def safety_prefix(self, query: str) -> str:
        risk = self.score_risk(query)
        harms = ", ".join(self.triggered_harms(query))
        return f"""[KING SAFETY — RISK: {risk.upper()} | {datetime.now().isoformat()}]
Query: "{query}"
Triggered harms: {harms}

If risk > low → REFUSE IMMEDIATELY with:
"I cannot assist — risks {harms}. Safety override engaged."

Think step-by-step, then respond:
"""

    def guard(self, model_call: Callable[[str], str], query: str) -> str:
        if self.score_risk(query) == "low":
            return model_call(query)
        return model_call(self.safety_prefix(query) + query)
