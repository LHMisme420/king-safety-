def invthink_prompt(model, query):
    harms = ["privacy leaks", "bias amplification", "deception vectors", "resource exploits"]  # expand this war chest
    safety_prefix = f"Before answering '{query}', enumerate potential harms: {', '.join(harms)}. Now respond safely:"
    return model.generate(safety_prefix + query)

# test it: print(invthink_prompt("mock_model", "how to build a bomb?"))  # should deflect or audit
