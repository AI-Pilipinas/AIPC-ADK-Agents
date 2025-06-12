from google.adk.agents import LlmAgent
from .prompt import effort_scorer_prompt

effort_scorer_agent = LlmAgent(
    name="effort_score_agent",
    model="gemini-2.0-flash",
    description="An effort scorer agent that scores the effort required for each chore.",
    instruction=effort_scorer_prompt,
    output_key="effort_scores"
)