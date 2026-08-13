# Day 43 – API Response & Frontend-Backend Practice

## Objective

Improve the existing Day 41 and Day 42 React + Flask application by handling successful responses, failed requests, and successful responses that contain no data.

## Task 01 – Error Handling

The React GET request now uses `try...catch...finally` and checks `response.ok`.

If Flask is unavailable, the request enters `catch` and the UI shows:

```text
Unable to load students.
```

The `finally` block always sets the GET loading state back to `false`.

The POST flow also checks `response.ok`, handles JSON errors, and stops its submitting state in `finally`.

### Practical failure test

1. Stop the Flask server.
2. Keep the React/Vite server running.
3. Refresh the React page.
4. The student list request fails.
5. The UI shows `Unable to load students.` instead of crashing or displaying an empty table.

## Task 02 – Empty Data Handling

A successful API response can still contain no records. When the GET API returns `[]`, React displays:

```text
No students found.
```

The table is not rendered when the list is empty.

### Empty-data test mode

For safe testing without editing the normal student data, the Flask API supports:

```text
GET http://127.0.0.1:5000/api/students?empty=true
```

This intentionally returns `[]` for Day 43 testing only.

Alternatively, set:

```text
DAY43_EMPTY_DATA=1
```

before starting Flask.

After testing, remove the variable or use the normal URL again.

## Task 03 – Complete GET → POST → UI Flow

```text
Open React App
      ↓
GET /api/students
      ↓
Display Students
      ↓
Fill Student Form
      ↓
Submit
      ↓
POST /api/students
      ↓
Flask validates data
      ↓
201 JSON Response
      ↓
Show Success Message
      ↓
Add returned student to React state
      ↓
Updated list appears without page refresh
```

## What happens after clicking Submit?

1. The controlled inputs already contain the form values in React state.
2. `onSubmit` runs and `event.preventDefault()` prevents a browser refresh.
3. React sets the submitting/loading state to `true`.
4. `fetch()` sends a POST request with `Content-Type: application/json`.
5. Flask receives the JSON body.
6. Flask validates `name`, `email`, and `course`.
7. Flask creates the new student and returns HTTP `201` with JSON.
8. React checks `response.ok` and parses the JSON response.
9. React adds the returned student to `students` using `setStudents()`.
10. React clears the form and shows the success message.
11. The component re-renders and the new student appears without a page refresh.

## Response States

| Situation | HTTP/API Result | React UI |
|---|---|---|
| Backend available + students | 200 + student array | Student table |
| Backend available + no students | 200 + `[]` | `No students found.` |
| Backend unavailable | Network failure | `Unable to load students.` |
| Invalid POST data | 400 + JSON error | Error message |
| Successful POST | 201 + created student | Success + updated list |

## Day 43 Completion Checklist

- Error handling with `try...catch`
- `response.ok` checked
- GET loading state stopped in `finally`
- `Unable to load students.` shown for backend failure
- Empty API response handled
- `No students found.` shown for empty data
- No empty table rendered
- Full GET → POST → JSON → UI flow supported
- Successful POST updates list without refresh
- POST failure is displayed in the UI
- Testing instructions included
