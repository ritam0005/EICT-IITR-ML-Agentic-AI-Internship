from crewai import Agent, LLM

from config.settings import MODEL, BASE_URL, TEMPERATURE
from function_tools.analyst_tools import (
    suggest_kpi,
    recommend_dashboard,
)

llm = LLM(
    model=f"ollama/{MODEL}",
    base_url=BASE_URL,
    temperature=TEMPERATURE,
)


def get_analyst_agent():
    return Agent(
        role="Data Analyst",
        goal="Generate KPIs and business insights.",
        backstory=(
            "You are an expert in dashboards, reports and business analysis."
        ),
        llm=llm,
        tools=[
            suggest_kpi,
            recommend_dashboard,
        ],
        verbose=True,
    )