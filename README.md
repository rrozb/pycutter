# pycutter 🔪

<p align="center">
  <img src="assets/logo.webp" alt="Pycutter Logo" width="200"/>
</p>

A highly opinionated Python template built for Human 👤 and AI 🤖 devs, featuring AI-friendly configurations for Cursor, CodeRabbit, and future AI tools. 
Your AI collegues deserve better 💪

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-312/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Features

- Modern Python 3.12 setup
- [Poetry](https://python-poetry.org/) for dependency management
- [Ruff](https://docs.astral.sh/ruff/) for lightning-fast linting
- [Pytest](https://docs.pytest.org/en/latest/) with coverage reporting
- [Deptry](https://deptry.com/) for dependency analysis
- GitHub Actions CI pipeline
- Pre-configured settings for:
  - Type checking with mypy
  - Code formatting
  - Git ignore patterns
  - Dependency analysis with Deptry
  - [Cursor](https://docs.cursor.com/) prompt
  - [CodeRabbit](https://docs.coderabbit.ai/) AI code review

## 📦 Project Structure

```
cookiecutter-python-template/
├── assets/
│   └── logo.png
├── cookiecutter.json
├── hooks/
│   └── post_gen_project.py
└── {{cookiecutter.project_slug}}/
    ├── .github/
    │   └── workflows/
    │       └── ci.yml
    ├── {{cookiecutter.project_slug}}/
    │   ├── __init__.py
    │   ├── settings/
    │   │   ├── __init__.py
    │   │   └── settings.py
    │   └── main.py
    ├── tests/
    │   ├── __init__.py
    │   └── test_main.py
    ├── .gitignore
    ├── .cursorrules
    ├── .coderabbit.yaml
    ├── makefile
    ├── pyproject.toml
    └── README.md
```

## 🛠️ Quick Start

1. First, ensure you have cookiecutter installed:
```bash
pip install -U cookiecutter
```
2. Create a [new repository](https://github.com/new) on GitHub (or other git provider)

3. Generate a new Python project:
```bash
cookiecutter https://github.com/rrozb/pycutter.git
```

4. Set up remote repository:
```bash
git remote add origin <your-repo-url>
git branch -M main
```
5. Commit and push:
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

6. Start coding 💻 & follow the new project's README.md.

## 📋 Requirements

- Python 3.12+
- Cookiecutter
- Poetry (will be installed automatically)

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

Or just open an issue 😊

## What is next

- Figure out how to improve repo for [Devin](https://docs.devin.ai/)
- Add a guide for AI assisted development.
- Add documentation support.

## 🙏 Acknowledgments

- Built with [Cookiecutter](https://github.com/cookiecutter/cookiecutter)
- Coded with [Cursor](https://www.cursor.com/) and [Claude](https://www.anthropic.com)
- Logo made with [Gemini 2](https://deepmind.google/technologies/gemini/)


