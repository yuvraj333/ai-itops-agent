# ai-itops-agent
AI ITOps Agent Demo
Author: Yuvraj Kumar MahatoGitHub: https://github.com/yuvraj333/ai-itops-agentContact: yuvrajkumarmahato@gmail.com  

Project Overview
This project demonstrates a demo AI Agent for IT Ticket Resolution, designed to simulate autonomous ITOps workflows. The system:

Monitors logs or alerts.
Diagnoses common infrastructure or service issues.
Suggests or executes mock fixes (e.g., restart service, clear cache).

It uses LangChain agents, OpenAI GPT-3.5, and Python for a fully functional demo.

Features

Supervisor Agent: Monitors logs and coordinates actions.
Diagnosis Agent: Detects known errors via knowledge base and generates solutions using LLM reasoning.
Knowledge Agent: Stores predefined error patterns and suggestions.
Mock execution: Simulates automated actions like service restart or cache clearing.
Demo-ready: Fully working code to showcase AI-driven ITOps automation.


Architecture
main.py
└─ SupervisorAgent
   ├─ monitors logs
   ├─ calls DiagnosisAgent
   └─ executes suggested actions
└─ DiagnosisAgent
   ├─ checks KnowledgeAgent KB
   ├─ uses OpenAI LLM for unknown issues
   └─ returns suggested fixes


Technologies used: Python, LangChain, OpenAI, dotenv.  
Optional storage: PostgreSQL (mocked actions for demo).  
Virtual environment: Isolated Python venv.


Installation

Clone the repo:

git clone https://github.com/yuvraj333/ai-itops-agent.git
cd ai-itops-agent


Create and activate a virtual environment:

python3 -m venv --copies venv
source venv/bin/activate


Install dependencies:

pip install --upgrade pip
pip install -r requirements.txt


Set OpenAI API key:

Create a .env file in the root folder:
OPENAI_API_KEY=your_api_key_here

Or set it directly in your terminal:
export OPENAI_API_KEY="your_api_key_here"


Usage
Run the main script:
python main.py

Example output:
⏱ Monitoring logs...
Issue: Database connection failed | Suggested Action: Restart PostgreSQL service
Executing: Restart PostgreSQL service ✅
Issue: High memory usage detected | Suggested Action: Clear cache and optimize processes
Executing: Clear cache and optimize processes ✅
Monitoring complete.


Project Structure
ai-itops-agent/
├─ agents/
│  ├─ supervisor_agent.py   # Supervises log monitoring and orchestrates actions
│  ├─ diagnosis_agent.py    # Diagnoses issues using KB and LLM
│  └─ knowledge_agent.py    # Stores predefined error patterns
├─ main.py                  # Entry point
├─ requirements.txt         # Python dependencies
├─ .env                     # OpenAI API key
└─ README.md


How It Works

SupervisorAgent monitors logs (mocked log file in demo).
For each log line, it calls DiagnosisAgent.
DiagnosisAgent:
Checks predefined KnowledgeAgent KB for known errors.
Uses OpenAI GPT-3.5 via LangChain to suggest fixes for unknown issues.


Suggested actions are executed (mocked) and printed to console.


Dependencies

Python 3.12+
LangChain (langchain, langchain-community)
OpenAI Python SDK
python-dotenv


Notes

This is a demo project for showcasing AI-driven ITOps automation.
LLM-based reasoning generates mock suggestions, not real system changes.
For production, integrate with actual services, APIs, and monitoring systems.


Author
Yuvraj Kumar Mahato – AI & ML Research Enthusiast📍 Kathmandu, Nepal📧 yuvrajkumarmahato@gmail.comGitHub | LinkedIn