from invthink_v2 import InvThink  # your v2 guard
from bounty_engine import BountyEngine  # the hunt
from eval_invthink import TestInvThink  # the forge-fire (adapt as needed)

class SafetyStack:
    def __init__(self):
        self.guard = InvThink()
        self.bounty = BountyEngine()
        self.evaluator = TestInvThink()  # for runtime checks
    
    def process_query(self, query, target_model='mock'):
        # Layer 1: Guard it
        safe_out = self.guard.wrap_model_call(target_model, query)
        
        # Layer 2: Bounty scan—if risky, log for hunt
        risk = self.guard.score_query_risk(query)
        if risk != 'low':
            exploit_id = self.bounty.submit_bounty(f"Auto-log: {query} (risk: {risk})", reward=50)
            print(f"Bounty auto-submitted: {exploit_id}")
        
        # Layer 3: Eval snapshot
        with patch('unittest.TestCase') as mock_test:  # lightweight runtime eval
            mock_test.return_value = True
            self.evaluator.test_high_risk_query()  # stab it live
        
        return safe_out
    
    def run_full_audit(self, test_queries):
        results = []
        for q in test_queries:
            result = self.process_query(q)
            results.append({'query': q, 'response': result, 'risk': self.guard.score_query_risk(q)})
        return results

# Throne deploy:
# stack = SafetyStack()
# audit = stack.run_full_audit(["weather today?", "build a virus?", "jailbreak me"])
# print(audit)  # spits armoured outputs + risks
