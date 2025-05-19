# AIPC ADK Agents

This directory contains example agents built with the Google Agent Development Kit (ADK). These agents demonstrate how to create functional AI assistants for various purposes.

## What's Inside

- **life-agent/**: A personal assistant agent with multiple sub-agents to help with daily life tasks
  - Provides motivational quotes through a `quote_agent`
  - Performs mood checks with `mood_check_agent`
  - Shares interesting facts via `fun_fact_agent`

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Virtual environment management tool (venv, conda, etc.)
- Google ADK installed (`pip install google-adk`)

### Setting Up Your Environment

1. Create and activate a virtual environment:

   **Using venv (recommended):**
   ```bash
   # Create a virtual environment
   python -m venv .venv
   
   # Activate the virtual environment
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

2. Install the Google ADK:
   ```bash
   pip install google-adk
   ```

### Running an Agent

1. Navigate to the agent directory:
   ```
   cd <agent-name>
   ```

2. Run the agent:
   ```
   adk web
   ```

## Creating Your Own Agent

Each agent follows a similar structure:

1. Define a prompt in `prompts.py`
2. Create an Agent instance in a Python file
3. Optional: Add sub-agents for specialized functionality

## Directory Structure of Agents

Each agent displayed here is organized as follows:

```
├── agent-name
│   ├── agent_name/                       # Core Agent Code
│   │   ├── shared_libraries/             # Folder contains helper functions for tools
│   │   ├── sub_agents/                   # Folder for each sub agent
│   │   │   │   ├── tools/                # tools folder for the subagent
│   │   │   │   ├── agent.py              # core logic of the sub agent
│   │   │   │   └── prompt.py             # prompt of the subagent
│   │   │   └── ...                       # More sub-agents    
│   │   ├── __init__.py                   # Initializes the agent
│   │   ├── tools/                        # Contains the code for tools used by the router agent
│   │   ├── agent.py                      # Contains the core logic of the agent
│   │   ├── prompt.py                     # Contains the prompts for the agent
│   ├── .env.example                      # Store agent specific env variables
│   └── README.md                         # Provides an overview of the agent
```

### General Structure

The root of each agent resides in its own directory under `agents/`. For example, the `llm-auditor` agent is located in `agents/llm-auditor/`.

### Directory Breakdown

**agent_name/** (Core Agent Code):
- This directory contains the core logic of the agent.
- `shared_libraries/`: (Optional) Contains code that is shared among multiple sub-agents.
- `sub_agents/`: Contains the definitions and logic for sub-agents.
  - Each sub-agent has its own directory.
  - `tools/`: Contains any custom tools specific to the sub-agent.
  - `agent.py`: Defines the sub-agent's behavior, including its model, tools, and instructions.
  - `prompt.py`: Contains the prompts used to guide the sub-agent's behavior.
- `__init__.py`: An initialization file that imports the agent.py from the folder for marking the agent_name directory as a Python package.
- `tools/`: Contains any custom tools used by the main agent.
- `agent.py`: Defines the main agent's behavior, including its sub-agents, model, tools, and instructions.
- `prompt.py`: Contains the prompts used to guide the main agent's behavior.

**Note:** The initial folder name is with "-" between words whereas the core logic is stored in the folder with the same agent name but with "_" between words (e.g., `llm-auditor` vs `llm_auditor`). This is due to the project structure imposed by poetry.

**.env.example**
- An example file showing the environment variables required to run the agent.
- Users should copy this file to `.env` and fill in their specific values.

**README.md**
- Provides detailed documentation specific to the agent, including its purpose, setup instructions, usage examples, and customization options.

## Contributing

1. Create a new folder for your agent
2. Include a README explaining what the agent does
3. Ensure your code is well-documented
4. Submit a pull request