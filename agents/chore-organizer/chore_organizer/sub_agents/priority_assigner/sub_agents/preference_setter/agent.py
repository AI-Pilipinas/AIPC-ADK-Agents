from google.adk.agents import LlmAgent
from .prompt import preference_setter_prompt

preference_setter_agent = LlmAgent(
    name="preference_setter_agent",
    model="gemini-2.0-flash",
    description="A preference setter agent that sets the preference for each chore.",
    instruction=preference_setter_prompt,
    output_key="preferences"
)