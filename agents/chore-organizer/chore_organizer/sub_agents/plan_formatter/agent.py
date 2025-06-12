from google.adk.agents import LlmAgent
from .prompt import plan_formatter_prompt

plan_formatter_agent = LlmAgent(
    name="plan_formatter_agent",
    model="gemini-2.0-flash",
    description="Formats the chore schedule into a user-friendly plan.",
    instruction=plan_formatter_prompt,
)