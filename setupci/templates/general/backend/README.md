# Professional Python Project

A clean structure for developing modern Python libraries or applications.

## Structure
- `src/`: Core source files of the package.
- `tests/`: Automated unit tests using Pytest.
- `pyproject.toml`: Dependency and build packaging setup.

## Getting Started

1. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install the package in editable mode with development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

3. Run the application:
   ```bash
   python -m src.main
   ```

4. Run unit tests:
   ```bash
   pytest
   ```
