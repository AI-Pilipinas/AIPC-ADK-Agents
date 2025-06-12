from google.adk.agents import ParallelAgent

from .sub_agents import effort_scorer_agent, urgency_flag_agent, preference_setter_agent

priority_assigner_agent = ParallelAgent(
    name="priority_assigner_agent",
    description="Runs effort, urgency, and preference analysis in parallel to provide a comprehensive priority assessment.",
    sub_agents=[
        effort_scorer_agent,
        urgency_flag_agent,
        preference_setter_agent
    ]
)