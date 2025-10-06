# 🤖 AI Pilipinas Cebu — Agent Collection

Welcome to the **AI Pilipinas Cebu Agent Collection** — a community-driven repository where we build, share, and collaborate on AI agents to solve real-world problems.

Whether you're exploring agents with the [Google Agent Development Kit (ADK)](https://github.com/google/agent-development-kit), building something cool with LangChain, or just experimenting with your own ideas — this is the place for you.  

> 🌟 Our goal is to **empower Filipinos** to explore agentic AI and contribute to a shared ecosystem of smart, useful, and innovative agents.

---

## 🧠 Why This Repo Exists

- 🤝 **Collaboration** — We believe in building together.
- 🇵🇭 **Community-first** — Agents built by Filipinos, for Filipinos.
- 🔄 **Reusability** — Don't start from scratch. Learn from and build upon what others have done.

---

## 🚀 Quick Start

> ⚡ **New here?** Check out [QUICK_START.md](docs/QUICK_START.md) for a 5-minute setup guide!

### Prerequisites

- **Python 3.12+** (specified in `.python-version`)
- **[uv](https://docs.astral.sh/uv/)** - Fast Python package manager

### Installation

1. **Install uv** (if you haven't already):
   ```bash
   # macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # Windows
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   
   # Or with pip
   pip install uv
   ```

2. **Clone the repository**:
   ```bash
   git clone https://github.com/ai-pilipinas-cebu/AIPC-ADK-Agents.git
   cd AIPC-ADK-Agents
   ```

3. **Set up the environment**:
   ```bash
   # uv will automatically use the Python version from .python-version
   uv sync
   ```

   This will:
   - Create a virtual environment (`.venv`)
   - Install all dependencies from `pyproject.toml`
   - Install development dependencies

4. **Activate the virtual environment**:
   ```bash
   # macOS/Linux
   source .venv/bin/activate
   
   # Windows
   .venv\Scripts\activate
   ```

5. **Set up your environment variables**:
   ```bash
   # Create .env file and add your API keys
   # Get your Google API key from: https://aistudio.google.com/app/apikey
   echo "GOOGLE_API_KEY=your_api_key_here" > .env
   ```

### Running an Agent

Each agent has its own directory under `agents/`. To run an agent:

```bash
# Example: Run the todo-list agent
python -m agents.todo_list.agent

# Example: Run the life-agent
python -m agents.life_agent.agent
```

Check each agent's `README.md` for specific usage instructions.

---

## 📦 Managing Dependencies

### Architecture Overview

This project uses a **workspace-based architecture** where:
- **Root project** (`pyproject.toml`) contains only core dependencies (Google ADK, etc.)
- **Each agent** has its own `pyproject.toml` for agent-specific dependencies
- This keeps agents **isolated and independent**

> 📖 **Detailed Guide**: See [DEPENDENCY_MANAGEMENT.md](docs/DEPENDENCY_MANAGEMENT.md) for comprehensive documentation

### Working with Core Dependencies

To add dependencies used across all agents:

```bash
# Add to root project
uv add package-name

# Add a development dependency
uv add --dev package-name
```

### Working with Agent-Specific Dependencies

Each agent manages its own dependencies independently:

```bash
# Navigate to the agent directory
cd agents/your-agent-name/

# Add a dependency for this agent only
uv add package-name

# Add with version constraint
uv add "requests>=2.31.0"

# Add a dev dependency for this agent
uv add --dev pytest-mock
```

**Example**: If your `todo-list` agent needs `sqlalchemy`, only add it to `agents/todo-list/pyproject.toml`:

```bash
cd agents/todo-list/
uv add sqlalchemy
```

### Installing All Dependencies

```bash
# From root: Install core + all agent dependencies
uv sync

# Install only core dependencies
uv sync --no-workspace

# Install specific agent dependencies
cd agents/your-agent-name/
uv sync
```

### Removing Dependencies

```bash
# Remove from root project
uv remove package-name

# Remove from specific agent
cd agents/your-agent-name/
uv remove package-name
```

### Updating Dependencies

```bash
# Update all dependencies (root + all agents)
uv sync --upgrade

# Update specific agent dependencies
cd agents/your-agent-name/
uv sync --upgrade
```

### Viewing Installed Packages

```bash
# View all installed packages
uv pip list

# View packages for specific agent
cd agents/your-agent-name/
uv pip list
```

---

## 🛠️ Development

### Code Quality Tools

This project uses several tools to maintain code quality:

- **Black** - Code formatter
- **Ruff** - Fast Python linter
- **MyPy** - Static type checker
- **Pytest** - Testing framework

### Running Tests

```bash
# Run all tests
uv run pytest

# Run tests with coverage
uv run pytest --cov

# Run specific test file
uv run pytest tests/test_specific.py
```

### Code Formatting

```bash
# Format code with Black
uv run black .

# Check formatting without changes
uv run black --check .
```

### Linting

```bash
# Run Ruff linter
uv run ruff check .

# Auto-fix issues
uv run ruff check --fix .
```

### Type Checking

```bash
# Run MyPy type checker
uv run mypy .
```

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](docs/CONTRIBUTING.md) for detailed guidelines.

### Quick Contribution Guide

1. **Fork this repo**
2. **Create a new branch**:
   ```bash
   git checkout -b feature/your-agent-name
   ```
3. **Add your agent** under `agents/your-agent-name/`:
   ```
   agents/your-agent-name/
   ├── README.md          # Agent documentation
   ├── __init__.py
   ├── agent.py           # Main agent code
   ├── prompt.py          # Agent prompts (if applicable)
   ├── tools/             # Custom tools (if applicable)
   │   ├── __init__.py
   │   └── your_tool.py
   └── sub_agents/        # Sub-agents (if applicable)
   ```
4. **Include a clear `README.md`** in your agent folder explaining:
   - What it does
   - How to use it
   - Any special requirements
   - Example usage
5. **Test your agent**:
   ```bash
   uv run pytest tests/
   uv run ruff check .
   uv run black --check .
   ```
6. **Submit a Pull Request**!

---

## 📚 Available Agents

### 🏠 Chore Organizer
**Location**: `agents/chore-organizer/`

An intelligent chore organization system that helps you manage household tasks efficiently.

### 🎯 Todo List Agent
**Location**: `agents/todo-list/`

A simple but powerful todo list manager with add, update, delete, and complete functionality.

### 🌟 Life Agent
**Location**: `agents/life-agent/`

Your personal life assistant that provides daily quotes, mood checks, and fun facts.

### 🤖 Automation Analyst
**Location**: `agents/automation_analyst/`

Analyzes job roles and identifies automation opportunities.

### 📄 Contract Analyzer
**Location**: `agents/contract-analyzer/`

Analyzes contracts and extracts key information.

> 💡 **Tip**: Check each agent's `README.md` for detailed documentation and usage examples.

---

## 🔧 Project Structure

```
AIPC-ADK-Agents/
├── agents/                 # All agents live here
│   ├── agent-name/
│   │   ├── README.md      # Agent-specific documentation
│   │   ├── agent.py       # Main agent implementation
│   │   ├── prompt.py      # Agent prompts
│   │   ├── tools/         # Custom tools
│   │   └── sub_agents/    # Sub-agents (if any)
│   └── ...
├── pyproject.toml         # Project dependencies and config
├── .python-version        # Python version specification
├── .gitignore            # Git ignore rules
├── README.md             # This file
└── CONTRIBUTING.md       # Contribution guidelines
```

---

## 📖 Documentation

Comprehensive documentation is available in the [`docs/`](docs/) folder:

- **[Quick Start Guide](docs/QUICK_START.md)** - Get started in 5 minutes
- **[Contributing Guide](docs/CONTRIBUTING.md)** - How to contribute
- **[Dependency Management](docs/DEPENDENCY_MANAGEMENT.md)** - Managing dependencies
- **[Project Structure](docs/PROJECT_STRUCTURE.md)** - Understanding the codebase
- **[Migration Summary](docs/MIGRATION_SUMMARY.md)** - UV migration details

---

## 💬 Community

### Get Help
- 🐛 **Found a bug?** [Open an issue](https://github.com/ai-pilipinas-cebu/AIPC-ADK-Agents/issues)
- 💡 **Have an idea?** [Start a discussion](https://github.com/ai-pilipinas-cebu/AIPC-ADK-Agents/discussions)
- 🤝 **Want to collaborate?** Join our community discussions!

### Resources
- [Google ADK Documentation](https://github.com/google/agent-development-kit)
- [uv Documentation](https://docs.astral.sh/uv/)
- [Python 3.12 Documentation](https://docs.python.org/3.12/)

---

## 📝 License

MIT License - feel free to use, modify, and distribute as you see fit.

---

**Built with ❤️ by the AI Pilipinas Cebu Community**
