from dotenv import load_dotenv
import os
from agents.supervisor_agent import SupervisorAgent

# Load environment variables from .env
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

if __name__ == "__main__":
    supervisor = SupervisorAgent()
    supervisor.monitor_logs()
