# AI ITOps Agent Demo

An AI-powered IT Operations agent designed to autonomously monitor, diagnose, and resolve common infrastructure issues through simulated workflows.

![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)
![LangChain](https://img.shields.io/badge/LangChain-0.1.0-green)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-purple)

## 📋 Project Overview

This project demonstrates an AI Agent for IT Ticket Resolution that simulates autonomous ITOps workflows. The system monitors logs or alerts for potential issues, diagnoses common infrastructure or service problems, suggests or executes mock fixes (e.g., restart service, clear cache), and uses LangChain agents and OpenAI GPT-3.5 for intelligent reasoning. It is built with Python for a fully functional demo, showcasing AI-driven ITOps automation.

## ✨ Features

- **Supervisor Agent**: Monitors logs and coordinates actions between agents.
- **Diagnosis Agent**: Detects known errors via knowledge base and generates solutions using LLM reasoning.
- **Knowledge Agent**: Stores predefined error patterns and suggested resolutions.
- **Mock Execution**: Simulates automated actions like service restart or cache clearing without making real system changes.
- **Demo-Ready**: Fully working code to showcase AI-driven ITOps automation.

## 🏗️ Architecture
main.py
└─ SupervisorAgent
├─ monitors logs
├─ calls DiagnosisAgent
└─ executes suggested actions
└─ DiagnosisAgent
├─ checks KnowledgeAgent KB
├─ uses OpenAI LLM for unknown issues
└─ returns suggested fixes

text- **Technologies used**: Python, LangChain, OpenAI, python-dotenv.
- **Optional storage**: PostgreSQL (mocked actions for demo).
- **Virtual environment**: Isolated Python venv.

## 🛠️ Installation

1. **Clone the repo and set up environment**:

```bash
# Clone the repository
git clone https://github.com/yuvraj333/ai-itops-agent.git
cd ai-itops-agent


2. **Create and activate virtual environment
python3 -m venv --copies venv
source venv/bin/activate

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Create .env file with OpenAI API Key
echo 'OPENAI_API_KEY="your_openai_api_key_here"' > .env

 ```

##Set OpenAI API key:
 ```bash
Create a .env file in the root folder:
textOPENAI_API_KEY=your_api_key_here
Or set it directly in your terminal:
bashexport OPENAI_API_KEY="your_api_key_here"
 ```

## 🚀 Usage

# Run the main script:

```bash
python main.py
```
# Example output:
```bash
⏱ Monitoring logs...
Issue: Database connection failed | Suggested Action: Restart PostgreSQL service
Executing: Restart PostgreSQL service ...done.
Issue: High memory usage detected | Suggested Action: Clear cache and optimize processes
Executing: Clear cache and optimize processes ...done.
Monitoring complete.
```

## 📂 Project Structure

textai-itops-agent/
├─ agents/
│  ├─ supervisor_agent.py   # Supervises log monitoring and orchestrates actions
│  ├─ diagnosis_agent.py    # Diagnoses issues using KB and LLM
│  └─ knowledge_agent.py    # Stores predefined error patterns
├─ main.py                  # Entry point
├─ requirements.txt         # Python dependencies
├─ .env                     # OpenAI API key
└─ README.md


## 🔧 How It Works

1. **SupervisorAgent** monitors logs (mocked log file in demo)
2. For each log line, it calls **DiagnosisAgent**
3. **DiagnosisAgent**:
   - Checks predefined **KnowledgeAgent** KB for known errors
   - Uses OpenAI GPT-3.5 via LangChain to suggest fixes for unknown issues
4. Suggested actions are executed (mocked) and printed to console

## 📦 Dependencies

- Python 3.12+
- LangChain (langchain, langchain-community)
- OpenAI Python SDK
- python-dotenv

## ⚠️ Important Notes

- This is a demo project for showcasing AI-driven ITOps automation
- LLM-based reasoning generates mock suggestions, not real system changes
- For production use, integrate with actual services, APIs, and monitoring systems
- Ensure proper security measures when working with real systems

## 👨‍💻 Author

**Yuvraj Kumar Mahato** - AI & ML Research Enthusiast

📍 Kathmandu, Nepal  
📧 yuvrajkumarmahato@gmail.com  
[GitHub](https://github.com/yuvraj333) | [LinkedIn](https://www.linkedin.com/in/yuvraj-kumar-mahato-8807551b7/)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 🙏 Acknowledgments

- OpenAI for the GPT models
- LangChain team for the agent framework
- The open-source community for various libraries and tools
