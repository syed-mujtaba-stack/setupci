# setupci

[![PyPI version](https://badge.fury.io/py/setupci.svg)](https://pypi.org/project/setupci/)
[![Tests](https://github.com/syed-mujtaba-stack/setupci/actions/workflows/tests.yml/badge.svg)](https://github.com/syed-mujtaba-stack/setupci/actions/workflows/tests.yml)
[![Python Versions](https://img.shields.io/pypi/pyversions/setupci.svg)](https://pypi.org/project/setupci/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**setupci** is an interactive Python CLI tool to bootstrap project structures for various Python frameworks. Stop setting up boilerplate — just run one command and start coding.

---

## 📦 Installation

```bash
pip install setupci
```

---

## 🚀 Usage

Navigate to your project directory and run:

```bash
setupci init .
```

You will be asked:
1. **Which framework?** — FastAPI, Flask, Django, or General Python
2. **Which project type?** — Backend (professional) or Simple (basic)

That's it! Your project structure will be generated instantly.

---

## 🗂️ Generated Structures

### ⚡ FastAPI — Backend
```
app/
├── main.py         # FastAPI app + CORS + routers
├── core/config.py  # Pydantic settings (reads from .env)
├── api/
│   ├── router.py
│   └── endpoints/items.py   # CRUD routes
├── models/item.py  # SQLAlchemy model
├── schemas/item.py # Pydantic schemas
└── db/session.py   # Database engine + session
requirements.txt
Dockerfile
.env.example
```

### 🌶️ Flask — Backend
```
app/
├── __init__.py     # Application factory
├── config.py       # Config class
├── api/items.py    # Blueprint with CRUD routes
└── models/item.py  # SQLAlchemy model
wsgi.py
requirements.txt
Dockerfile
.env.example
```

### 🎸 Django — Backend
```
config/
├── settings.py     # Uses django-environ for .env
├── urls.py
├── wsgi.py
└── asgi.py
apps/
└── items/          # Sample DRF CRUD app
    ├── models.py
    ├── views.py
    ├── serializers.py
    └── urls.py
manage.py
requirements.txt
Dockerfile
.env.example
```

### 🐍 General Python — Backend
```
src/
├── __init__.py
└── main.py
tests/
└── test_main.py
pyproject.toml
README.md
```

---

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) to get started.

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

## 🔗 Links

- 🐙 **GitHub**: [github.com/syed-mujtaba-stack/setupci](https://github.com/syed-mujtaba-stack/setupci)
- 📦 **PyPI**: [pypi.org/project/setupci](https://pypi.org/project/setupci/)
- 🐛 **Issues**: [github.com/syed-mujtaba-stack/setupci/issues](https://github.com/syed-mujtaba-stack/setupci/issues)