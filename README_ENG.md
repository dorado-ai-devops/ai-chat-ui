# 🧠 ai-chat-ui

Web interface built with **Python** and **Flask** for direct interaction with LangChain agents and LLM models (Ollama, OpenAI).
Provides a simple UI for quick tests, agent interactions, and real-time response visualization.

---

## 🎯 Purpose

Offers a visual entry point to (`devops-ai-lab`).
Facilitates interactions and testing with LangChain reasoning agents (`ai-agent`) that orchestrate complex DevOps tasks via `ai-gateway`.

This interface represents the user's frontend access.

---

## 🔧 Features

The UI directly interacts via HTTP with tools deployed through `ai-gateway`, enabling:

- Quick prompt testing on AI tools.
- Clear and structured visualization of agent responses.
- Basic interaction traceability.

---

## ⚙️ Project Structure

```
ai-chat-ui/
├── chat_ui.py              # Main Flask application
├── Dockerfile              # Dockerization of the service
├── Jenkinsfile             # CI/CD pipeline for Jenkins
├── Makefile                # Automation of build/deployment tasks
├── requirements.txt        # Python dependencies
├── LICENSE                 # Project license
├── README.md               # This file
└── .gitignore
```

---

## 🚀 Local Execution

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python chat_ui.py
```

Access via browser at `http://localhost:5000` to interact with the interface.

---

## 🌐 Environment Communication

The application communicates with AI microservices through HTTP requests defined in `ai-agent` via `ai-gateway`.

Typical endpoints:

- `POST /generate-pipeline`
- `POST /analyze-log`
- `POST /lint-chart`

---

## 🧠 Intelligence and Models

- **By default**, it uses models accessible via `ai-gateway`: Ollama (local) or OpenAI (remote).
- Easily configurable in the `chat_ui.py` file.

---

## 🔎 Observability and Traceability

- Basic logs available in stdout.
- Integrable with MCP system via gateway calls.

---

## 📦 Main Dependencies

```text
flask
requests
python-dotenv
```

---

## 📌 Current Status

- Basic operational interface
- Advanced features under development

---

## 👨‍💻 Author

**Dani**  
[github.com/dorado-ai-devops](https://github.com/dorado-ai-devops)

---

## 🛡 License

GNU General Public License v3.0

