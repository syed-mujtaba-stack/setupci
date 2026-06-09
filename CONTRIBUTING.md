# Contributing to setupci

Thank you for considering contributing to **setupci**! 🎉  
This guide will help you get started.

---

## 🐛 Reporting Bugs

Use the [Bug Report](.github/ISSUE_TEMPLATE/bug_report.md) template to report issues.  
Please include:
- Your OS, Python version, and setupci version
- Exact steps to reproduce
- Expected vs actual behavior

---

## ✨ Suggesting Features

Use the [Feature Request](.github/ISSUE_TEMPLATE/feature_request.md) template to suggest improvements.  
Popular ideas include:
- New framework templates (e.g. Tornado, Starlette, Sanic)
- New project types (e.g. CLI app, data science)
- Improved interactive prompts

---

## 🛠️ Setting Up for Development

1. **Fork** the repository on GitHub
2. **Clone** your fork:
   ```bash
   git clone https://github.com/<your-username>/setupci.git
   cd setupci
   ```
3. **Create a virtual environment and install dependencies:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # source .venv/bin/activate  # Linux/macOS
   pip install -e . pytest
   ```
4. **Run the tests** to make sure everything works:
   ```bash
   pytest
   ```

---

## 🌿 Branching & Committing

- Create a branch from `main`:
  ```bash
  git checkout -b feature/my-new-feature
  ```
- Write meaningful commit messages:
  ```
  feat: add Tornado simple template
  fix: handle empty target directory edge case
  docs: update README with new framework list
  ```

---

## ➕ Adding a New Framework Template

1. Create a folder inside `setupci/templates/<framework>/simple/` and `setupci/templates/<framework>/backend/`
2. Add the standard files (`README.md`, `.gitignore`, etc.)
3. Add your new framework name to the `choices` list in [setupci/cli.py](setupci/cli.py)
4. Add the framework mapping in the `framework_map` dictionary in [setupci/cli.py](setupci/cli.py)
5. Add tests in [tests/test_cli.py](tests/test_cli.py)
6. Run `pytest` to verify

---

## ✅ Pull Request Checklist

Before submitting a PR, make sure:
- [ ] All tests pass: `pytest`
- [ ] You have tested `setupci init .` manually
- [ ] `README.md` is updated if needed
- [ ] Your branch is up to date with `main`

---

## 📝 Code Style

- Follow [PEP 8](https://peps.python.org/pep-0008/) for Python code.
- Keep functions focused and small.
- Add docstrings/comments where helpful.

---

Thank you for contributing! 💙
