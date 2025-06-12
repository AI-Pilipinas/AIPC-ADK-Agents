from google.adk.agents import LlmAgent

from .prompt import chore_collector_prompt
from .tools import get_current_date

chore_collector_agent = LlmAgent(
    name="chore_collector_agent",
    model="gemini-2.0-flash",
    description="A chore collector agent that collects chores from user input.",
    instruction=chore_collector_prompt,
    tools=[get_current_date],
    output_key="chore_list"
)