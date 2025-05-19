from google.adk.agents import Agent
from google.adk.agents import SequentialAgent

from .sub_agents.agent import (
    job_description_agent,
    workflow_analysis_agent,
    prompt_engineer_agent
)

# --- 1. Define Root Agent ---

root_agent = SequentialAgent(
    name='workflow',
    description="A sequential workflow for role automation",
    sub_agents=[
        job_description_agent,
        workflow_analysis_agent,
        prompt_engineer_agent,
    ],
)