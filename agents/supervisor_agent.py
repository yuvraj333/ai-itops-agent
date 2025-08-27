from agents.diagnosis_agent import DiagnosisAgent
from agents.action_agent import ActionAgent

class SupervisorAgent:
    def __init__(self, log_file="logs/system_logs.txt"):
        self.log_file = log_file
        self.diagnosis_agent = DiagnosisAgent()
        self.action_agent = ActionAgent()

    def monitor_logs(self):
        print("⏱ Monitoring logs...")
        with open(self.log_file, "r") as f:
            for line in f:
                if "ERROR" in line or "WARNING" in line:
                    issue = self.diagnosis_agent.diagnose(line)
                    if issue:
                        self.action_agent.execute(issue)
        print("Monitoring complete.")