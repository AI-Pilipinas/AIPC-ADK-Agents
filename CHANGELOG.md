# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **Pre-commit hooks** - Automated code quality checks before commits
- **Commitizen** - Conventional commit message helper
- **Makefile** - Convenient command shortcuts for common tasks
- **GitHub Templates** - Issue and PR templates for better contributions
- **CI/CD Workflow** - Automated testing and quality checks on GitHub Actions
- **Development Setup Guide** - Comprehensive development environment setup documentation
- **Quick Contributing Guide** - Fast-track guide for new contributors
- **Coverage reporting** - Test coverage tracking with pytest-cov
- **.gitignore** - Comprehensive gitignore configuration
- **Workspace configuration** - Moved from uv.toml to pyproject.toml (proper location)

### Changed
- **Updated README.md** - Enhanced contributing section with new tools and workflows
- **Enhanced pyproject.toml** - Added workspace config, commitizen, and coverage settings
- **Improved dev dependencies** - Added pre-commit, commitizen, and pytest-cov

### Removed
- **uv.toml** - Moved workspace configuration to pyproject.toml where it belongs

### Fixed
- **Workspace configuration error** - Resolved "workspace field not allowed in uv.toml" error

## [0.1.0] - 2024

### Added
- Initial project structure
- Todo List agent
- Life Agent with sub-agents (mood check, quote, fun fact)
- Chore Organizer agent
- Automation Analyst agent
- Contract Analyzer agent
- Personal Journal agent
- UV package manager integration
- Basic documentation (README, CONTRIBUTING, QUICK_START)

[Unreleased]: https://github.com/ai-pilipinas-cebu/AIPC-ADK-Agents/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/ai-pilipinas-cebu/AIPC-ADK-Agents/releases/tag/v0.1.0
