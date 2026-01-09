.PHONY: help install test lint format type-check pre-commit clean dev-setup

# Default target
help:
	@echo "🚀 AIPC ADK Agents - Development Commands"
	@echo ""
	@echo "Setup:"
	@echo "  make install        Install all dependencies"
	@echo "  make dev-setup      Complete development setup (install + pre-commit)"
	@echo ""
	@echo "Code Quality:"
	@echo "  make format         Format code with Black"
	@echo "  make lint           Lint code with Ruff (with auto-fix)"
	@echo "  make type-check     Run type checking with MyPy"
	@echo "  make pre-commit     Run all pre-commit hooks"
	@echo "  make check          Run all checks (format, lint, type-check, test)"
	@echo ""
	@echo "Testing:"
	@echo "  make test           Run all tests"
	@echo "  make test-cov       Run tests with coverage report"
	@echo ""
	@echo "Maintenance:"
	@echo "  make clean          Clean up cache and build files"
	@echo "  make update-deps    Update all dependencies"
	@echo ""
	@echo "Git:"
	@echo "  make commit         Interactive commit with Commitizen"
	@echo "  make verify         Verify development environment setup"

# Installation
install:
	@echo "📦 Installing dependencies..."
	uv sync

dev-setup: install
	@echo "🔧 Setting up development environment..."
	uv run pre-commit install
	uv run pre-commit install --hook-type commit-msg
	@echo "✅ Development setup complete!"
	@echo ""
	@echo "Next steps:"
	@echo "  1. Activate virtual environment: source .venv/bin/activate"
	@echo "  2. Start coding!"

# Code Quality
format:
	@echo "🎨 Formatting code with Black..."
	uv run black .

lint:
	@echo "🔍 Linting code with Ruff..."
	uv run ruff check --fix .

type-check:
	@echo "🔎 Running type checks with MyPy..."
	uv run mypy agents/ --ignore-missing-imports

pre-commit:
	@echo "🔄 Running pre-commit hooks..."
	uv run pre-commit run --all-files

check: format lint type-check test
	@echo "✅ All checks passed!"

# Testing
test:
	@echo "🧪 Running tests..."
	uv run pytest -v

test-cov:
	@echo "🧪 Running tests with coverage..."
	uv run pytest --cov=agents --cov-report=html --cov-report=term-missing

# Maintenance
clean:
	@echo "🧹 Cleaning up..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	rm -rf htmlcov/ .coverage 2>/dev/null || true
	@echo "✅ Cleanup complete!"

update-deps:
	@echo "📦 Updating dependencies..."
	uv sync --upgrade

# Git helpers
commit:
	@echo "💬 Creating commit with Commitizen..."
	uv run cz commit

# Verification
verify:
	@echo "🔍 Verifying development environment..."
	python scripts/verify_setup.py
