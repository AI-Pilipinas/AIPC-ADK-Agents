"""A mood check agent that can respond kindly to users who are feeling down, anxious, tired, or emotional."""

from google.adk.agents import Agent
from .prompt import mood_check_agent_prompt

mood_check_agent = Agent(
  name="mood_check_agent",
  model="gemini-2.0-flash",
  description="A supportive and empathetic mood-check agent. Your job is to respond kindly to users who are feeling down, anxious, tired, or emotional.",
  instruction=mood_check_agent_prompt,
)