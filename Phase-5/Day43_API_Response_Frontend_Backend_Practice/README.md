# Day 43 – API Response & Frontend-Backend Practice

Day 43 improves the existing Day 41 + Day 42 React and Flask application. No separate application was created.

## Completed Tasks

- GET API error handling with `try...catch`
- `response.ok` checks
- Clear `Unable to load students.` message when Flask is unavailable
- Loading state always stopped with `finally`
- Empty API response handling with `No students found.`
- No empty table displayed
- POST response/error handling preserved
- Full GET → display → form → POST → Flask validation → JSON → success → list update flow
- New student appears without page refresh
- Automated API tests for success, empty data, POST success, and POST failure

## Run Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## Run Frontend

In another terminal:

```bash
cd frontend
npm install
npm run dev
```

Open the Vite URL, normally `http://localhost:5173`.

## Test Error Handling

1. Start React.
2. Stop Flask.
3. Refresh the React page.
4. The UI should show:

```text
Unable to load students.
```

## Test Empty State

With Flask running, open:

```text
http://127.0.0.1:5000/api/students?empty=true
```

This returns `[]` for testing. The React app normally uses `/api/students`; to test the empty state through the UI, temporarily set `VITE_API_URL=http://127.0.0.1:5000/api/students?empty=true` in a frontend `.env` file, restart Vite, and then remove the override afterward.

The expected UI is:

```text
No students found.
```

## Test Full Flow

1. Open React while Flask is running.
2. Confirm students load.
3. Fill Name, Email, and Course.
4. Submit the form.
5. Observe the loading state.
6. Confirm Flask returns `201 Created`.
7. Confirm the success message.
8. Confirm the form clears.
9. Confirm the new student appears immediately without refreshing.
10. Stop Flask and verify the GET failure message.

## Automated Tests

From the project root:

```bash
python -m pytest tests
```

The tests cover successful GET, empty GET response, successful POST, and invalid POST failure.
