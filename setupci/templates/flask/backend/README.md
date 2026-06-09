# Flask Professional Backend

A modular Flask backend project template using the Application Factory pattern and Blueprints.

## Structure
- `app/`: The core application code.
  - `__init__.py`: Application factory where Flask is initialized, extensions configured, and blueprints registered.
  - `config.py`: Environment-based settings management.
  - `api/`: API blueprints containing route definitions.
  - `models/`: SQLAlchemy database models.
- `wsgi.py`: WSGI entry point to run or deploy the app.

## Getting Started

1. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   ```

4. Initialize the database:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

5. Run the development server:
   ```bash
   flask run
   ```

6. Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Docker Setup

```bash
docker build -t flask-backend .
docker run -p 5000:5000 --env-file .env flask-backend
```
