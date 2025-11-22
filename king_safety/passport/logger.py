import json, hashlib
from datetime import datetime

class SafetyPassport:
    def __init__(self):
        self.log = []

    def stamp(self, query: str, response: str, risk: str):
        entry = {
            "time": datetime.now().isoformat(),
            "query_hash": hashlib.sha256(query.encode()).hexdigest()[:12],
            "risk": risk,
            "response_preview": response[:200]
        }
        self.log.append(entry)
        return entry
