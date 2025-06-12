from google.adk.agents import LlmAgent
from .prompt import priority_merger_prompt

priority_merger_agent = LlmAgent(
    name="priority_merger_agent",
    model="gemini-2.0-flash",
    description="Combines effort, urgency, and preference assessments into final chore priorities with calculated scores.",
    instruction=priority_merger_prompt,
    output_key="prioritized_chores"
)
