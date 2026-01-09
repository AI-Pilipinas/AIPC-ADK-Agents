# Development Setup Guide

This guide will help you set up your development environment for contributing to AIPC ADK Agents.

## 🚀 Quick Start

The fastest way to get started:

```bash
# Clone the repository
git clone https://github.com/ai-pilipinas-cebu/AIPC-ADK-Agents.git
cd AIPC-ADK-Agents

# Run the automated setup
make dev-setup

# Activate the virtual environment
source .venv/bin/activate

# Verify your setup (optional but recommended)
python scripts/verify_setup.py
```

That's it! You're ready to start developing.

---

## 📋 Prerequisites

Before you begin, ensure you have:

- **Python 3.12+** - [Download](https://www.python.org/downloads/)
- **uv** - Fast Python package manager
  ```bash
  # macOS/Linux
  curl -LsSf https://astral.sh/uv/install.sh | sh

  # Windows
  powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```
- **Git** - [Download](https://git-scm.com/downloads)
- **Make** (optional, but recommended)
  - macOS: Already installed
  - Linux: `sudo apt install build-essential`
  - Windows: Use [WSL](https://docs.microsoft.com/en-us/windows/wsl/) or [Git Bash](https://gitforwindows.org/)

---

## 🛠️ Manual Setup

If you prefer a step-by-step setup:

### 1. Clone the Repository

```bash
# Fork the repo on GitHub first, then:
git clone https://github.com/YOUR_USERNAME/AIPC-ADK-Agents.git
cd AIPC-ADK-Agents

# Add upstream remote
git remote add upstream https://github.com/ai-pilipinas-cebu/AIPC-ADK-Agents.git
```

### 2. Install Dependencies

```bash
# Install all dependencies (root + all agent workspaces)
uv sync

# Activate the virtual environment
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate     # Windows
```

### 3. Install Pre-commit Hooks

Pre-commit hooks automatically check your code before each commit:

```bash
# Install pre-commit
uv run pre-commit install

# Install commit message hook (for conventional commits)
uv run pre-commit install --hook-type commit-msg

# Test the hooks (optional)
uv run pre-commit run --all-files
```

---

## 🧰 Development Tools

### Available Make Commands

If you have `make` installed, you can use these convenient commands:

```bash
# Setup
make install        # Install all dependencies
make dev-setup      # Complete setup (install + pre-commit)

# Code Quality
make format         # Format code with Black
make lint           # Lint code with Ruff
make type-check     # Run type checking with MyPy
make pre-commit     # Run all pre-commit hooks
make check          # Run all checks (format, lint, type, test)

# Testing
make test           # Run all tests
make test-cov       # Run tests with coverage report

# Maintenance
make clean          # Clean cache and build files
make update-deps    # Update all dependencies

# Git
make commit         # Interactive commit with Commitizen
```

View all available commands:
```bash
make help
```

### Manual Commands (without Make)

If you don't have `make`, you can run the commands directly:

```bash
# Install dependencies
uv sync

# Format code
uv run black .

# Lint code
uv run ruff check --fix .

# Type check
uv run mypy agents/ --ignore-missing-imports

# Run tests
uv run pytest -v

# Run tests with coverage
uv run pytest --cov=agents --cov-report=html

# Run all pre-commit hooks
uv run pre-commit run --all-files

# Interactive commit
uv run cz commit

# Clean up
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
```

---

## 🔍 Understanding the Tools

### Black - Code Formatting
Automatically formats your Python code to a consistent style.

**Configuration**: `[tool.black]` in `pyproject.toml`

```bash
# Format all code
make format
# or
uv run black .

# Check formatting without changing files
uv run black --check .
```

### Ruff - Fast Linting
Checks your code for common errors, style issues, and potential bugs.

**Configuration**: `[tool.ruff]` in `pyproject.toml`

```bash
# Lint and auto-fix
make lint
# or
uv run ruff check --fix .

# Check only (no fixes)
uv run ruff check .
```

### MyPy - Type Checking
Checks type hints to catch type-related bugs early.

**Configuration**: `[tool.mypy]` in `pyproject.toml`

```bash
# Run type checking
make type-check
# or
uv run mypy agents/ --ignore-missing-imports
```

### Pytest - Testing
Runs your test suite to ensure code works as expected.

**Configuration**: `[tool.pytest.ini_options]` in `pyproject.toml`

```bash
# Run all tests
make test
# or
uv run pytest -v

# Run with coverage
make test-cov
# or
uv run pytest --cov=agents --cov-report=html
```

### Pre-commit - Automated Checks
Runs checks automatically before each commit.

**Configuration**: `.pre-commit-config.yaml`

```bash
# Run manually
make pre-commit
# or
uv run pre-commit run --all-files

# Update hooks
uv run pre-commit autoupdate
```

### Commitizen - Conventional Commits
Helps you write consistent, semantic commit messages.

**Configuration**: `[tool.commitizen]` in `pyproject.toml`

```bash
# Interactive commit
make commit
# or
uv run cz commit

# Bump version (maintainers only)
uv run cz bump
```

---

## 🌳 Workspace Architecture

This project uses **uv workspaces** for managing multiple agents:

```
AIPC-ADK-Agents/                 # Root workspace
├── pyproject.toml               # Root config + workspace definition
├── agents/
│   ├── todo-list/
│   │   └── pyproject.toml       # Agent-specific dependencies
│   ├── life-agent/
│   │   └── pyproject.toml       # Agent-specific dependencies
│   └── ...
```

### Why Workspaces?

- **Isolation**: Each agent manages its own dependencies
- **No conflicts**: Agents can use different versions of packages
- **Easy testing**: Test agents independently
- **Better organization**: Clear separation of concerns

### Working with Workspaces

```bash
# Install ALL dependencies (root + all agents)
uv sync

# Install only root dependencies
uv sync --no-workspace

# Add dependency to root
uv add package-name

# Add dependency to specific agent
cd agents/your-agent/
uv add package-name

# Run command in specific agent context
cd agents/your-agent/
uv run python -m agent
```

---

## 🎨 Code Style Guidelines

### Python Style
- Follow [PEP 8](https://pep8.org/)
- Line length: 100 characters
- Use type hints where appropriate
- Write docstrings for functions and classes

### Commit Message Format
We use [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, etc.)
- `refactor:` - Code refactoring
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

**Examples**:
```bash
feat(todo-list): add priority sorting
fix(life-agent): resolve mood check error
docs(contributing): update setup instructions
```

### Using Commitizen

Instead of manual commits, use Commitizen for guided commit creation:

```bash
make commit
# or
uv run cz commit
```

This will:
1. Prompt you for commit type
2. Ask for scope (optional)
3. Request a short description
4. Allow longer description
5. Format everything correctly

---

## 🧪 Testing Your Changes

### Before Committing

Always run these checks before committing:

```bash
# Option 1: Run all checks at once
make check

# Option 2: Run checks individually
make format
make lint
make type-check
make test
```

### Pre-commit Hooks

Pre-commit hooks run automatically when you commit:

```bash
git add .
git commit -m "feat: your change"
# Hooks run automatically and may modify files
# If files are modified, you'll need to git add again
```

To skip hooks (not recommended):
```bash
git commit --no-verify -m "message"
```

### CI/CD

All pull requests automatically run checks on GitHub Actions:
- Code formatting (Black)
- Linting (Ruff)
- Type checking (MyPy)
- Tests (pytest)
- Multiple platforms (Ubuntu, macOS, Windows)

View workflow: `.github/workflows/ci.yml`

---

## 🔧 Troubleshooting

### uv command not found

Install uv:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Restart your terminal and try again.

### Pre-commit hooks failing

Update hooks:
```bash
uv run pre-commit autoupdate
uv run pre-commit install
```

Run manually to see details:
```bash
uv run pre-commit run --all-files --verbose
```

### Import errors

Make sure virtual environment is activated:
```bash
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

Reinstall dependencies:
```bash
uv sync
```

### Tests failing

Run tests in verbose mode:
```bash
uv run pytest -v -s
```

Check specific test:
```bash
uv run pytest tests/test_specific.py::test_function -v
```

### Type checking errors

MyPy can be strict. For now, it's set to not fail CI:
```bash
uv run mypy agents/ --ignore-missing-imports --no-error-summary
```

---

## 📚 Additional Resources

### Documentation
- [Contributing Guide](CONTRIBUTING.md)
- [Project Structure](PROJECT_STRUCTURE.md)
- [Dependency Management](DEPENDENCY_MANAGEMENT.md)

### External Resources
- [Google ADK Documentation](https://github.com/google/agent-development-kit)
- [uv Documentation](https://docs.astral.sh/uv/)
- [Pre-commit Documentation](https://pre-commit.com/)
- [Conventional Commits](https://www.conventionalcommits.org/)

---

## 🎯 Quick Reference

### First-time Setup
```bash
git clone https://github.com/YOUR_USERNAME/AIPC-ADK-Agents.git
cd AIPC-ADK-Agents
make dev-setup
source .venv/bin/activate
```

### Daily Development
```bash
# Before starting work
git pull upstream main
uv sync

# During development
make format
make lint
make test

# Before committing
make check
make commit  # Interactive commit
git push origin your-branch
```

### Creating a PR
1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make your changes
3. Run checks: `make check`
4. Commit: `make commit`
5. Push: `git push origin feature/your-feature`
6. Open PR on GitHub

---

## 🆘 Getting Help

- **Questions?** Open a [Discussion](https://github.com/ai-pilipinas-cebu/AIPC-ADK-Agents/discussions)
- **Found a bug?** Open an [Issue](https://github.com/ai-pilipinas-cebu/AIPC-ADK-Agents/issues)
- **Need help?** Ask in the community chat

**Happy coding!** 🚀
