from google.adk.agents import SequentialAgent

from ..priority_assigner.agent import priority_assigner_agent
from ..priority_merger.agent import priority_merger_agent
from ..chore_balancer.agent import chore_balancer_agent
from ..plan_formatter.agent import plan_formatter_agent

process_sequencer_agent = SequentialAgent(
    name="process_sequencer_agent",
    description="Sequences the process of chore organization.",
    sub_agents=[
        priority_assigner_agent,
        priority_merger_agent,
        chore_balancer_agent,
        plan_formatter_agent
    ]
)