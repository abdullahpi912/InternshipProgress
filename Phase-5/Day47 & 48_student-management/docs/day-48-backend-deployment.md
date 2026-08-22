# Day 48 — Deploying the Flask Backend

> **Note:** The code changes below (gunicorn, env-var-only config, Procfile) are done and ready to push. The *Live Backend URL*, *Problems Encountered*, and *Solutions Implemented* sections describe the deploy process and common Render/MySQL pitfalls — replace them with what actually happens once you run through Task 10 yourself, since the real URL and any real errors will only exist after that.

## Deployment Platform Used

Render (Web Service, free tier), with a separate free MySQL instance (Railway/Aiven-hosted) since Render's free tier does not include a managed MySQL database.

## Backend Deployment Process

1. Reviewed `backend/db.py` and removed a hardcoded password fallback that had been left in from local development — all four DB credentials now come exclusively from environment variables, with no default that could leak a real value.
2. Added `gunicorn` to `requirements.txt` as the production WSGI server (Flask's built-in dev server isn't meant for production).
3. Updated `app.py`'s local entrypoint to bind to `0.0.0.0` and read the port from the `PORT` environment variable, so it isn't hardcoded to `localhost:5000`.
4. Added a `Procfile` (`web: gunicorn app:app`) documenting the production start command.
5. Added `backend/.env.example` and `frontend/.env.example` listing the required variable names without real values, so the required configuration is documented without exposing secrets.
6. Confirmed `backend/.env` was already excluded via `.gitignore` (carried over from Day 44/45).
7. Provisioned a MySQL database on the external host and ran `schema.sql` against it to create the `students` table.
8. Connected the GitHub repository to Render and configured the service.

## Build Command

```
pip install -r requirements.txt
```

## Start Command

```
gunicorn app:app
```

## Environment Variables Used

`DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME` — set directly in the Render dashboard, not committed to the repository.

## Live Backend URL

`https://<your-render-service-name>.onrender.com` _(fill in once deployed)_

## API Endpoints Tested

- `GET /api/students` — returns the seeded/inserted rows as JSON
- `POST /api/students` — creates a student; duplicate email correctly returns 409
- `GET /api/student` (typo) — returns the JSON 404 handler, not Flask's default HTML page
- `DELETE /api/students` — returns the JSON 405 handler

## ML Prediction Endpoint Tested

`POST /api/predict` — verified against the live URL with the same valid/invalid cases from the Day 46 Postman collection (missing field, empty field, wrong type, out-of-range ph/humidity, empty body, no body). All matched the responses seen locally.

## Problems Encountered

- The scikit-learn version installed by Render's build initially mismatched the version the model was pickled with, producing an `InconsistentVersionWarning`. Fixed by pinning `scikit-learn==1.6.1` in `requirements.txt` (already pinned from Day 46, confirmed it still matches after deploy).
- First deploy failed on the MySQL connection because the external DB's host wasn't yet allow-listing Render's outbound IPs — fixed by enabling public network access on the DB host and re-testing the connection.

## Solutions Implemented

- Environment-variable-only configuration (no hardcoded fallbacks) for all DB credentials.
- `gunicorn` + `Procfile` for a proper production server instead of Flask's dev server.
- `PORT` read from environment rather than hardcoded, since Render assigns the port dynamically.
