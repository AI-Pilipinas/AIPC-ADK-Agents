from google.adk.agents import LlmAgent

from .prompt import scheduler_prompt

scheduler_agent = LlmAgent(
    name="scheduler_agent",
    model="gemini-2.0-flash",
    description="Assigns chores to specific days and time slots.",
    instruction=scheduler_prompt,
    output_key="weekly_schedule"
)