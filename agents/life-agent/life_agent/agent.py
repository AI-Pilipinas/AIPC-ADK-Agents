
"""A personal life agent that can help you with your daily life."""

from google.adk.agents import Agent
from .sub_agents.quote import quote_agent
from .sub_agents.fun_fact import fun_fact_agent
from .sub_agents.mood_check import mood_check_agent
from .prompt import personal_life_assistant_prompt

root_agent = Agent(
  name="your_personal_life_agent",
  model="gemini-2.0-flash",
  description="A personal life agent that can help you with your daily life",
  instruction=personal_life_assistant_prompt,
  sub_agents=[
    quote_agent,
    mood_check_agent,
    fun_fact_agent
  ]
)