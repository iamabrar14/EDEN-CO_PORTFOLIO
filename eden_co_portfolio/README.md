# Eden & Co Portfolio

Company portfolio website built with Django.

## Environment Setup

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Apply database migrations:

```powershell
python manage.py makemigrations
python manage.py migrate
```

4. Create an admin user (optional):

```powershell
python manage.py createsuperuser
```

5. Run the development server:

```powershell
python manage.py runserver
```

Visit http://127.0.0.1:8000/landing/ (or http://127.0.0.1:8000/) to view the site.

## Project Structure

- Project: `eden_co_portfolio`
- App: `portfolio`
- Database: SQLite (development)

## Notes

- Static files are served from `portfolio/static` during development.
- Update `ALLOWED_HOSTS` in `eden_co_portfolio/settings.py` for production.
