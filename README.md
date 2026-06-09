<p align="center">
  <img src="https://raw.githubusercontent.com/syed-mujtaba-stack/setupci/main/assets/logo.png" alt="setupci logo" width="400" />
</p>

<p align="center">
  Stop setting up boilerplate from scratch. Launch your next production-ready Python project in seconds with zero configuration.
</p>

<p align="center">
  Stop setting up boilerplate from scratch. Launch your next production-ready Python project in seconds with zero configuration.
</p>

<p align="center">
  <a href="https://pypi.org/project/setupci/"><img src="https://badge.fury.io/py/setupci.svg" alt="PyPI version" /></a>
  <a href="https://github.com/syed-mujtaba-stack/setupci/actions/workflows/tests.yml"><img src="https://github.com/syed-mujtaba-stack/setupci/actions/workflows/tests.yml/badge.svg" alt="Tests status" /></a>
  <a href="https://pypi.org/project/setupci/"><img src="https://img.shields.io/pypi/pyversions/setupci.svg" alt="Python Versions" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT" /></a>
  <a href="https://github.com/syed-mujtaba-stack/setupci/stargazers"><img src="https://img.shields.io/github/stars/syed-mujtaba-stack/setupci.svg?style=social" alt="GitHub Stars" /></a>
  <a href="https://pepy.tech/project/setupci"><img src="https://pepy.tech/badge/setupci" alt="Downloads" /></a>
</p>

---

## ✨ Features

- 💻 **Interactive CLI Interface** — Elegant, user-friendly interactive prompt powered by `questionary` and styled with `rich`.
- ⚡ **FastAPI Support** — Instantly scaffold modern, high-performance, asynchronous REST API architectures.
- 🌶️ **Flask Support** — Spin up lightweight, factory-pattern-based WSGI apps with pre-configured settings.
- 🎸 **Django Support** — Initialize modular Django and Django REST Framework structures with pre-split apps folder.
- 🐍 **General Python** — Setup clean general-purpose Python CLI, library, or script templates using modern `pyproject.toml` packaging.
- 🏗️ **Professional Backend Structure** — Generate comprehensive production-ready layouts that separate configuration, routing, schemas, and databases.
- 🐳 **Docker Ready** — Fully-featured multi-stage `Dockerfile` configurations included automatically.
- 🔑 **Environment Configured** — Out-of-the-box support for dotenv (`.env` and `.env.example`) parsing.
- 🛠️ **CRUD Starter Templates** — Pre-written SQLAlchemy models, Pydantic schemas, and sample routers to let you write business logic immediately.
- ⚙️ **Zero Boilerplate** — Get linting, testing, and dependency configurations setup automatically.

---

## 📦 Installation

To get started, install `setupci` from PyPI using pip:

```bash
pip install setupci
```

### 🔄 Keep Up-to-date
Upgrade to the latest version to get the newest features and templates:

```bash
pip install --upgrade setupci
```

---

## 🚀 Usage

Navigate to your workspace and initialize a new project in the current directory (or specify a subfolder):

```bash
setupci init .
```

### 🔄 Interactive Workflow
Once the CLI starts, it walks you through two simple configuration choices:

1. **Framework Selection** — Choose between `FastAPI`, `Flask`, `Django`, or `General Python`.
2. **Project Type Selection** — 
   - **Backend**: Generates a professional, production-ready structure complete with databases, docker files, environment separation, and CRUD examples.
   - **Simple**: A streamlined, minimal boilerplate template ideal for simple scripts, quick spikes, or lightweight integrations.

---

## 💻 Terminal Demo

Below is an example of what running `setupci init` looks like in your terminal:

```ansi
$ setupci init .

 ███████╗███████╗████████╗██╗   ██╗██████╗  ██████╗██╗
 ██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝██║
 ███████╗█████╗     ██║   ██║   ██║██████╔╝██║     ██║
 ╚════██║██╔══╝     ██║   ██║   ██║██╔═══╝ ██║     ██║
 ███████║███████╗   ██║   ╚██████╔╝██║     ╚██████╗██║
 ╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝      ╚═════╝╚═╝

                 Python Project Bootstrapper  •  v0.1.2

┌────────────────────────────── 🚀 Getting Started ──────────────────────────────┐
│ Answer a few questions and your project structure will be ready in seconds.      │
└──────────────────────────────────────────────────────────────────────────────────┘

? Which framework would you like to use?
  ● FastAPI        — Async Python API framework
  ○ Flask          — Lightweight micro-framework
  ○ Django         — Full-stack web framework
  ○ General Python — Library, script, or CLI project

? Which project type would you like?
  ● Backend  — Professional structure, Docker, env config
  ○ Simple   — Minimal boilerplate, quick start

┌──────────────────────────────── 📋 Project Summary ───────────────────────────────┐
│  Framework:  FastAPI                                                            │
│  Type:       Backend                                                            │
│  Location:   E:\my-new-project                                                  │
└──────────────────────────────────────────────────────────────────────────────────┘

⠋ Generating project files...
✓ Your FastAPI backend project is ready!
```

---

## 🗂️ Generated Structures

`setupci` designs clean layouts adhering to industry standards. Here is what gets generated:

### ⚡ FastAPI — Backend
A clean modular design using Pydantic, SQLAlchemy, and dependency injection.

```
app/
├── main.py                # App entrypoint with middleware, routing, & setup
├── core/
│   └── config.py          # Settings management loading configs from .env using Pydantic
├── api/
│   ├── router.py          # Global API router aggregating separate endpoints
│   └── endpoints/
│       └── items.py       # Implements complete mock CRUD endpoints (GET, POST, etc.)
├── models/
│   └── item.py            # SQLAlchemy Database model definitions
├── schemas/
│   └── item.py            # Pydantic schemas validating API payloads
└── db/
    └── session.py         # DB connection setup and SessionLocal generator
requirements.txt           # Main API dependencies
Dockerfile                 # Multi-stage Docker build config
.env.example               # Template database and system environment variables
```

### 🌶️ Flask — Backend
A structure implementing the flask factory pattern, Blueprints, and Flask-SQLAlchemy.

```
app/
├── __init__.py            # Application factory setup & extension loading
├── config.py              # Configuration classes (Development, Production)
├── api/
│   └── items.py           # Blueprint definition mapping API routes
└── models/
    └── item.py            # Database model mapping using Flask-SQLAlchemy
wsgi.py                    # Entry point script to run the server
requirements.txt           # Web server, Flask, and DB drivers
Dockerfile                 # Gunicorn-based production Docker setup
.env.example               # Flask configurations template
```

### 🎸 Django — Backend
A modernized Django layout splitting apps, tracking settings with django-environ, and API-ready with DRF.

```
config/
├── settings.py            # Core settings reading environment values from .env
├── urls.py                # Main URL configurations
├── wsgi.py                # WSGI entrypoint for web servers
└── asgi.py                # ASGI entrypoint for async channels or servers
apps/
└── items/                 # Pre-configured DRF API App
    ├── models.py          # Sample DB model definitions
    ├── views.py           # REST views implementing ModelViewSet
    ├── serializers.py     # Serializers converting model data to JSON
    └── urls.py            # App-level routing definitions
manage.py                  # Django execution utility
requirements.txt           # Django + DRF and dependencies
Dockerfile                 # Lightweight container setup for deployment
.env.example               # Configurable Django secret key and DB environment settings
```

### 🐍 General Python — Backend
A standard workspace ready for library publication or tool development.

```
src/
├── __init__.py            # Main package initializer
└── main.py                # Main execution script
tests/
└── test_main.py           # Standard pytest script
pyproject.toml             # Modern setup configuration for packaging/publishing
README.md                  # Basic user guide for the created package
```

---

## ❔ Why setupci?

Developers spend too much time repeating the same boilerplate setups. `setupci` bridges this gap:

- **🕒 Saves Time**: Avoid copying config files, writing database connections, or creating dockerfiles. Get to coding in 5 seconds.
- **🛡️ Production-Ready**: Implements industry best-practices such as configuration-code separation, factory patterns, environment variables, and Docker containerization.
- **🔰 Beginner & Pro Friendly**: Gives beginners a clear architecture to build on, and professionals a consistent, zero-fluff starter template.

---

## 🗺️ Roadmap

We are constantly improving `setupci`. Check out our planned roadmap:

- [ ] **Database Scaffolding** — Option to auto-configure PostgreSQL, MySQL, SQLite, or MongoDB.
- [ ] **Authentication Integration** — Bootstrap JWT/OAuth2 flows out-of-the-box.
- [ ] **AI-Powered Templates** — Prompt-to-structure project initialization.
- [ ] **Full-stack Support** — Pair backend frameworks with React, Vue, or Svelte frontends.
- [ ] **Extended Frameworks** — Support for Litestar, Sanic, Masonite, and Pynecone.

---

## 🤝 Contributing

Contributions make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

Please see our [CONTRIBUTING.md](CONTRIBUTING.md) to understand details on submitting PRs, setting up local tests, and reporting bugs.

---

## 📝 License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

---

## 🔗 Links

- **🐙 GitHub Repository**: [github.com/syed-mujtaba-stack/setupci](https://github.com/syed-mujtaba-stack/setupci)
- **📦 PyPI Package**: [pypi.org/project/setupci](https://pypi.org/project/setupci/)
- **🐛 Issues & Requests**: [github.com/syed-mujtaba-stack/setupci/issues](https://github.com/syed-mujtaba-stack/setupci/issues)