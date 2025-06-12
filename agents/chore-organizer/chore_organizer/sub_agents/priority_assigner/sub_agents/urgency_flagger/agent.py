from google.adk.agents import LlmAgent
from .prompt import urgency_flagger_prompt

urgency_flag_agent = LlmAgent(
    name="urgency_flag_agent",
    model="gemini-2.0-flash",
    description="An urgency flagger agent that flags the urgency of each chore.",
    instruction=urgency_flagger_prompt,
    output_key="urgency_flags"
)