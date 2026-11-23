from crewai.tools import tool


@tool("Suggest KPI")
def suggest_kpi(domain: str) -> str:
    """Suggest KPIs for a business domain."""

    domain = domain.lower()

    if domain == "ecommerce":
        return """
KPIs
- Revenue
- Conversion Rate
- Average Order Value
- Customer Retention
"""

    elif domain == "education":
        return """
KPIs
- Student Enrollment
- Course Completion
- Student Satisfaction
"""

    return """
KPIs
- Revenue
- Growth
- Customer Count
"""


@tool("Recommend Dashboard")
def recommend_dashboard(domain: str) -> str:
    """Recommend dashboard widgets."""

    return f"""
Dashboard for {domain}

- KPI Cards
- Line Chart
- Bar Chart
- Pie Chart
"""