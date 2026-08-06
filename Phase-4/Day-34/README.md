# Day 34 — REST API & Middlewares

Innolift Ventures — Crescent Batch

## What this covers
- Custom Express middlewares: request logger, response timer, body validator
- Full REST API on `/api/projects` — GET, POST, PUT, DELETE
- A live Projects page (`public/projects.html`) that adds/edits/deletes projects
  through `fetch()` calls to that API

## Run it
```bash
npm install
npm start
```
Then open http://127.0.0.1:5000/home.html

## API reference
| Method | Route                | Description          |
|--------|-----------------------|----------------------|
| GET    | /api/projects          | List all projects    |
| GET    | /api/projects/:id      | Get one project      |
| POST   | /api/projects          | Create a project     |
| PUT    | /api/projects/:id      | Update a project     |
| DELETE | /api/projects/:id      | Delete a project     |

## How to verify it's working
1. Start the server (`npm start`) — watch the terminal for `[REQUEST]` / `[RESPONSE]` log lines as you use the site; this confirms the middleware is running.
2. Open `projects.html` in the browser, add a project, then refresh the page — if it's still there, POST + GET both work.
3. Click **Edit** on a project, change the description, save — confirms PUT.
4. Click **Delete** on a project — confirms DELETE.
5. In the browser DevTools Network tab, check any `/api/projects` request's response headers for `X-Response-Time-Ms` — confirms the timer middleware ran.
6. Try submitting the form with an empty title — should show a red error instead of saving, confirming the validation middleware runs before the route handler.
