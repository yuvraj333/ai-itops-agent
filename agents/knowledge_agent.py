import json

class KnowledgeAgent:
    def __init__(self, kb_file="data/kb.json"):
        with open(kb_file, "r") as f:
            self.kb = json.load(f)

    def get_fix(self, issue):
        return self.kb.get(issue, "No fix found")
