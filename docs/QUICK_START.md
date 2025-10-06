# Quick Start Guide

Get up and running with AIPC ADK Agents in 5 minutes! ⚡

## Prerequisites

- **Python 3.12+**
- **Git**

## Step 1: Install UV

UV is a fast Python package manager. Install it:

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or with pip
pip install uv
```

Verify installation:
```bash
uv --version
```

## Step 2: Clone the Repository

```bash
git clone https://github.com/ai-pilipinas-cebu/AIPC-ADK-Agents.git
cd AIPC-ADK-Agents
```

## Step 3: Install Dependencies

```bash
# Install all dependencies (core + all agents)
uv sync
```

This will:
- Create a virtual environment (`.venv`)
- Install core dependencies
- Install all agent-specific dependencies
- Take ~30 seconds

## Step 4: Set Up Environment Variables

```bash
# Copy the example env file
cp .env.example .env

# Edit .env and add your API key
# Get your key from: https://aistudio.google.com/app/apikey
```

Edit `.env`:
```bash
GOOGLE_API_KEY=your_actual_api_key_here
```

## Step 5: Activate Virtual Environment

```bash
# macOS/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

You should see `(.venv)` in your terminal prompt.

## Step 6: Run an Agent

Try running the todo-list agent:

```bash
python -m agents.todo_list.agent
```

Or the life agent:

```bash
python -m agents.life_agent.agent
```

## Next Steps

### Explore Agents

Check out the available agents:

```bash
ls agents/
```

Each agent has its own README with usage instructions.

### Create Your Own Agent

```bash
# Create a new agent directory
mkdir -p agents/my-agent
cd agents/my-agent

# Initialize with uv
uv init --name my-agent --no-readme

# Add dependencies
uv add requests

# Create your agent files
touch __init__.py agent.py prompt.py README.md
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed instructions.

### Add Dependencies

```bash
# For your agent
cd agents/my-agent
uv add package-name

# For core project (affects all agents)
cd ../..
uv add package-name
```

See [DEPENDENCY_MANAGEMENT.md](DEPENDENCY_MANAGEMENT.md) for details.

## Common Commands

```bash
# Install dependencies
uv sync

# Add a package
uv add package-name

# Remove a package
uv remove package-name

# Update dependencies
uv sync --upgrade

# Run tests
uv run pytest

# Format code
uv run black .

# Lint code
uv run ruff check .
```

## Troubleshooting

### "uv: command not found"

UV is not installed or not in PATH. Reinstall:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then restart your terminal.

### "Python 3.12 not found"

Install Python 3.12:
```bash
# macOS (with Homebrew)
brew install python@3.12

# Ubuntu/Debian
sudo apt install python3.12

# Windows
# Download from python.org
```

### "GOOGLE_API_KEY not set"

Create `.env` file:
```bash
cp .env.example .env
# Edit .env and add your API key
```

### "Module not found"

Make sure you've installed dependencies:
```bash
uv sync
```

And activated the virtual environment:
```bash
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

## Getting Help

- 📚 [Full Documentation](../README.md)
- 🤝 [Contributing Guide](CONTRIBUTING.md)
- 📦 [Dependency Management](DEPENDENCY_MANAGEMENT.md)
- 🐛 [Report Issues](https://github.com/ai-pilipinas-cebu/AIPC-ADK-Agents/issues)
- 💬 [Discussions](https://github.com/ai-pilipinas-cebu/AIPC-ADK-Agents/discussions)

---

**Ready to build?** Start with [CONTRIBUTING.md](CONTRIBUTING.md)!

**Built with ❤️ by the AI Pilipinas Cebu Community**
