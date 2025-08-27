from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from agents.knowledge_agent import KnowledgeAgent

class DiagnosisAgent:
    def __init__(self):
        self.kb_agent = KnowledgeAgent()
        # LangChain model for reasoning
        self.llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    def diagnose(self, log_line):
        # Check KB first
        for error in self.kb_agent.kb.keys():
            if error in log_line:
                return error

        # Use LLM to reason about unknown errors
        prompt = ChatPromptTemplate.from_template(
            "A log line reports this issue: '{log_line}'. "
            "Suggest a probable cause and safe fix as a mock action."
        )
        response = self.llm.generate([prompt.format_messages(log_line=log_line)])
        suggested_issue = response.generations[0][0].text.strip()
        return suggested_issue
