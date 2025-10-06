# Contributing to AIPC ADK Agents

Thank you for your interest in contributing to the AI Pilipinas Cebu Agent Collection! 🎉

This document provides guidelines and instructions for contributing to this project.

---

## 🌟 Ways to Contribute

- **Add a new agent** - Build and share your own AI agent
- **Improve existing agents** - Enhance functionality, fix bugs, or improve documentation
- **Report bugs** - Help us identify issues
- **Suggest features** - Share ideas for new capabilities
- **Improve documentation** - Help make our docs clearer and more comprehensive

---

## 🚀 Getting Started

### 1. Set Up Your Development Environment

First, make sure you have the prerequisites installed:

- **Python 3.12+**
- **[uv](https://docs.astral.sh/uv/)** - Fast Python package manager
- **Git**

Then, fork and clone the repository:

```bash
# Fork the repo on GitHub first, then:
git clone https://github.com/YOUR_USERNAME/AIPC-ADK-Agents.git
cd AIPC-ADK-Agents

# Add upstream remote
git remote add upstream https://github.com/ai-pilipinas-cebu/AIPC-ADK-Agents.git
```

### 2. Install Dependencies

```bash
# Install all dependencies including dev tools
uv sync

# Activate the virtual environment
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate     # Windows
```

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
# or
git checkout -b agent/your-agent-name
```

---

## 📝 Creating a New Agent

### Agent Structure

Follow this standard structure for your agent:

```
agents/your-agent-name/
├── README.md              # Required: Agent documentation
├── pyproject.toml         # Required: Agent dependencies
├── __init__.py           # Required: Package initialization
├── agent.py              # Required: Main agent implementation
├── prompt.py             # Optional: Agent prompts/instructions
├── tools/                # Optional: Custom tools
│   ├── __init__.py
│   ├── tool1.py
│   └── tool2.py
└── sub_agents/           # Optional: Sub-agents
    ├── __init__.py
    ├── sub_agent1/
    │   ├── __init__.py
    │   ├── agent.py
    │   └── prompt.py
    └── sub_agent2/
        ├── __init__.py
        ├── agent.py
        └── prompt.py
```

### Agent Dependencies (pyproject.toml)

Each agent **must** have its own `pyproject.toml` file to manage dependencies independently:

```toml
[project]
name = "your-agent-name"
version = "0.1.0"
description = "Brief description of your agent"
requires-python = ">=3.12.0"

dependencies = [
    # Core dependencies are inherited from root project
    # Add only agent-specific dependencies here
    # Example: "requests>=2.31.0",
    # Example: "sqlalchemy>=2.0.0",
]

[tool.uv]
# Optional: Agent-specific development dependencies
dev-dependencies = [
    # Example: "pytest-mock>=3.12.0",
]
```

**Important**: 
- Only add dependencies that are **specific to your agent**
- Core dependencies (google-adk, google-genai) are already in the root project
- Keep dependencies minimal and well-documented

### Agent README Template

Your agent's `README.md` should include:

```markdown
# Agent Name

Brief description of what your agent does.

## Features

- Feature 1
- Feature 2
- Feature 3

## Prerequisites

- Any special requirements
- API keys needed
- External services

## Installation

```bash
# Any agent-specific setup
uv add additional-package
```

## Usage

```python
# Example code showing how to use your agent
from agents.your_agent_name.agent import root_agent

# Usage example
```

## Configuration

Explain any configuration needed (environment variables, etc.)

## Examples

Provide real-world examples of using your agent.

## Limitations

Any known limitations or constraints.

## Contributing

Contributions welcome! See [CONTRIBUTING.md](../docs/CONTRIBUTING.md).

## License

MIT
```

### Agent Code Template

Here's a basic template for `agent.py`:

```python
"""Brief description of your agent."""

from google.adk.agents import Agent
from .prompt import agent_prompt
# Import any tools or sub-agents

root_agent = Agent(
    name="your_agent_name",
    model="gemini-2.0-flash",  # or other supported models
    description="Brief description for the agent",
    instruction=agent_prompt,
    # Add tools if needed
    tools=[
        # your_tool1,
        # your_tool2,
    ],
    # Add sub-agents if needed
    sub_agents=[
        # sub_agent1,
        # sub_agent2,
    ]
)
```

### Prompt Template

Create a `prompt.py` file:

```python
"""Prompts and instructions for your agent."""

agent_prompt = """
You are [agent description].

Your responsibilities:
1. Responsibility 1
2. Responsibility 2
3. Responsibility 3

Guidelines:
- Guideline 1
- Guideline 2
- Guideline 3

Always [important behavior].
"""
```

---

## 🧪 Testing Your Agent

### Manual Testing

```bash
# Run your agent
python -m agents.your_agent_name.agent
```

### Writing Tests

Create tests in a `tests/` directory:

```python
# tests/test_your_agent.py
import pytest
from agents.your_agent_name.agent import root_agent

def test_agent_initialization():
    """Test that agent initializes correctly."""
    assert root_agent.name == "your_agent_name"
    assert root_agent.description is not None

@pytest.mark.asyncio
async def test_agent_response():
    """Test agent response."""
    # Add your test logic here
    pass
```

Run tests:

```bash
uv run pytest tests/test_your_agent.py -v
```

---

## 🎨 Code Quality

### Code Formatting

We use **Black** for consistent code formatting:

```bash
# Format your code
uv run black agents/your-agent-name/

# Check formatting
uv run black --check agents/your-agent-name/
```

### Linting

We use **Ruff** for fast linting:

```bash
# Check for issues
uv run ruff check agents/your-agent-name/

# Auto-fix issues
uv run ruff check --fix agents/your-agent-name/
```

### Type Checking

We use **MyPy** for type checking:

```bash
# Run type checker
uv run mypy agents/your-agent-name/
```

### Pre-commit Checklist

Before committing, ensure:

- [ ] Code is formatted with Black
- [ ] No linting errors from Ruff
- [ ] Type checking passes (if applicable)
- [ ] Tests pass
- [ ] Documentation is updated
- [ ] README.md is included in agent directory

```bash
# Run all checks
uv run black .
uv run ruff check --fix .
uv run mypy .
uv run pytest
```

---

## 📦 Managing Dependencies

### Understanding the Dependency Architecture

This project uses a **workspace architecture**:
- **Root `pyproject.toml`**: Contains core dependencies (Google ADK, etc.)
- **Agent `pyproject.toml`**: Each agent has its own for agent-specific dependencies
- **Benefits**: Agents are isolated, dependencies don't conflict, easier to maintain

### Adding Agent-Specific Dependencies

When your agent needs additional packages, add them to **your agent's** `pyproject.toml`:

```bash
# Navigate to your agent directory
cd agents/your-agent-name/

# Add a dependency for your agent only
uv add package-name

# Add with version constraint
uv add "requests>=2.31.0,<3.0.0"

# Add a development dependency for your agent
uv add --dev pytest-mock
```

**Example**: Your weather agent needs `requests`:

```bash
cd agents/weather-agent/
uv add requests
```

This adds `requests` to `agents/weather-agent/pyproject.toml` only, not to the root project.

### Adding Core Dependencies

Only add to root if the dependency is needed by **all or most agents**:

```bash
# From root directory
uv add package-name
```

**Think carefully** before adding to root - it affects all agents!

### Viewing Your Agent's Dependencies

```bash
cd agents/your-agent-name/
cat pyproject.toml  # View dependencies
uv pip list         # View installed packages
```

### Installing Dependencies

```bash
# Install all dependencies (root + all agents)
uv sync

# Install only your agent's dependencies
cd agents/your-agent-name/
uv sync
```

### Best Practices

1. **Keep it minimal** - Only add what you actually need
2. **Pin versions** - Use version constraints (e.g., `>=2.0.0,<3.0.0`)
3. **Document** - Explain why each dependency is needed in your README
4. **Test isolation** - Ensure your agent works with just its declared dependencies

---

## 🔄 Submitting Your Contribution

### 1. Commit Your Changes

Write clear, descriptive commit messages:

```bash
git add .
git commit -m "feat: add weather forecast agent"
# or
git commit -m "fix: resolve issue with todo list deletion"
# or
git commit -m "docs: update chore organizer README"
```

**Commit Message Format:**
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `refactor:` - Code refactoring
- `test:` - Adding tests
- `chore:` - Maintenance tasks

### 2. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 3. Create a Pull Request

1. Go to your fork on GitHub
2. Click "New Pull Request"
3. Select your branch
4. Fill in the PR template:

```markdown
## Description
Brief description of your changes

## Type of Change
- [ ] New agent
- [ ] Bug fix
- [ ] Feature enhancement
- [ ] Documentation update
- [ ] Code refactoring

## Agent Details (if applicable)
- **Agent Name**: your-agent-name
- **Purpose**: What does it do?
- **Key Features**: Main capabilities

## Testing
- [ ] Tested manually
- [ ] Added unit tests
- [ ] All tests pass

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No new warnings
- [ ] README.md included (for new agents)

## Screenshots/Examples (if applicable)
Add screenshots or example outputs
```

### 4. Code Review Process

- Maintainers will review your PR
- Address any feedback or requested changes
- Once approved, your PR will be merged!

---

## 🤝 Community Guidelines

### Code of Conduct

- **Be respectful** - Treat everyone with respect and kindness
- **Be collaborative** - Work together, share knowledge
- **Be constructive** - Provide helpful feedback
- **Be inclusive** - Welcome contributors of all skill levels

### Getting Help

- **Questions?** Open a [Discussion](https://github.com/ai-pilipinas-cebu/AIPC-ADK-Agents/discussions)
- **Found a bug?** Open an [Issue](https://github.com/ai-pilipinas-cebu/AIPC-ADK-Agents/issues)
- **Need clarification?** Comment on existing issues or PRs

---

## 📚 Resources

### Documentation
- [Google ADK Documentation](https://github.com/google/agent-development-kit)
- [uv Documentation](https://docs.astral.sh/uv/)
- [Python 3.12 Documentation](https://docs.python.org/3.12/)

### Example Agents
Look at existing agents in the `agents/` directory for inspiration:
- `agents/todo-list/` - Simple agent with tools
- `agents/life-agent/` - Agent with sub-agents
- `agents/chore-organizer/` - Complex agent with custom orchestration

### Coding Standards
- Follow [PEP 8](https://pep8.org/) style guide
- Use type hints where appropriate
- Write docstrings for functions and classes
- Keep functions focused and modular

---

## 🎯 Quick Reference

### Common Commands

```bash
# Setup
uv sync                          # Install dependencies
source .venv/bin/activate       # Activate venv

# Development
uv add package-name             # Add dependency
uv remove package-name          # Remove dependency
uv run pytest                   # Run tests
uv run black .                  # Format code
uv run ruff check .             # Lint code
uv run mypy .                   # Type check

# Git
git checkout -b feature/name    # Create branch
git add .                       # Stage changes
git commit -m "message"         # Commit
git push origin branch-name     # Push to fork
```

---

## 🙏 Thank You!

Your contributions help make this project better for everyone. We appreciate your time and effort!

**Happy coding!** 🚀

---

**Questions?** Feel free to reach out by opening an issue or starting a discussion.

**Built with ❤️ by the AI Pilipinas Cebu Community**
