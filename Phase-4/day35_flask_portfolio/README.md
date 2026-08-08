# Day 35 — Basics of SQL (Flask + MySQL version)

Innolift Ventures — Crescent Batch

Python/Flask rewrite of the Day 34 Node/Express project, now backed by a real
MySQL database instead of an in-memory array.

## What this covers
- MySQL database `portfolio_db` with `skills`, `projects`, `certifications`,
  and `messages` tables (see `db_setup.sql`)
- Flask backend (`app.py`) connected via `mysql-connector-python`
- Request logger + response timer as `before_request` / `after_request` hooks
  (equivalent to the Day 34 Express middlewares)
- Full REST API on `/api/projects` — GET, POST, PUT, DELETE — reading and
  writing MySQL
- Read-only `/api/skills` and `/api/certifications` endpoints
- Same Projects page UI as Day 34, now calling the Flask API

## Setup

1. **Create the database** — open MySQL Workbench (or the CLI) and run
   everything in `db_setup.sql`.

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your MySQL password** — open `app.py` and replace
   `YOUR_MYSQL_PASSWORD` in `DB_CONFIG` with your actual root password.

4. **Run the server:**
   ```bash
   python app.py
   ```

5. Open **http://127.0.0.1:5000/**

## API reference
| Method | Route                    | Description          |
|--------|--------------------------|-----------------------|
| GET    | /api/projects            | List all projects    |
| GET    | /api/projects/<id>       | Get one project       |
| POST   | /api/projects            | Create a project     |
| PUT    | /api/projects/<id>       | Update a project      |
| DELETE | /api/projects/<id>       | Delete a project      |
| GET    | /api/skills              | List all skills       |
| GET    | /api/certifications      | List all certifications |

## How to verify it's working
1. Run `python app.py` — watch the terminal for `[REQUEST]` / `[RESPONSE]`
   log lines as you use the site; confirms the logger + timer are running.
2. Open the Projects page, add a project, then refresh — if it's still
   there, POST + GET both work against MySQL.
3. Click **Edit** on a project, change the description, save — confirms PUT.
4. Click **Delete** on a project — confirms DELETE.
5. In DevTools → Network tab, check any `/api/projects` response's headers
   for `X-Response-Time-Ms` — confirms the timer is attaching headers.
6. Submit the form with an empty title — should show a red error instead of
   saving, confirming validation runs before the database write.
7. In MySQL Workbench, run `SELECT * FROM projects;` — the row you added
   through the site should be visible directly in the table.
