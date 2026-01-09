# Google Agent Development Kit (ADK) - Python

The Agent Development Kit (ADK) is a flexible, code-first Python framework for building, evaluating, and deploying sophisticated AI agents. Designed primarily for Google's Gemini models (including Gemini 2.5 Flash, Gemini 3 Pro, and native audio/video models) but model-agnostic at its core, ADK enables developers to create everything from simple single-agent assistants to complex multi-agent orchestration systems. The framework emphasizes software development best practices, making agent development feel like traditional application development with full testability, versioning, and deployment flexibility.

ADK provides a rich ecosystem of pre-built tools for Google services (Search, BigQuery, Spanner, Bigtable, Pub/Sub, Vertex AI), support for custom function tools, MCP (Model Context Protocol) tool integration, OpenAPI and API Registry toolsets, multi-agent coordination patterns (sequential, parallel, loop), session and state management with multiple backend options (in-memory, SQLite, PostgreSQL, Vertex AI), evaluation frameworks, and deployment options ranging from local development to Cloud Run and Vertex AI Agent Engine. With built-in observability, authentication flows, session rewind capabilities, custom service registration, Interactions API support for long-running conversations, computer use tools for desktop automation, and a development UI with live streaming support, ADK streamlines the entire agent development lifecycle from prototyping to production.

## Agent Creation and Configuration

### Creating a Simple Agent

```python
from google.adk import Agent, Runner
from google.adk.tools import google_search
from google.adk.sessions import InMemorySessionService
from google.genai import types

# Define agent with model, instructions, and tools
agent = Agent(
    name="search_assistant",
    model="gemini-2.5-flash",
    instruction="You are a helpful assistant. Answer user questions using Google Search when needed.",
    description="An assistant that can search the web.",
    tools=[google_search]
)

# Create runner with session service
runner = Runner(
    app_name="my_app",
    agent=agent,
    session_service=InMemorySessionService()
)

# Run agent asynchronously
async def run_query():
    content = types.Content(role='user', parts=[types.Part(text="What's the weather in Tokyo?")])
    async for event in runner.run_async(
        user_id="user123",
        session_id="session456",
        new_message=content
    ):
        if event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    print(f"[{event.author}]: {part.text}")
```

### Creating Custom Function Tools

```python
from google.adk import Agent
from google.adk.tools.tool_context import ToolContext
import random

def roll_die(sides: int, tool_context: ToolContext) -> int:
    """Roll a die and return the result.

    Args:
        sides: The integer number of sides the die has.

    Returns:
        An integer of the result of rolling the die.
    """
    result = random.randint(1, sides)
    if 'rolls' not in tool_context.state:
        tool_context.state['rolls'] = []
    tool_context.state['rolls'].append(result)
    return result

async def check_prime(nums: list[int]) -> str:
    """Check if given numbers are prime.

    Args:
        nums: The list of numbers to check.

    Returns:
        A string indicating which numbers are prime.
    """
    primes = {num for num in nums if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))}
    return f"{', '.join(str(n) for n in primes)} are prime numbers." if primes else "No prime numbers found."

# Create agent with custom tools
dice_agent = Agent(
    model='gemini-2.5-flash',
    name='dice_agent',
    description='Agent that can roll dice and check prime numbers.',
    instruction="""You roll dice and check prime numbers.
    Always call roll_die first, then check_prime with the results.""",
    tools=[roll_die, check_prime]
)
```

## Multi-Agent Systems

### Hierarchical Multi-Agent with Sub-Agents

```python
from google.adk.agents import LlmAgent
from google.adk.tools import google_search

# Define specialized agents
greeter = LlmAgent(
    name="greeter",
    model="gemini-2.5-flash",
    description="Greets users and provides welcoming messages.",
    instruction="You greet users warmly and professionally."
)

task_executor = LlmAgent(
    name="task_executor",
    model="gemini-2.5-flash",
    description="Executes tasks and provides solutions.",
    instruction="You execute tasks efficiently and provide detailed solutions.",
    tools=[google_search]
)

# Create coordinator agent with sub-agents
coordinator = LlmAgent(
    name="coordinator",
    model="gemini-2.5-flash",
    description="Coordinates greetings and task execution.",
    instruction="You coordinate between greeting users and executing their tasks. Delegate appropriately.",
    sub_agents=[greeter, task_executor]
)
```

### Sequential Agent Workflow

```python
from google.adk.agents import SequentialAgent, LlmAgent

# Define agents for each step
research_agent = LlmAgent(
    name="researcher",
    model="gemini-2.5-flash",
    instruction="Research the topic thoroughly.",
    tools=[google_search]
)

writer_agent = LlmAgent(
    name="writer",
    model="gemini-2.5-flash",
    instruction="Write a comprehensive article based on the research."
)

editor_agent = LlmAgent(
    name="editor",
    model="gemini-2.5-flash",
    instruction="Edit and polish the article for publication."
)

# Create sequential workflow
content_pipeline = SequentialAgent(
    name="content_pipeline",
    description="Research, write, and edit content sequentially.",
    sub_agents=[research_agent, writer_agent, editor_agent]
)
```

### Parallel Agent Execution

```python
from google.adk.agents import ParallelAgent, LlmAgent

# Define agents that run in parallel
fact_checker = LlmAgent(
    name="fact_checker",
    model="gemini-2.5-flash",
    instruction="Verify facts in the content.",
    tools=[google_search]
)

sentiment_analyzer = LlmAgent(
    name="sentiment_analyzer",
    model="gemini-2.5-flash",
    instruction="Analyze sentiment of the content."
)

seo_optimizer = LlmAgent(
    name="seo_optimizer",
    model="gemini-2.5-flash",
    instruction="Suggest SEO improvements."
)

# Run multiple agents in parallel
parallel_analyzer = ParallelAgent(
    name="content_analyzer",
    description="Analyze content from multiple perspectives simultaneously.",
    sub_agents=[fact_checker, sentiment_analyzer, seo_optimizer]
)
```

### Loop Agent for Iterative Tasks

```python
from google.adk.agents import LoopAgent, LlmAgent
from google.adk.tools import exit_loop

# Define agent that iterates
problem_solver = LlmAgent(
    name="problem_solver",
    model="gemini-2.5-flash",
    instruction="""Solve the problem step by step.
    Call exit_loop when you have a complete solution.""",
    tools=[exit_loop]
)

# Create loop agent with max iterations
iterative_solver = LoopAgent(
    name="iterative_solver",
    description="Solve problems through iterative refinement.",
    sub_agents=[problem_solver],
    max_iterations=5
)
```

## Application and Runner Configuration

### Creating an App with Configuration

```python
from google.adk.apps import App, ResumabilityConfig
from google.adk import Agent, Runner
from google.adk.sessions import InMemorySessionService
from google.adk.artifacts import InMemoryArtifactService
from google.adk.memory import InMemoryMemoryService

# Define root agent
root_agent = Agent(
    name="assistant",
    model="gemini-2.5-flash",
    instruction="You are a helpful assistant."
)

# Create app with resumability
app = App(
    name="my_application",
    root_agent=root_agent,
    resumability_config=ResumabilityConfig(is_resumable=True)
)

# Initialize services
session_service = InMemorySessionService()
artifact_service = InMemoryArtifactService()
memory_service = InMemoryMemoryService()

# Create runner with full configuration
runner = Runner(
    app=app,
    session_service=session_service,
    artifact_service=artifact_service,
    memory_service=memory_service
)

# Run with session management
async def run_with_session():
    session = await session_service.create_session(
        app_name="my_application",
        user_id="user123",
        state={"context": "initial_state"}
    )

    from google.genai import types
    message = types.Content(role='user', parts=[types.Part(text="Hello!")])

    async for event in runner.run_async(
        user_id=session.user_id,
        session_id=session.id,
        new_message=message
    ):
        if event.content:
            print(event.content)
```

## Built-in Tools and Integrations

### Using Google Search and Web Tools

```python
from google.adk import Agent
from google.adk.tools import google_search, url_context

search_agent = Agent(
    name="web_researcher",
    model="gemini-2.5-flash",
    instruction="Research topics using web search and extract content from URLs.",
    tools=[google_search, url_context]
)
```

### MCP (Model Context Protocol) Tools Integration

```python
from google.adk import Agent
from google.adk.tools import McpToolset
from google.adk.tools.mcp_tool.mcp_toolset import StdioServerParameters
import json
import os

# Configure MCP connection with environment variables
notion_api_key = os.getenv("NOTION_API_KEY")
notion_headers = json.dumps({
    "Authorization": f"Bearer {notion_api_key}",
    "Notion-Version": "2022-06-28",
})

# Create agent with MCP toolset
mcp_agent = Agent(
    name="notion_assistant",
    model="gemini-2.5-flash",
    instruction="You are my workspace assistant. Use the provided tools to read, search, and manage Notion pages.",
    tools=[
        McpToolset(
            connection_params=StdioServerParameters(
                command="npx",
                args=["-y", "@notionhq/notion-mcp-server"],
                env={"OPENAPI_MCP_HEADERS": notion_headers}
            )
        )
    ]
)

# MCP tools support multiple connection types:
# - StdioServerParameters: For stdio-based MCP servers
# - RemoteServerParameters: For remote MCP servers via HTTP/WebSocket
# - SSEServerParameters: For server-sent events connections
```

### BigQuery Integration

```python
from google.adk import Agent
from google.adk.tools.bigquery_toolset import BigQueryToolset

# Initialize BigQuery toolset
bigquery_tools = BigQueryToolset(project_id="my-project")

# Create agent with BigQuery tools
data_analyst = Agent(
    name="data_analyst",
    model="gemini-2.5-flash",
    instruction="Analyze data using BigQuery. Execute SQL queries and provide insights.",
    tools=bigquery_tools.get_tools()
)

# Example usage
# The agent can now execute queries like:
# "Query the sales table and show top 10 products by revenue"
# Available tools: get_dataset_info, get_table_info, list_dataset_ids,
# list_table_ids, execute_sql, forecast, analyze_contribution,
# detect_anomalies, ask_data_insights
```

### Spanner and Bigtable Integration

```python
from google.adk import Agent
from google.adk.tools.spanner import SpannerToolset
from google.adk.tools.bigtable import BigtableToolset

# Initialize Spanner toolset for relational database operations
spanner_tools = SpannerToolset(
    project_id="my-project",
    instance_id="my-instance",
    database_id="my-database"
)

# Initialize Bigtable toolset for NoSQL operations
bigtable_tools = BigtableToolset(
    project_id="my-project",
    instance_id="my-instance"
)

# Create agent with database tools
database_agent = Agent(
    name="database_agent",
    model="gemini-2.5-flash",
    instruction="Query and manage data across Spanner and Bigtable databases.",
    tools=[*spanner_tools.get_tools(), *bigtable_tools.get_tools()]
)
```

### API Registry Integration

```python
from google.adk import Agent
from google.adk.tools import APIRegistryToolset

# Create toolset from Cloud API Registry
api_tools = APIRegistryToolset(
    project_id="my-project",
    location="us-central1",
    api_id="my-api",
    version_id="v1"
)

# Create agent with API Registry tools
api_agent = Agent(
    name="api_agent",
    model="gemini-2.5-flash",
    instruction="Use the API Registry tools to interact with registered APIs.",
    tools=api_tools.get_tools()
)
```

### Code Execution Tools

```python
from google.adk import Agent
from google.adk.code_executors import (
    BuiltInCodeExecutor,
    AgentEngineSandboxCodeExecutor,
    ContainerCodeExecutor,
    GkeCodeExecutor,
    VertexAiCodeExecutor
)

# Create agent with built-in code execution capability (Gemini's native executor)
code_agent = Agent(
    name="code_executor",
    model="gemini-2.5-flash",
    instruction="You can execute Python code to solve problems. Write and run code when needed.",
    code_executor=BuiltInCodeExecutor()
)

# Or use Vertex AI Code Execution Sandbox for enhanced security
sandbox_agent = Agent(
    name="sandbox_executor",
    model="gemini-2.5-flash",
    instruction="Execute code safely in a sandboxed environment.",
    code_executor=AgentEngineSandboxCodeExecutor()
)

# Other code execution options:
# - ContainerCodeExecutor: Docker-based execution
# - GkeCodeExecutor: Google Kubernetes Engine execution
# - VertexAiCodeExecutor: Vertex AI managed execution
```

### Computer Use Tools for Desktop Automation

```python
from google.adk import Agent
from google.adk.tools.computer_use import ComputerUseTool

# Create computer use tool for desktop automation
computer_tool = ComputerUseTool()

# Create agent with desktop automation capability
automation_agent = Agent(
    name="desktop_agent",
    model="gemini-2.5-flash",
    instruction="You can control the desktop, take screenshots, and interact with applications.",
    tools=[computer_tool]
)

# The agent can now perform actions like:
# - Taking screenshots
# - Moving the mouse
# - Clicking elements
# - Typing text
# - Running desktop applications
```

## Session and State Management

### Managing Sessions with Multiple Backends

```python
from google.adk.sessions import (
    InMemorySessionService,
    SqliteSessionService,
    DatabaseSessionService,
    VertexAiSessionService
)
from google.adk.sessions import Session

# Use in-memory session service (for development only - not persistent)
session_service = InMemorySessionService()

# Or use SQLite-backed session service for local persistence
sqlite_service = SqliteSessionService(db_path="sessions.db")

# Or use database session service for production (PostgreSQL, MySQL, etc.)
database_service = DatabaseSessionService(uri="postgresql://user:pass@host:5432/dbname")

# Or use Vertex AI session service for cloud-based persistence
vertex_service = VertexAiSessionService(project_id="my-project", location="us-central1")

async def session_management_example():
    # Create session with initial state
    session = await session_service.create_session(
        app_name="my_app",
        user_id="user123",
        state={"preferences": {"language": "en"}, "context": "customer_support"}
    )

    # Retrieve existing session
    retrieved = await session_service.get_session(
        app_name="my_app",
        user_id="user123",
        session_id=session.id
    )

    # Update session state
    await session_service.update_session_state(
        app_name="my_app",
        user_id="user123",
        session_id=session.id,
        state={"preferences": {"language": "es"}}
    )

    # List all sessions for user
    sessions = await session_service.list_sessions(
        app_name="my_app",
        user_id="user123"
    )

    return session
```

### Session Rewind

```python
from google.adk import Runner
from google.adk.sessions import InMemorySessionService

# Create runner with session service
runner = Runner(
    app_name="my_app",
    agent=my_agent,
    session_service=InMemorySessionService()
)

async def rewind_session():
    # Rewind session to before a specific invocation
    # This allows undoing previous interactions and starting from an earlier point
    await runner.rewind_session(
        user_id="user123",
        session_id="session456",
        invocation_id="invocation789"
    )

    # The session history is now reverted to the state before invocation789
    # You can continue with new interactions from this point
```

## Service Registration and Custom Backends

### Custom Service Registration via YAML

```yaml
# Create services.yaml in your agent directory
services:
  - scheme: mysession
    type: session
    class: my_package.my_module.MyCustomSessionService
  - scheme: myartifacts
    type: artifact
    class: my_package.artifacts.MyCustomArtifactService
  - scheme: mymemory
    type: memory
    class: my_package.memory.MyCustomMemoryService
```

### Custom Service Registration via Python

```python
# Create services.py in your agent directory
from google.adk.cli.service_registry import get_service_registry
from my_package.my_module import MyCustomSessionService

def my_session_factory(uri: str, **kwargs):
    # Custom initialization logic
    return MyCustomSessionService(uri=uri, **kwargs)

# Register custom service
get_service_registry().register_session_service("mysession", my_session_factory)

# Now you can use custom URIs in your configuration:
# --session-uri mysession://my-custom-backend
```

### Using File-Based Artifact Service

```python
from google.adk import Runner
from google.adk.artifacts import FileArtifactService
from pathlib import Path

# Create file-based artifact service for local storage
artifact_service = FileArtifactService(root_dir=Path("./artifacts"))

runner = Runner(
    app_name="my_app",
    agent=my_agent,
    artifact_service=artifact_service
)

# Artifacts will be stored in the local filesystem at ./artifacts/
```

## Live Streaming and Bidirectional Communication

### Creating a Live Streaming Agent

```python
from google.adk import Agent
from google.genai import types

# Create agent with live streaming model for real-time audio/video
live_agent = Agent(
    name='live_assistant',
    model='gemini-2.5-flash-native-audio-preview-09-2025',
    description='Live streaming agent that supports real-time audio/video interaction.',
    instruction='You are a helpful assistant that responds in real-time to user queries.',
    generate_content_config=types.GenerateContentConfig(
        safety_settings=[
            types.SafetySetting(
                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=types.HarmBlockThreshold.OFF,
            ),
        ]
    )
)

# Start live streaming session through ADK Web UI
# Click the Audio or Video icon to begin streaming
# The agent will respond in real-time to voice/video input
```

### Interactions API for Long-Running Conversations

```python
from google.adk import Agent
from google.adk.models import Gemini

# Create agent using Gemini 3 with Interactions API enabled
interactions_agent = Agent(
    name="long_conversation_agent",
    model=Gemini(
        model="gemini-3-pro-preview",
        use_interactions_api=True  # Enable Interactions API
    ),
    description="Agent for extended multi-turn conversations.",
    instruction="You are a helpful assistant for long-running conversations with memory."
)

# The Interactions API provides:
# - Extended conversation context
# - Improved memory across long dialogues
# - Better handling of complex multi-turn interactions
# - Optimized for sustained conversations
```

## CLI Commands

### Running Agents Locally

```bash
# Install ADK
pip install google-adk

# Run agent interactively
adk run path/to/agent

# Run with specific input file
adk run path/to/agent --input input.json

# Start development UI
adk web path/to/agent

# Start development UI with custom port
adk web path/to/agent --port 8080

# Use custom session backend
adk web path/to/agent --session-uri sqlite://sessions.db

# Use file-based artifacts
adk web path/to/agent --artifact-uri file:///path/to/artifacts
```

### Agent Evaluation

```bash
# Evaluate agent with test cases
adk eval path/to/agent path/to/evalset.json

# Evaluate with specific criteria
adk eval path/to/agent evalset.json --criteria response_match_score:0.8

# Generate evaluation report
adk eval path/to/agent evalset.json --output results.json

# Create a new eval set
adk eval create-set path/to/evalset.json

# Add an eval case to existing set
adk eval add-case path/to/evalset.json --query "What is 2+2?" --expected "4"
```

### Deployment

```bash
# Deploy to Cloud Run
adk deploy cloud-run path/to/agent \
  --project my-project \
  --region us-central1

# Deploy to Vertex AI Agent Engine
adk deploy agent-engine path/to/agent \
  --project my-project \
  --location us-central1 \
  --display-name "My Agent"

# Build Docker container
adk deploy docker path/to/agent \
  --output Dockerfile
```

## Evaluation Framework

### Defining Evaluation Cases

```python
from google.adk.evaluation import EvalCase
from google.genai import types

# Define evaluation test cases
eval_cases = [
    EvalCase(
        query=types.Content(role='user', parts=[types.Part(text="What is 2+2?")]),
        expected_response="4",
        expected_tool_calls=[]
    ),
    EvalCase(
        query=types.Content(role='user', parts=[types.Part(text="Search for Python tutorials")]),
        expected_tool_calls=["google_search"]
    )
]
```

### Running Evaluations Programmatically

```python
from google.adk import Agent
from google.adk.evaluation import Evaluator
from google.adk.sessions import InMemorySessionService

# Create agent to evaluate
agent = Agent(
    name="test_agent",
    model="gemini-2.5-flash",
    instruction="You are a helpful assistant."
)

# Initialize evaluator
evaluator = Evaluator(
    agent=agent,
    session_service=InMemorySessionService()
)

# Run evaluation
async def evaluate():
    results = await evaluator.evaluate(
        eval_cases=eval_cases,
        app_name="test_app"
    )

    for result in results:
        print(f"Case: {result.eval_case.query}")
        print(f"Score: {result.score}")
        print(f"Status: {result.status}")

    return results
```

## Authentication and Authorization

### OAuth2 Tool Authentication

```python
from google.adk import Agent
from google.adk.auth import AuthConfig, OAuth2AuthScheme
from google.adk.tools import RestAPITool, OpenAPIToolset

# Define OAuth2 configuration
oauth_config = OAuth2AuthScheme(
    client_id="your-client-id",
    client_secret="your-client-secret",
    authorization_url="https://provider.com/oauth/authorize",
    token_url="https://provider.com/oauth/token",
    scopes=["read", "write"]
)

# Create REST API tool with authentication
api_tool = RestAPITool(
    name="secure_api",
    openapi_spec_url="https://api.example.com/openapi.json",
    auth_config=AuthConfig(scheme=oauth_config)
)

# Or use custom header provider for dynamic authentication
def custom_header_provider() -> dict[str, str]:
    """Provide custom headers dynamically for each request."""
    return {
        "Authorization": f"Bearer {get_dynamic_token()}",
        "X-Custom-Header": "custom-value"
    }

openapi_toolset = OpenAPIToolset(
    openapi_spec_url="https://api.example.com/openapi.json",
    header_provider=custom_header_provider
)

# Create agent with authenticated tool
secure_agent = Agent(
    name="secure_agent",
    model="gemini-2.5-flash",
    instruction="Use the secure API to access protected resources.",
    tools=[api_tool]
)
```

## Advanced Features

### Context Caching

```python
from google.adk import Agent
from google.adk.agents import ContextCacheConfig
from google.adk.apps import App
from google.genai import types

# Create agent with static instruction for caching
agent = Agent(
    name="cached_agent",
    model="gemini-2.5-flash",
    static_instruction=types.Content(
        parts=[types.Part(text="You are an expert in Python programming. " * 100)]
    ),
    instruction="Answer Python programming questions."
)

# Configure context caching at app level
app = App(
    name="cached_app",
    root_agent=agent,
    context_cache_config=ContextCacheConfig(
        enable_auto_caching=True,
        ttl_seconds=3600
    )
)
```

### Human-in-the-Loop Tool Confirmation

```python
from google.adk import Agent
from google.adk.tools import FunctionTool
from google.adk.tools.tool_configs import ToolConfig, ConfirmationConfig

def delete_file(path: str) -> str:
    """Delete a file from the system."""
    import os
    os.remove(path)
    return f"Deleted {path}"

# Create tool with confirmation required
delete_tool = FunctionTool(
    func=delete_file,
    config=ToolConfig(
        confirmation=ConfirmationConfig(
            require_confirmation=True,
            confirmation_prompt="Are you sure you want to delete this file?"
        )
    )
)

# Agent will pause for user confirmation before executing
safe_agent = Agent(
    name="safe_agent",
    model="gemini-2.5-flash",
    instruction="Help manage files safely.",
    tools=[delete_tool]
)
```

### Agent Resumability for Long-Running Tasks

```python
from google.adk.apps import App, ResumabilityConfig
from google.adk import Agent
from google.adk.tools import LongRunningFunctionTool

async def long_computation(data: str) -> str:
    """Perform a long-running computation."""
    import asyncio
    await asyncio.sleep(300)  # Simulates 5-minute task
    return f"Processed: {data}"

# Create long-running tool
compute_tool = LongRunningFunctionTool(func=long_computation)

# Create agent
agent = Agent(
    name="compute_agent",
    model="gemini-2.5-flash",
    instruction="Execute long computations.",
    tools=[compute_tool]
)

# Enable resumability
app = App(
    name="resumable_app",
    root_agent=agent,
    resumability_config=ResumabilityConfig(is_resumable=True)
)

# The invocation will pause during long-running tool execution
# and can be resumed after completion
```

## Summary

Google ADK provides a comprehensive framework for building production-ready AI agents with enterprise features. The library's main strengths lie in its code-first approach to agent development, extensive tool ecosystem including MCP (Model Context Protocol) integration for interoperability with external services, OpenAPI and API Registry toolsets for API integration, flexible multi-agent orchestration patterns, and robust session management with multiple backend options (in-memory, SQLite, PostgreSQL, Vertex AI) including rewind capabilities. Developers can start with simple single-agent applications and scale to complex multi-agent systems with minimal code changes. The framework handles the complexity of state management, tool execution, authentication, and deployment, allowing teams to focus on agent logic and user experience.

Integration patterns typically involve defining agents with specific capabilities through tools and instructions, composing them into hierarchies or workflows using orchestration agents (LlmAgent, SequentialAgent, ParallelAgent, LoopAgent), managing conversation state through pluggable session services with support for rewinding to earlier states, and deploying to cloud infrastructure using CLI commands. ADK's compatibility with the Agent2Agent (A2A) protocol enables remote agent communication, while built-in evaluation frameworks and observability tools support testing and monitoring throughout the development lifecycle. Recent features include Interactions API for extended multi-turn conversations with Gemini 3 models, computer use tools for desktop automation, enhanced database support (Spanner, Bigtable) alongside BigQuery, API Registry integration for discovering and using registered APIs, multiple code execution environments (built-in, sandbox, container, GKE, Vertex AI), custom service registration for extensible backends, dynamic header providers for flexible API authentication, file-based artifact storage, and live streaming for real-time audio/video interactions. Whether building a simple chatbot, a data analysis assistant with database access, a desktop automation agent, or a complex multi-agent orchestration system, ADK provides the primitives and patterns needed for scalable, maintainable agent applications with the latest Gemini 2.5, Gemini 3, and other supported models (Claude, LiteLLM, Gemma).
