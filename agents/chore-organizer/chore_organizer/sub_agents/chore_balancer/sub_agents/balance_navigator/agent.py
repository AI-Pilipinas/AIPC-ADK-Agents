from google.adk.agents import LlmAgent
from google.adk.tools.tool_context import ToolContext

from .prompt import balance_navigator_prompt

def exit_loop(tool_context: ToolContext):
  """Call this function ONLY when the critique indicates no further changes are needed, signaling the iterative process should end."""
  print(f"  [Tool Call] exit_loop triggered by {tool_context.agent_name}")
  tool_context.actions.escalate = True
  # Return empty dict as tools should typically return JSON-serializable output
  return {}

balance_navigator_agent = LlmAgent(
    name="balance_navigator_agent",
    model="gemini-2.0-flash",
    description="Ensures schedules are sustainable and energy-appropriate.",
    instruction=balance_navigator_prompt,
    tools=[exit_loop],
    output_key="balanced_weekly_schedule"
)