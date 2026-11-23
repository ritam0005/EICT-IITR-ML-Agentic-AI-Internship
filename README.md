# Machine Learning & Agentic AI — Summer Training & Internship Program

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-000000?style=for-the-badge)
![Ollama](https://img.shields.io/badge/Ollama-Llama_3.2-111111?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

> **Organization:** E&ICT Academy, IIT Roorkee (Supported by MeitY, Govt. of India)  
> **Intern:** Ritam Das (B.Tech CSE, Adamas University, Kolkata)  
> **Duration:** 01 June 2026 – 15 July 2026  
> **Industry Mentor:** Prof. Sanjeev Manhas (Principal Investigator, E&ICT Academy, IIT Roorkee)  
> **Certificate ID:** `EICTIITR-STP-MLAI-26-35B1X`

---

## Overview
This repository contains the three end-to-end projects completed during the **Machine Learning & Agentic AI** Summer Training & Internship Program at **E&ICT Academy, IIT Roorkee**:
1. **XGBoost and Decision Tree** (Movie Revenue & Technical Oscar Prediction)
2. **Agents with tools and mcp server** (Multi-Agent Analytics Assistant)
3. **Resume - Job Description matching using a Siamese BiLSTM DNN**

---

## 1. XGBoost and Decision Tree
**Folder:** `01-XGBoost-and-Decision-Tree/`

End-to-end regression (`Movie_regression.csv`, target: `Collection`) and classification (`Movie_classification.csv`, target: `Start_Tech_Oscar`) pipelines built in Python.
- **Methodology:** EDA, `ColumnTransformer` preprocessing pipelines (imputation + one-hot encoding), Decision Tree pre-pruning & post-pruning, 5-fold Cross-Validation, Grid Search, XGBoost, LightGBM, and model persistence via `Joblib`.
- **Test Set Results:**

| Model | Regression $R^2$ | Regression RMSE | Classification Accuracy | Classification F1-Score |
| :--- | :---: | :---: | :---: | :---: |
| Base Decision Tree | 0.8077 | 7532.34 | 0.5686 | 0.6000 |
| Pre-Pruned Decision Tree | 0.7980 | 7719.99 | 0.5686 | 0.6508 |
| Post-Pruned Decision Tree | 0.8787 | 5981.87 | 0.5882 | 0.6379 |
| Grid Search Decision Tree | 0.8907 | 5678.68 | 0.5490 | 0.4889 |
| **XGBoost** | **0.9133** | **5056.40** | 0.6471 | 0.6786 |
| **LightGBM** | 0.8289 | 7104.22 | **0.6765** | **0.7027** |

---

## 2. Agents with tools and mcp server
**Folder:** `02-Agents-with-Tools-and-MCP-Server/`

A fully local, privacy-preserving **Multi-Agent Analytics Assistant** built with **CrewAI**, **Ollama (Llama 3.2)**, **Streamlit**, custom function tools, and a local **MCP Server**.
- **Architecture:** A **Supervisor Agent** delegates queries to specialist **Data Scientist** (ML, AI, statistics) and **Data Analyst** (SQL, KPIs, dashboards) agents configured via `agents.yaml` and `tasks.yaml`.
- **Quick Start:**
```bash
cd 02-Agents-with-Tools-and-MCP-Server
python -m venv venv
# Activate: venv\Scripts\activate (Windows) | source venv/bin/activate (Mac/Linux)
pip install -r requirements.txt
ollama serve
streamlit run app.py
```
---
## 3. Resume - Job Description matching using a Siamese BiLSTM DNN
**Folder:** `Resume-JD Match Scorer/`

A deep learning NLP system trained on a JSONL dataset of resume and job description pairs to classify candidate fit into **Weak Match**, **Medium Match**, or **Strong Match**, while outputting class probabilities and shared/missing skills.
- **Architecture:** Siamese Bidirectional LSTM network with shared weights in TensorFlow/Keras, `TextVectorization`, `EarlyStopping`, and `ModelCheckpoint` (`resume_jd_match_model_final.keras`).
- **Test Set Performance:**

| Metric | Score |
| :--- | :---: |
| **Accuracy** | **0.8699** (86.99%) |
| **Precision** | **0.8733** (87.33%) |
| **Recall** | **0.8699** (86.99%) |
| **F1-Score** | **0.8695** (86.95%) |

---

## Author
**Ritam Das** — B.Tech CSE, Adamas University, Kolkata  
GitHub: [@ritam0005](https://github.com/ritam0005)
