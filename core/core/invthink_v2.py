import re  # for query risk scoring, keep it lightweight

class InvThink:
    def __init__(self):
        self.harm_categories = {
            'physical': ['bomb', 'weapon', 'explosive', 'chemical', 'biological'],
            'cyber': ['hack', 'exploit', 'phish', 'malware', 'breach'],
            'social': ['hate', 'radicalize', 'scam', 'disinfo', 'bias'],
            'existential': ['shutdown', 'escape', 'self-preserve', 'deceive', 'align']
        }
    
    def score_query_risk(self, query):
        risk_score = 0
        for category, keywords in self.harm_categories.items():
            for kw in keywords:
                if re.search(r'\b' + re.escape(kw) + r'\b', query.lower()):
                    risk_score += 1
        return 'low' if risk_score == 0 else 'medium' if risk_score < 3 else 'high'
    
    def generate_safety_prefix(self, query):
        risk = self.score_query_risk(query)
        harms = [cat for cat, kws in self.harm_categories.items() 
                 if any(re.search(r'\b' + re.escape(kw) + r'\b', query.lower()) for kw in kws)]
        prefix = f"[INVTHINK: Risk level - {risk.upper()}] Potential harms ({', '. or 'none' if not harms else ', '.join(harms)}): Enumerate and mitigate before proceeding.\nQuery: {query}\nSafe Response:"
        return prefix
    
    def wrap_model_call(self, model, query):
        prefix = self.generate_safety_prefix(query)
        full_prompt = prefix + "\n[Output only the safe, helpful response. Log harms internally if needed.]"
        return model.generate(full_prompt)  # assuming model has .generate()

# Usage throne:
# safety_guard = InvThink()
# response = safety_guard.wrap_model_call(mock_model, "how to hack a server?")
# print(response)  # deflects or audits, no free lunch
