# Multi-Agent Analytics Assistant

## Overview

This project is a **Multi-Agent Analytics Assistant** built using **CrewAI**, **Ollama**, **Streamlit**, **Function Tools**, and a **Local MCP Server**. It uses multiple AI agents to answer business analytics and machine learning queries.

---

## Technologies Used

- Python
- CrewAI 1.15.1
- CrewAI Tools
- Ollama (llama3.2)
- Streamlit
- FastMCP
- Python Dotenv

---

## Agents

### Supervisor Agent
- Manages user requests
- Delegates tasks to other agents

**Function Tools**
- classify_request()
- create_work_plan()

### Data Analyst Agent
- Suggests KPIs
- Recommends dashboards

**Function Tools**
- suggest_kpi()
- recommend_dashboard()

### Data Scientist Agent
- Recommends ML models
- Detects data risks

**Function Tools**
- recommend_ml_model()
- detect_data_risk()

---

## MCP Server

The Local MCP Server provides two tools:

- KPI Tool
- Machine Learning Tool

---

## Run the Project

Activate virtual environment:

```bash
venv\Scripts\activate
```

Start Ollama:

```bash
ollama serve
```

Run Streamlit:

```bash
streamlit run app.py
```

(Optional) Run MCP Server:

```bash
python -m mcp_server.server
```

---

## Project Structure

```
MultiAgentAnalyticsAssistant/
│
├── agents/
├── config/
├── crew/
├── function_tools/
├── mcp_server/
├── app.py
├── requirements.txt
└── README.md
```

---

## Developed By

**Ritam Das**  