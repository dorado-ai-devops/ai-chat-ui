import streamlit as st
import requests

# Backend Agente
AI_AGENT_API_URL = "http://ai-agent-service.devops-ai.svc.cluster.local:6001/ask"

st.set_page_config(page_title="AI Chat UI", layout="wide")
st.title("Chat DevOps")

if "history" not in st.session_state:
    st.session_state["history"] = []

def ask_agent(prompt):
    try:
        response = requests.post(AI_AGENT_API_URL, json={"prompt": prompt}, timeout=120)
        if response.status_code == 200:
            data = response.json()
            return data.get("result", data)
        else:
            return f"Error: {response.status_code} {response.text}"
    except Exception as e:
        return f"Error de conexión: {e}"


with st.form(key="chat_form"):
    user_input = st.text_area("Mensaje", value="", height=100)
    submit = st.form_submit_button("Enviar")
    if submit and user_input.strip():
        st.session_state["history"].append(("Tú", user_input))
        ai_reply = ask_agent(user_input)
        st.session_state["history"].append(("AI", ai_reply))


for role, msg in reversed(st.session_state["history"]):
    st.markdown(f"**{role}:**")
    st.write(msg)
    st.markdown("---")
