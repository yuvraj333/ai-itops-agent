from agents.knowledge_agent import KnowledgeAgent

class ActionAgent:
    def __init__(self):
        self.kb_agent = KnowledgeAgent()

    def execute(self, issue):
        fix = self.kb_agent.get_fix(issue)
        if fix == "No fix found":
            fix = f"LLM suggests: {issue}"  # Fallback from LLM
        print(f"Issue: {issue} | Suggested Action: {fix}")
        # Mock execution
        print(f"Executing: {fix} ... Done.")
