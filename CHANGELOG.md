# Changelog

All notable changes to **setupci** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),  
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

---

## [0.1.0] - 2024-06-09

### Added
- 🚀 Initial release of `setupci`
- Interactive CLI using `questionary` for framework and project type selection
- **FastAPI** templates:
  - `simple`: Minimal single-file FastAPI app
  - `backend`: Professional multi-module structure (routers, models, schemas, db, config, Dockerfile)
- **Flask** templates:
  - `simple`: Single-file Flask app
  - `backend`: Application factory pattern with blueprints, SQLAlchemy, Flask-Migrate, WSGI
- **Django** templates:
  - `simple`: Standard Django setup with manage.py
  - `backend`: Professional setup using `django-environ`, CORS, DRF, modular apps layout
- **General Python** templates:
  - `simple`: Basic Python script entrypoint
  - `backend`: Packageable `src/` layout with pyproject.toml and pytest
- Automated tests with `pytest` covering all 8 template combinations
- GitHub Actions CI workflow (tests on Python 3.9–3.13)
- GitHub Actions CD workflow (auto-publish to PyPI on GitHub Release)
