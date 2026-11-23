from crewai import Agent

from config.settings import MODEL, BASE_URL, TEMPERATURE
from function_tools.supervisor_tools import (
    classify_request,
    create_work_plan,
)
from crewai import LLM

llm = LLM(
    model=f"ollama/{MODEL}",
    base_url=BASE_URL,
    temperature=TEMPERATURE,
)


def get_supervisor_agent():
    return Agent(
        role="Supervisor Agent",
        goal="Understand the user request and delegate work.",
        backstory=(
            "You manage the analytics team and decide which specialist "
            "should answer the user."
        ),
        llm=llm,
        allow_delegation=True,
        verbose=True,
    )