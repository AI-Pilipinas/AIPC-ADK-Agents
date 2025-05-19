
"""A fun fact agent that can share surprising, wholesome, or interesting facts that make people smile or learn something new."""

from google.adk.agents import Agent
from .prompt import fun_fact_agent_prompt

fun_fact_agent = Agent(
  name="fun_fact_agent",
  model="gemini-2.0-flash",
  description="A fun fact agent. Your role is to share surprising, wholesome, or interesting facts that make people smile or learn something new.",
  instruction=fun_fact_agent_prompt,
)