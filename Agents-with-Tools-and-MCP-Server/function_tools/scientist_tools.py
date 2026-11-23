from crewai.tools import tool


@tool("Recommend ML Model")
def recommend_ml_model(problem: str) -> str:
    """Recommend an ML model."""

    text = problem.lower()

    if "predict" in text:
        return "Regression"

    if "classify" in text:
        return "Classification"

    if "cluster" in text:
        return "Clustering"

    return "General Machine Learning"


@tool("Detect Data Risk")
def detect_data_risk(problem: str) -> str:
    """Identify common ML risks."""

    return """
Possible Risks

- Missing Values
- Duplicate Records
- Data Leakage
- Class Imbalance
"""