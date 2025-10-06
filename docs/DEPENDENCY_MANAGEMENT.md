# Dependency Management Guide

This document explains how dependencies are managed in the AIPC ADK Agents repository.

## Architecture

This project uses a **UV workspace architecture** with isolated agent dependencies:

```
AIPC-ADK-Agents/
├── pyproject.toml          # Core dependencies (Google ADK, etc.)
├── uv.toml                 # Workspace configuration
└── agents/
    ├── agent-1/
    │   └── pyproject.toml  # Agent-1 specific dependencies
    ├── agent-2/
    │   └── pyproject.toml  # Agent-2 specific dependencies
    └── agent-3/
        └── pyproject.toml  # Agent-3 specific dependencies
```

## Benefits

✅ **Isolation**: Each agent has its own dependencies  
✅ **No Conflicts**: Agents can use different versions of the same package  
✅ **Clarity**: Easy to see what each agent needs  
✅ **Maintainability**: Changes to one agent don't affect others  
✅ **Scalability**: Easy to add new agents without dependency bloat  

## How It Works

### Root Project (`pyproject.toml`)

Contains **only** dependencies needed by all or most agents:

```toml
dependencies = [
    "google-adk>=1.15.1",
    "google-genai>=1.41.0",
    "typing-extensions>=4.15.0",
]
```

### Agent Projects (`agents/*/pyproject.toml`)

Each agent declares **only** its specific dependencies:

```toml
[project]
name = "weather-agent"
version = "0.1.0"
requires-python = ">=3.12.0"

dependencies = [
    "requests>=2.31.0",      # For API calls
    "python-dotenv>=1.0.0",  # For config
]
```

### Workspace Configuration (`uv.toml`)

Tells UV which agents are part of the workspace:

```toml
[workspace]
members = [
    "agents/todo-list",
    "agents/life-agent",
    "agents/chore-organizer",
    # ... other agents
]
```

## Usage Examples

### For Users: Installing Dependencies

```bash
# Clone the repo
git clone https://github.com/ai-pilipinas-cebu/AIPC-ADK-Agents.git
cd AIPC-ADK-Agents

# Install all dependencies (root + all agents)
uv sync

# Install only core dependencies (no agents)
uv sync --no-workspace

# Install specific agent
cd agents/todo-list/
uv sync
```

### For Contributors: Adding Dependencies

#### Adding to Your Agent

```bash
# Navigate to your agent
cd agents/your-agent-name/

# Add a dependency
uv add requests

# Add with version constraint
uv add "sqlalchemy>=2.0.0,<3.0.0"

# Add a dev dependency
uv add --dev pytest-mock
```

This updates `agents/your-agent-name/pyproject.toml`:

```toml
dependencies = [
    "requests>=2.31.0",
    "sqlalchemy>=2.0.0,<3.0.0",
]

[tool.uv]
dev-dependencies = [
    "pytest-mock>=3.12.0",
]
```

#### Adding to Core (Rare)

Only add to root if needed by **all or most agents**:

```bash
# From root directory
cd /path/to/AIPC-ADK-Agents
uv add package-name
```

⚠️ **Warning**: This affects all agents. Use sparingly!

### For Maintainers: Managing Workspace

#### Adding a New Agent to Workspace

1. Create agent with `pyproject.toml`:
   ```bash
   mkdir -p agents/new-agent
   cd agents/new-agent
   uv init --name new-agent --no-readme
   ```

2. Add to workspace in `uv.toml`:
   ```toml
   [workspace]
   members = [
       "agents/todo-list",
       "agents/new-agent",  # Add this line
   ]
   ```

3. Sync workspace:
   ```bash
   cd ../..
   uv sync
   ```

#### Removing an Agent from Workspace

1. Remove from `uv.toml`:
   ```toml
   [workspace]
   members = [
       # "agents/old-agent",  # Remove or comment out
   ]
   ```

2. Sync workspace:
   ```bash
   uv sync
   ```

## Common Scenarios

### Scenario 1: Creating a New Agent

```bash
# 1. Create agent directory
mkdir -p agents/my-agent
cd agents/my-agent

# 2. Initialize with uv
uv init --name my-agent --no-readme

# 3. Add agent-specific dependencies
uv add requests
uv add python-dotenv

# 4. Add to workspace (edit uv.toml in root)
# 5. Sync from root
cd ../..
uv sync
```

### Scenario 2: Agent Needs a Specific Package Version

```bash
cd agents/my-agent

# Add specific version
uv add "pandas>=2.0.0,<2.1.0"

# Or exact version
uv add "pandas==2.0.3"
```

### Scenario 3: Two Agents Need Different Versions

**Agent A** needs `requests>=2.28.0`:
```bash
cd agents/agent-a
uv add "requests>=2.28.0,<3.0.0"
```

**Agent B** needs `requests>=2.31.0`:
```bash
cd agents/agent-b
uv add "requests>=2.31.0,<3.0.0"
```

✅ **No conflict!** Each agent gets its required version.

### Scenario 4: Updating All Dependencies

```bash
# Update all (root + all agents)
uv sync --upgrade

# Update specific agent
cd agents/my-agent
uv sync --upgrade
```

### Scenario 5: Checking What's Installed

```bash
# View all packages
uv pip list

# View agent-specific packages
cd agents/my-agent
uv pip list

# View dependency tree
uv pip tree
```

## Best Practices

### ✅ DO

- Add dependencies to agent's `pyproject.toml` when only that agent needs it
- Use version constraints (e.g., `>=2.0.0,<3.0.0`)
- Document why each dependency is needed in agent's README
- Test your agent with only its declared dependencies
- Keep dependencies minimal

### ❌ DON'T

- Add agent-specific dependencies to root `pyproject.toml`
- Use unpinned versions (e.g., `requests` without version)
- Add dependencies "just in case"
- Forget to update `uv.toml` when adding new agents
- Mix development and runtime dependencies

## Troubleshooting

### Issue: "Package not found"

```bash
# Make sure you're in the right directory
cd agents/your-agent-name/

# Sync dependencies
uv sync

# Check if package is in pyproject.toml
cat pyproject.toml
```

### Issue: "Conflicting dependencies"

This shouldn't happen with workspace architecture, but if it does:

```bash
# Clear cache
uv cache clean

# Re-sync
uv sync
```

### Issue: "Agent not in workspace"

Check `uv.toml` and ensure your agent is listed:

```toml
[workspace]
members = [
    "agents/your-agent-name",  # Should be here
]
```

### Issue: "Wrong Python version"

```bash
# Check Python version
python --version

# Should be 3.12.0 (from .python-version)
# If not, install Python 3.12 and try again
```

## Migration Guide

### Migrating Existing Agents

If you have an agent without `pyproject.toml`:

1. **Create `pyproject.toml`**:
   ```bash
   cd agents/your-agent-name
   uv init --name your-agent-name --no-readme
   ```

2. **Add dependencies**:
   ```bash
   # Add each dependency your agent uses
   uv add package-name
   ```

3. **Add to workspace**:
   Edit `uv.toml` in root and add your agent.

4. **Test**:
   ```bash
   uv sync
   python -m agents.your_agent_name.agent
   ```

## Resources

- [Main README](../README.md)
- [Contributing Guide](CONTRIBUTING.md)
- [Quick Start](QUICK_START.md)
- [UV Documentation](https://docs.astral.sh/uv/)
- [UV Workspaces](https://docs.astral.sh/uv/concepts/workspaces/)
- [Python Packaging Guide](https://packaging.python.org/)

## Questions?

- Open an [Issue](https://github.com/ai-pilipinas-cebu/AIPC-ADK-Agents/issues)
- Start a [Discussion](https://github.com/ai-pilipinas-cebu/AIPC-ADK-Agents/discussions)

---

**Last Updated**: October 2025  
**Maintained by**: AI Pilipinas Cebu Community
