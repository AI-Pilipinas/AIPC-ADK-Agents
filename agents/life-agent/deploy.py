import os

import vertexai
from life_agent.agent import root_agent
from vertexai import agent_engines

PROJECT_ID = os.getenv("GOOGLE_PROJECT_ID")
LOCATION = os.getenv("GOOGLE_PROJECT_LOCATION")
STAGING_BUCKET = os.getenv("GOOGLE_PROJECT_STAGING_BUCKET")

# Initialize the Vertex AI SDK
vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
    staging_bucket=STAGING_BUCKET,
)

app = agent_engines.AdkApp(
    agent=root_agent,
    enable_tracing=True,
)

remote_app = agent_engines.create(
    agent_engine=app, requirements=["google-cloud-aiplatform[adk,agent_engines]"]
)

print("Deployment finished!")
print(f"Resource Name: {remote_app.resource_name}")
