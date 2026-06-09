# Django Professional Backend

A highly structured, professional Django backend ready for API production.

## Features
- **REST APIs**: Using Django REST Framework (DRF).
- **Environment variables**: Managed using `django-environ`.
- **Modular Apps**: Kept in the `apps/` directory to keep the root directory clean.
- **CORS Headers**: Pre-configured.
- **Production Ready**: Gunicorn and Docker configuration.

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

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Run development server:
   ```bash
   python manage.py runserver
   ```

6. Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

## Docker Setup

```bash
docker build -t django-backend .
docker run -p 8000:8000 --env-file .env django-backend
```
