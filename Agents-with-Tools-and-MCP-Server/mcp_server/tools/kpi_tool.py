"""
KPI Tool
Provides KPI recommendations for different business domains.
"""

def suggest_kpis(domain: str) -> str:
    domain = domain.lower()

    if domain == "ecommerce":
        return """
Recommended KPIs

• Revenue
• Conversion Rate
• Average Order Value
• Customer Retention
"""

    elif domain == "education":
        return """
Recommended KPIs

• Student Enrollment
• Course Completion Rate
• Student Satisfaction
"""

    return """
Recommended KPIs

• Revenue
• Growth
• Customer Count
"""