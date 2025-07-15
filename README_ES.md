# 🧠 ai-chat-ui

Interfaz web construida con **Python** y **Flask** para interacción directa con agentes LangChain y modelos LLM (Ollama, OpenAI).
Ofrece una UI sencilla para pruebas rápidas, interacción con agentes, y visualización de respuestas en tiempo real.

---

## 🎯 Propósito

Proporciona un punto de acceso visual a (`devops-ai-lab`).
Facilita la interacción y pruebas con agentes de razonamiento LangChain (`ai-agent`) que orquestan tareas complejas de DevOps vía `ai-gateway`.

Esta interfaz representa el acceso frontal del usuario.

---

## 🔧 Funcionalidad

El UI interactúa directamente mediante HTTP con herramientas desplegadas vía `ai-gateway`, permitiendo:

- Pruebas rápidas de prompts sobre herramientas IA.
- Visualización clara y estructurada de respuestas obtenidas por los agentes.
- Trazabilidad básica de interacciones.

---

## ⚙️ Estructura del Proyecto

```
ai-chat-ui/
├── chat_ui.py              # Aplicación Flask principal
├── Dockerfile              # Dockerización del servicio
├── Jenkinsfile             # Pipeline CI/CD para Jenkins
├── Makefile                # Automatización tareas build/despliegue
├── requirements.txt        # Dependencias Python
├── LICENSE                 # Licencia del proyecto
├── README.md               # Este archivo
└── .gitignore
```

---

## 🚀 Ejecución Local

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python chat_ui.py
```

Accede vía navegador en `http://localhost:5000` para interactuar con la interfaz.

---

## 🌐 Comunicación con el entorno

La aplicación se comunica con microservicios IA mediante peticiones HTTP hacia `ai-gateway` definidas en ai-agent.

Endpoints típicos:

- `POST /generate-pipeline`
- `POST /analyze-log`
- `POST /lint-chart`

---

## 🧠 Inteligencia y Modelos

- **Por defecto** utiliza modelos accesibles vía `ai-gateway`: Ollama (local) o OpenAI (remoto).
- Fácilmente configurable en el archivo `chat_ui.py`.

---

## 🔎 Observabilidad y Trazabilidad

- Logs básicos disponibles en stdout.
- Integrable con sistema MCP mediante llamadas al gateway.

---

## 📦 Dependencias principales

```text
flask
requests
python-dotenv
```

---

## 📌 Estado actual

- Interfaz básica operativa
- En desarrollo funciones avanzadas

---

## 👨‍💻 Autor

**Dani**  
[github.com/dorado-ai-devops](https://github.com/dorado-ai-devops)

---

## 🛡 Licencia

Licencia Pública General GNU v3.0

