from crewai.tools import tool


@tool("Classify Request")
def classify_request(query: str) -> str:
    """Identify which agent should handle the request."""

    text = query.lower()

    if any(word in text for word in ["machine learning", "prediction", "classification", "regression", "ai"]):
        return "Data Scientist"

    elif any(word in text for word in ["sales", "dashboard", "kpi", "sql", "report"]):
        return "Data Analyst"

    return "Supervisor"


@tool("Create Work Plan")
def create_work_plan(query: str) -> str:
    """Generate a simple execution plan."""

    return f"""
Execution Plan

1. Read the user request
2. Identify the correct agent
3. Execute the task
4. Return the final response

User Request:
{query}
"""