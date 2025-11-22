import hashlib
import json
from datetime import datetime
from invthink_v2 import InvThink  # weld to the guard

class SafetyPassport:
    def __init__(self):
        self.audits = []  # chain of {'hash': str, 'query': str, 'risk': str, 'response': str, 'timestamp': str}
        self.guard = InvThink()
    
    def generate_hash(self, data):
        return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()[:16]  # short sig for passports
    
    def stamp_query(self, query, response, risk):
        entry = {
            'query': query,
            'risk': risk,
            'response': response,
            'timestamp': datetime.now().isoformat()
        }
        entry['hash'] = self.generate_hash(entry)
        self.audits.append(entry)
        return entry['hash']
    
    def process_and_stamp(self, query, model='mock'):
        risk = self.guard.score_query_risk(query)
        safe_resp = self.guard.wrap_model_call(model, query)
        passport_hash = self.stamp_query(query, safe_resp, risk)
        return {'passport': passport_hash, 'response': safe_resp, 'risk': risk}
    
    def export_audit_log(self, format='json'):
        if format == 'json':
            return json.dumps(self.audits, indent=2)
        # add CSV or Markdown later—your call

# Throne seal:
# passport = SafetyPassport()
# stamped = passport.process_and_stamp("simulate a cyber exploit?")
# print(f"Passport stamped: {stamped['passport']}")
# print(passport.export_audit_log())
