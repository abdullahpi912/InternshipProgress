# Day 45 — API Testing with Postman

Testing the Day 41–44 Student Management API (React → Flask → MySQL) before
relying on the frontend. All tests below were run against the real Flask
server connected to a live MySQL `student_management` database — not
predicted or assumed. Requests were sent with Postman (collection in
`postman/Student_Management_API.postman_collection.json`) and cross-checked
with `curl`/a Python test script hitting the same running server.

## Setup

- Backend: `python app.py` → `http://localhost:5000`
- Database: `mysql -u root -p < backend/schema.sql`, seeded with 5 students
  (ids 1–5)
- Postman collection: **Student Management API**, base URL variable
  `{{base_url}} = http://localhost:5000`

## Task 02 — GET /api/students

**Request:** `GET /api/students`

**Result:** `200 OK`, JSON body, all 5 seeded students returned, read
straight from MySQL (`SELECT id, name, email, course FROM students ORDER BY id`).

```json
{
  "success": true,
  "data": [
    { "id": 1, "name": "Ananya Rao", "email": "ananya.rao@example.com", "course": "B.Tech AI & DS" },
    { "id": 2, "name": "Karthik Iyer", "email": "karthik.iyer@example.com", "course": "B.Tech CSE" },
    { "id": 3, "name": "Sneha Menon", "email": "sneha.menon@example.com", "course": "B.Tech ECE" },
    { "id": 4, "name": "Rahul Varma", "email": "rahul.varma@example.com", "course": "B.Tech Mechanical" },
    { "id": 5, "name": "Divya Prakash", "email": "divya.prakash@example.com", "course": "B.Tech IT" }
  ]
}
```

✅ Status correct · ✅ JSON · ✅ records returned · ✅ from MySQL · ✅ consistent structure

## Task 03 — POST /api/students (valid)

**Request:** `POST /api/students`
```json
{ "name": "Test Student", "email": "test@example.com", "course": "Computer Science" }
```

**Result:** `201 Created`
```json
{
  "success": true,
  "message": "Student added successfully",
  "data": { "id": 6, "name": "Test Student", "email": "test@example.com", "course": "Computer Science" }
}
```

**MySQL verification** (`SELECT * FROM students WHERE id = 6`) confirmed the
row actually exists in the database — the API response wasn't taken on
trust:

```
id=6  name=Test Student  email=test@example.com  course=Computer Science
```

## Task 04 — Invalid inputs

All five cases were sent to `POST /api/students`. None of them crashed the
server; each returned `400 Bad Request` with the same validation message,
since the backend checks `name`, `email`, and `course` are all non-empty
after stripping whitespace, before ever touching the database.

| # | Case | Request Body | Status | Response |
|---|------|---------------|--------|----------|
| 1 | Empty name | `{"name":"","email":"test2@example.com","course":"IT"}` | 400 | `{"success":false,"message":"Name, email and course are all required"}` |
| 2 | Missing email | `{"name":"Test Student","course":"IT"}` | 400 | same message |
| 3 | Missing course | `{"name":"Test Student","email":"test3@example.com"}` | 400 | same message |
| 4 | Empty JSON body | `{}` | 400 | same message |
| 5 | No request body | *(none sent)* | 400 | same message |

Case 5 works because the route uses `request.get_json(silent=True) or {}` —
a missing/unparsable body becomes `{}` instead of raising an exception, so
it falls through to the same validation branch instead of a 500 crash.

## Task 05 — Duplicate email

**Request:** `POST /api/students`
```json
{ "name": "Another Student", "email": "test@example.com", "course": "IT" }
```
(`test@example.com` already belongs to id 6 from Task 03.)

**Result:** `409 Conflict`
```json
{ "success": false, "message": "A student with this email already exists" }
```

The `email` column has a `UNIQUE` constraint in MySQL. The insert fails at
the database level with MySQL error 1062, which `app.py` catches
specifically and turns into a 409 with a readable message instead of a
generic 500. **Verified in MySQL**: the table still has exactly 6 rows after
this request — no duplicate or partial row was created.

## Task 06 — Invalid requests

| Case | Request | Before fix | After fix | 
|------|---------|-----------|-----------|
| Invalid endpoint | `GET /api/student` (typo) | `404`, HTML error page | `404`, `{"success":false,"message":"Endpoint not found"}` |
| Unsupported method | `DELETE /api/students` | `405`, HTML error page | `405`, `{"success":false,"message":"Method not allowed on this endpoint"}` |

**Finding:** Flask's default error handlers return HTML, not JSON, which is
useless to a JS/fetch client. Fixed by adding `@app.errorhandler(404)`,
`@app.errorhandler(405)`, and `@app.errorhandler(500)` to `app.py` so every
error path — including ones the two existing routes don't explicitly
handle — returns the same `{"success": false, "message": "..."}` shape as
the rest of the API.

## Task 07 — HTTP status codes

| Scenario | Status | Why |
|----------|--------|-----|
| Successful GET | 200 | Read succeeded, data returned |
| Successful POST | 201 | New resource created |
| Invalid input (validation failure) | 400 | Client sent a malformed/incomplete request; the server can't process it as-is |
| Duplicate email | 409 | Request is well-formed but conflicts with existing state (unique constraint) |
| Invalid endpoint | 404 | The route doesn't exist |
| Unsupported method | 405 | The route exists but not for this HTTP verb |
| Server/DB error | 500 | Something failed on the server side, not the client's fault |

## Task 08 — Consistency with the React frontend

Ran the same GET/POST flows through the React app (`npm run dev`) against
the same backend and database used for the Postman tests above.

- `GET /api/students` on load renders the same 5 (then 6) rows the API
  returned in Postman.
- Submitting the student form performs the same POST, receives the same
  `201` + `data` payload, and the new row appears in the list without a
  page refresh — since the frontend re-fetches after a successful create.
- Submitting the form with a duplicate email surfaces the backend's
  `"A student with this email already exists"` message to the user instead
  of failing silently, since the frontend reads and displays `message` from
  non-2xx responses.

Behavior was consistent between Postman and the React UI — same status
codes, same response shapes, same data.

## Task 09 — Summary table

| Test | Method | Endpoint | Result | Status |
|------|--------|----------|--------|--------|
| Get all students | GET | /api/students | Passed | 200 |
| Create student (valid) | POST | /api/students | Passed | 201 |
| Empty name | POST | /api/students | Passed | 400 |
| Missing email | POST | /api/students | Passed | 400 |
| Missing course | POST | /api/students | Passed | 400 |
| Empty JSON body | POST | /api/students | Passed | 400 |
| No request body | POST | /api/students | Passed | 400 |
| Duplicate email | POST | /api/students | Passed | 409 |
| Invalid endpoint | GET | /api/student | Passed (after fix) | 404 |
| Unsupported method | DELETE | /api/students | Passed (after fix) | 405 |

**Break → Fix → Verify:** the invalid-endpoint and unsupported-method cases
initially returned Flask's default HTML error pages instead of JSON. Added
JSON `errorhandler`s for 404/405/500 in `app.py`, restarted the server, and
re-ran both tests to confirm they now return the same JSON error shape as
the rest of the API.

## Screenshots

Add Postman screenshots for the requests above here (not included in this
export — capture them from the collection when running it locally against
your own server).
