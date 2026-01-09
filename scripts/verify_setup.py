#!/usr/bin/env python3
"""
Setup Verification Script

Run this script to verify your development environment is properly configured.
Usage: python scripts/verify_setup.py
"""

import subprocess
import sys
from pathlib import Path


def run_command(cmd: list[str]) -> tuple[bool, str]:
    """Run a command and return success status and output."""
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True, timeout=10)
        return True, result.stdout
    except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired) as e:
        return False, str(e)


def check_python_version() -> bool:
    """Check if Python version is 3.12+."""
    print("🐍 Checking Python version...", end=" ")
    version = sys.version_info
    if version.major == 3 and version.minor >= 12:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} (needs 3.12+)")
        return False


def check_uv_installed() -> bool:
    """Check if uv is installed."""
    print("📦 Checking uv installation...", end=" ")
    success, output = run_command(["uv", "--version"])
    if success:
        version = output.strip()
        print(f"✅ {version}")
        return True
    else:
        print("❌ Not installed")
        return False


def check_git_installed() -> bool:
    """Check if git is installed."""
    print("🔧 Checking git installation...", end=" ")
    success, output = run_command(["git", "--version"])
    if success:
        version = output.strip()
        print(f"✅ {version}")
        return True
    else:
        print("❌ Not installed")
        return False


def check_virtual_env() -> bool:
    """Check if virtual environment exists."""
    print("🌐 Checking virtual environment...", end=" ")
    venv_path = Path(".venv")
    if venv_path.exists() and venv_path.is_dir():
        print("✅ .venv exists")
        return True
    else:
        print("❌ .venv not found")
        return False


def check_dependencies_installed() -> bool:
    """Check if dependencies are installed."""
    print("📚 Checking dependencies...", end=" ")
    success, _ = run_command(["uv", "pip", "list"])
    if success:
        print("✅ Dependencies installed")
        return True
    else:
        print("❌ Dependencies not installed")
        return False


def check_pre_commit_installed() -> bool:
    """Check if pre-commit hooks are installed."""
    print("🪝 Checking pre-commit hooks...", end=" ")
    pre_commit_file = Path(".git/hooks/pre-commit")
    if pre_commit_file.exists():
        print("✅ Pre-commit hooks installed")
        return True
    else:
        print("⚠️  Pre-commit hooks not installed")
        return False


def check_required_files() -> bool:
    """Check if required project files exist."""
    print("📁 Checking required files...", end=" ")
    required_files = [
        "pyproject.toml",
        ".pre-commit-config.yaml",
        "Makefile",
        ".gitignore",
        "README.md",
        "docs/CONTRIBUTING.md",
        "docs/DEVELOPMENT_SETUP.md",
    ]

    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)

    if not missing_files:
        print(f"✅ All {len(required_files)} required files present")
        return True
    else:
        print(f"❌ Missing {len(missing_files)} files:")
        for file in missing_files:
            print(f"   - {file}")
        return False


def check_workspace_config() -> bool:
    """Check if workspace is properly configured."""
    print("🏢 Checking workspace configuration...", end=" ")
    uv_toml = Path("uv.toml")
    if uv_toml.exists():
        print("⚠️  uv.toml exists (should be removed)")
        return False

    pyproject = Path("pyproject.toml")
    if pyproject.exists():
        content = pyproject.read_text()
        if "[tool.uv.workspace]" in content:
            print("✅ Workspace configured in pyproject.toml")
            return True
        else:
            print("⚠️  Workspace config not found in pyproject.toml")
            return False
    else:
        print("❌ pyproject.toml not found")
        return False


def main():
    """Run all verification checks."""
    print("🚀 AIPC ADK Agents - Development Environment Verification")
    print("=" * 60)
    print()

    checks = [
        ("Python 3.12+", check_python_version),
        ("uv package manager", check_uv_installed),
        ("Git", check_git_installed),
        ("Virtual environment", check_virtual_env),
        ("Dependencies", check_dependencies_installed),
        ("Pre-commit hooks", check_pre_commit_installed),
        ("Required files", check_required_files),
        ("Workspace config", check_workspace_config),
    ]

    results = []
    for _name, check_func in checks:
        results.append(check_func())
        print()

    print("=" * 60)
    passed = sum(results)
    total = len(results)

    print(f"\n📊 Results: {passed}/{total} checks passed")

    if passed == total:
        print("\n✅ Your development environment is fully configured!")
        print("   You're ready to start contributing! 🎉")
        return 0
    else:
        print("\n⚠️  Some checks failed. Here's what to do:")
        print()

        if not results[0]:  # Python
            print("   1. Install Python 3.12+: https://www.python.org/downloads/")

        if not results[1]:  # uv
            print("   2. Install uv: curl -LsSf https://astral.sh/uv/install.sh | sh")

        if not results[2]:  # Git
            print("   3. Install Git: https://git-scm.com/downloads")

        if not results[3] or not results[4]:  # venv or deps
            print("   4. Run: make dev-setup")
            print("      (or manually: uv sync)")

        if not results[5]:  # pre-commit
            print("   5. Run: uv run pre-commit install")
            print("           uv run pre-commit install --hook-type commit-msg")

        if not results[7]:  # workspace config
            print(
                "   6. Delete uv.toml if it exists (workspace config should be in pyproject.toml)"
            )

        print("\n   For detailed setup instructions, see:")
        print("   docs/DEVELOPMENT_SETUP.md")

        return 1


if __name__ == "__main__":
    sys.exit(main())
