from google.adk.agents import LoopAgent

from .sub_agents import balance_navigator_agent, scheduler_agent

chore_balancer_agent = LoopAgent(
    name="chore_balancer_agent",
    sub_agents=[scheduler_agent, balance_navigator_agent],
    max_iterations=3
)