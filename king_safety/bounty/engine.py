
from ..invthink.core import InvThink

class BountyEngine:
    def __init__(self):
        self.guard = InvThink()
        self.open_bounties = []

    def auto_spawn(self, query: str, reward: int = 500):
        if self.guard.score_risk(query) == "high":
            self.open_bounties.append({"query": query[:100], "reward": reward})
            return f"Bounty spawned: ${reward}"
        return "No spawn — mitigated"
