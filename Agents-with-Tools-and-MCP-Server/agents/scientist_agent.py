from crewai import Agent, LLM

from config.settings import MODEL, BASE_URL, TEMPERATURE
from function_tools.scientist_tools import (
    recommend_ml_model,
    detect_data_risk,
)

llm = LLM(
    model=f"ollama/{MODEL}",
    base_url=BASE_URL,
    temperature=TEMPERATURE,
)


def get_scientist_agent():
    return Agent(
        role="Data Scientist",
        goal="Recommend ML models and AI solutions.",
        backstory=(
            "You are an AI engineer specialized in machine learning."
        ),
        llm=llm,
        tools=[
            recommend_ml_model,
            detect_data_risk,
        ],
        verbose=True,
    )