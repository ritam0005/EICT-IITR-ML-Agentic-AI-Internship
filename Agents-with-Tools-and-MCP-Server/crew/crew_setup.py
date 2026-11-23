from crewai import Crew, Task, Process

from agents.supervisor_agent import get_supervisor_agent
from agents.analyst_agent import get_analyst_agent
from agents.scientist_agent import get_scientist_agent


supervisor = get_supervisor_agent()
analyst = get_analyst_agent()
scientist = get_scientist_agent()


def run_crew(user_query: str):

    task = Task(
        description=f"""
User Request:

{user_query}

If the request is related to:

• KPI
• Dashboard
• SQL
• Report

delegate to Data Analyst.

If the request is related to:

• Machine Learning
• Prediction
• Classification
• AI

delegate to Data Scientist.

Finally return the answer to the user.
""",

        expected_output="Final response.",

        agent=supervisor,
    )

    crew = Crew(
        agents=[
            analyst,
            scientist,
        ],

        tasks=[
            task,
        ],

        process=Process.hierarchical,

        manager_agent=supervisor,

        verbose=True,
    )

    result = crew.kickoff()

    return str(result)