# FastAPI Professional Backend

This is a professional backend project template using FastAPI, structured with clean separation of concerns:
- **api**: Route handlers (controllers)
- **core**: Application configuration and settings using Pydantic Settings
- **db**: Database session and engine setup (SQLAlchemy)
- **models**: SQLAlchemy models (database schema)
- **schemas**: Pydantic schemas (data validation & serialization)

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

4. Run the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

5. Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.
6. Interactive API docs are available at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Docker Setup

To run using Docker:
```bash
docker build -t fastapi-backend .
docker run -p 8000:8000 --env-file .env fastapi-backend
```
