# Project Structure

This document explains the organization and structure of the AIPC ADK Agents repository.

## Repository Layout

```
AIPC-ADK-Agents/
│
├── 📄 pyproject.toml              # Root project config & core dependencies
├── 📄 uv.toml                     # UV workspace configuration
├── 📄 .python-version             # Python version (3.12.0)
├── 📄 .gitignore                  # Git ignore rules
├── 📄 README.md                   # Main project documentation
│
├── 📚 docs/                       # Documentation folder
│   ├── README.md                  # Documentation index
│   ├── QUICK_START.md             # 5-minute setup guide
│   ├── CONTRIBUTING.md            # Contribution guidelines
│   ├── DEPENDENCY_MANAGEMENT.md   # Dependency architecture guide
│   ├── PROJECT_STRUCTURE.md       # This file
│   └── MIGRATION_SUMMARY.md       # UV migration summary
│
├── 🤖 agents/                     # All agents live here
│   │
│   ├── todo-list/                 # Todo list agent
│   │   ├── pyproject.toml         # Agent-specific dependencies
│   │   ├── README.md              # Agent documentation
│   │   ├── __init__.py
│   │   ├── agent.py               # Main agent code
│   │   ├── prompt.py              # Agent prompts
│   │   ├── data/                  # Agent data
│   │   │   └── todos.json
│   │   └── tools/                 # Agent tools
│   │       ├── __init__.py
│   │       ├── add_todo.py
│   │       ├── complete_todo.py
│   │       ├── delete_todo.py
│   │       ├── get_todos.py
│   │       └── update_todo.py
│   │
│   ├── life-agent/                # Life assistant agent
│   │   ├── pyproject.toml
│   │   ├── README.md
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   ├── prompt.py
│   │   └── sub_agents/            # Sub-agents
│   │       ├── __init__.py
│   │       ├── quote/
│   │       ├── mood_check/
│   │       └── fun_fact/
│   │
│   ├── chore-organizer/           # Chore organization agent
│   │   ├── pyproject.toml
│   │   ├── README.md
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   └── sub_agents/            # Complex sub-agent hierarchy
│   │       ├── chore_collector/
│   │       ├── priority_assigner/
│   │       ├── chore_balancer/
│   │       ├── plan_formatter/
│   │       └── process_sequencer/
│   │
│   ├── automation_analyst/        # Automation analysis agent
│   │   ├── pyproject.toml
│   │   ├── README.md
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   └── prompt.py
│   │
│   └── README.md                  # Agents overview
│
└── 🧪 tests/                      # Test directory (future)
    └── (test files)
```

## File Purposes

### Root Level Files

| File | Purpose |
|------|---------|
| `pyproject.toml` | Core project configuration and dependencies shared by all agents |
| `uv.toml` | UV workspace configuration defining which agents are members |
| `.python-version` | Specifies Python 3.12.0 for consistency |
| `.gitignore` | Defines files/directories to exclude from git |
| `README.md` | Main project documentation and setup instructions |
| `main.py` | Entry point (if needed) |

### Documentation Files (docs/)

| File | Purpose |
|------|---------|
| `README.md` | Documentation index and navigation |
| `QUICK_START.md` | Fast 5-minute setup guide for new users |
| `CONTRIBUTING.md` | Guidelines for contributors, code standards |
| `DEPENDENCY_MANAGEMENT.md` | Detailed dependency architecture explanation |
| `PROJECT_STRUCTURE.md` | This file - explains repository organization |
| `MIGRATION_SUMMARY.md` | Summary of UV migration changes |

### Agent Structure

Each agent follows this standard structure:

```
agents/agent-name/
├── pyproject.toml         # Agent-specific dependencies
├── README.md              # Agent documentation
├── __init__.py           # Package initialization
├── agent.py              # Main agent implementation
├── prompt.py             # Agent prompts/instructions (optional)
├── tools/                # Custom tools (optional)
│   ├── __init__.py
│   └── tool_name.py
└── sub_agents/           # Sub-agents (optional)
    ├── __init__.py
    └── sub_agent_name/
        ├── __init__.py
        ├── agent.py
        └── prompt.py
```

## Dependency Architecture

### Three-Level Hierarchy

1. **Root Level** (`pyproject.toml`)
   - Core dependencies (Google ADK, google-genai, typing-extensions)
   - Development tools (pytest, black, ruff, mypy)
   - Shared by all agents

2. **Agent Level** (`agents/*/pyproject.toml`)
   - Agent-specific dependencies
   - Isolated from other agents
   - Can use different versions of same package

3. **Workspace Level** (`uv.toml`)
   - Defines which agents are part of the workspace
   - Enables `uv sync` to install all at once

### Example Flow

```
User runs: uv sync
    ↓
UV reads: uv.toml (workspace members)
    ↓
UV installs:
    1. Root dependencies (pyproject.toml)
    2. todo-list dependencies (agents/todo-list/pyproject.toml)
    3. life-agent dependencies (agents/life-agent/pyproject.toml)
    4. ... (all workspace members)
    ↓
Result: .venv/ with all dependencies
```

## Agent Categories

### Simple Agents
- **todo-list**: Basic CRUD operations with tools
- **automation_analyst**: Single-agent analysis

### Multi-Agent Systems
- **life-agent**: Coordinator with 3 sub-agents
- **chore-organizer**: Complex hierarchy with 5+ sub-agents

### Specialized Agents
- **contract-analyzer**: Document processing (in development)
- **capital-agent**: Financial analysis (in development)

## Development Workflow

### Adding a New Agent

1. **Create directory structure**:
   ```bash
   mkdir -p agents/my-agent
   cd agents/my-agent
   ```

2. **Initialize with UV**:
   ```bash
   uv init --name my-agent --no-readme
   ```

3. **Create agent files**:
   ```bash
   touch __init__.py agent.py prompt.py README.md
   ```

4. **Add to workspace** (edit `uv.toml`):
   ```toml
   [workspace]
   members = [
       "agents/todo-list",
       "agents/my-agent",  # Add this
   ]
   ```

5. **Add dependencies**:
   ```bash
   uv add requests
   ```

6. **Implement agent**:
   - Write code in `agent.py`
   - Define prompts in `prompt.py`
   - Document in `README.md`

7. **Test**:
   ```bash
   cd ../..
   uv sync
   python -m agents.my_agent.agent
   ```

## Best Practices

### File Organization

✅ **DO**:
- Keep agent code in its own directory
- Use `__init__.py` for clean imports
- Separate prompts into `prompt.py`
- Document in agent's `README.md`
- Add agent-specific deps to agent's `pyproject.toml`

❌ **DON'T**:
- Mix agent code with other agents
- Put everything in one file
- Hardcode prompts in agent code
- Skip documentation
- Add agent deps to root `pyproject.toml`

### Naming Conventions

- **Directories**: `kebab-case` (e.g., `todo-list`, `life-agent`)
- **Python files**: `snake_case` (e.g., `agent.py`, `add_todo.py`)
- **Classes**: `PascalCase` (e.g., `TodoListAgent`)
- **Functions**: `snake_case` (e.g., `add_todo`, `get_todos`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `MAX_RETRIES`)

### Import Structure

```python
# Standard library
import json
import logging
from typing import AsyncGenerator

# Third-party
from google.adk.agents import Agent
from google.genai import types

# Local
from .prompt import agent_prompt
from .tools import add_todo, get_todos
```

## Testing Structure (Future)

```
tests/
├── __init__.py
├── conftest.py                    # Pytest configuration
├── test_agents/                   # Agent tests
│   ├── test_todo_list.py
│   ├── test_life_agent.py
│   └── test_chore_organizer.py
└── test_tools/                    # Tool tests
    └── test_todo_tools.py
```

## Configuration Files

### pyproject.toml (Root)

```toml
[project]
name = "aipc-adk-agents"
dependencies = [
    "google-adk>=1.15.1",
    "google-genai>=1.41.0",
]

[tool.uv]
dev-dependencies = [
    "pytest>=8.0.0",
    "black>=24.0.0",
    "ruff>=0.6.0",
]

[tool.black]
line-length = 100

[tool.ruff]
line-length = 100
```

### uv.toml

```toml
[workspace]
members = [
    "agents/todo-list",
    "agents/life-agent",
    "agents/chore-organizer",
    "agents/automation_analyst",
]
```

### .python-version

```
3.12.0
```

## Resources

- [Main README](../README.md) - Setup and usage
- [Quick Start](QUICK_START.md) - Fast setup
- [Contributing](CONTRIBUTING.md) - How to contribute
- [Dependencies](DEPENDENCY_MANAGEMENT.md) - Dependency management

---

**Questions?** Open an [issue](https://github.com/ai-pilipinas-cebu/AIPC-ADK-Agents/issues) or [discussion](https://github.com/ai-pilipinas-cebu/AIPC-ADK-Agents/discussions)!

**Built with ❤️ by the AI Pilipinas Cebu Community**
