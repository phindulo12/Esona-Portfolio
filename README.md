# Esona Portfolio

Lightweight Flask teaching portfolio for Esona Mzalazala.

## Getting started

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Optionally configure email delivery for the contact form:
   ```bash
   export SMTP_SERVER="smtp.example.com"
   export SMTP_PORT=587
   export EMAIL_SENDER="you@example.com"
   export EMAIL_PASSWORD="yourpassword"
   export EMAIL_RECEIVER="recipient@example.com"
   export FLASK_APP=run.py
   export FLASK_ENV=development
   ```
4. Launch the portfolio:
   ```bash
   python run.py
   ```

## App structure

- `run.py` — app launcher
- `app/__init__.py` — Flask initialization
- `app/routes.py` — page routing and contact handling
- `app/templates/base.html` — shared layout template
- `app/templates/index.html` — homepage content
- `app/templates/lessons.html` — lesson portfolio and testimonials
- `app/templates/project_detail.html` — project case study page
- `app/static/css/style.css` — lighter professional styling with interactive project cards
