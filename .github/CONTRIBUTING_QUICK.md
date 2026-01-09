# Quick Contributing Guide

**5-minute guide to start contributing!**

For comprehensive details, see [CONTRIBUTING.md](../docs/CONTRIBUTING.md).

## 🚀 Setup (One Time)

```bash
# 1. Fork the repo on GitHub
# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/AIPC-ADK-Agents.git
cd AIPC-ADK-Agents

# 3. Run automated setup
make dev-setup

# 4. Activate virtual environment
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

## 📝 Making Changes

```bash
# 1. Create a branch
git checkout -b feature/your-feature-name

# 2. Make your changes
# - Edit/create files
# - Add your agent in agents/your-agent/

# 3. Run checks
make check  # Formats, lints, type-checks, and tests

# 4. Commit changes
make commit  # Interactive commit helper
# or manually:
git add .
git commit -m "feat: your change description"

# 5. Push to your fork
git push origin feature/your-feature-name

# 6. Open Pull Request on GitHub
```

## ✅ Before Submitting PR

Make sure:
- [ ] `make check` passes
- [ ] Agent has README.md
- [ ] Tests added (if applicable)
- [ ] Commit messages follow convention (`feat:`, `fix:`, `docs:`)

## 🎯 Useful Commands

```bash
make help           # See all commands
make format         # Format code
make lint           # Lint code
make test           # Run tests
make check          # Run all checks
make commit         # Interactive commit
```

## 📚 More Information

- [Full Contributing Guide](../docs/CONTRIBUTING.md)
- [Development Setup](../docs/DEVELOPMENT_SETUP.md)
- [Project Structure](../docs/PROJECT_STRUCTURE.md)

## 🤝 Need Help?

- Open a [Discussion](https://github.com/ai-pilipinas-cebu/AIPC-ADK-Agents/discussions)
- Open an [Issue](https://github.com/ai-pilipinas-cebu/AIPC-ADK-Agents/issues)

**Happy coding!** 🚀
