# Day 42 – POST API & Form Submission

Completed the Day 42 tasks by extending the Day 41 React + Flask application from a read-only GET workflow into a complete form-submission workflow.

## Completed tasks

1. Flask `POST /api/students` API
2. JSON validation for `name`, `email`, and `course`
3. React controlled student form using `useState()` and `onChange`
4. Form submission using `onSubmit` and `event.preventDefault()`
5. React `fetch()` POST request with `Content-Type: application/json`
6. Loading state with spinner and disabled submit button
7. Success message and automatic form clearing
8. Newly created student added to the list without a page refresh
9. Existing Day 41 `GET /api/students` functionality preserved

## Project structure

```text
Day42_Post_API_Form_Submission/
├── backend/
│   ├── app.py
│   └── requirements.txt
├── frontend/
│   ├── package.json
│   ├── index.html
│   └── src/
│       ├── App.jsx
│       ├── main.jsx
│       └── styles.css
├── docs/
│   ├── day-41-api-flow.md
│   └── day-42-post-api-flow.md
├── tests/
│   └── test_api.py
├── POSTMAN_TEST.md
└── README.md
```

## Run Flask backend

```bash
cd backend
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start Flask:

```bash
python app.py
```

## Test the POST API

```http
POST http://127.0.0.1:5000/api/students
Content-Type: application/json
```

Body:

```json
{
  "name": "New Student",
  "email": "newstudent@example.com",
  "course": "B.Tech AI & DS"
}
```

A successful request returns HTTP `201 Created` and the created student object.

## Run React frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Open the Vite URL shown in the terminal, normally `http://localhost:5173`.

## Day 42 workflow

```text
User fills form
      ↓
Controlled inputs (useState)
      ↓
Submit → onSubmit
      ↓
event.preventDefault()
      ↓
loading = true → spinner
      ↓
fetch(POST /api/students)
      ↓
Flask validation
      ↓
Create student
      ↓
JSON response
      ↓
loading = false
      ↓
setStudents([...students, createdStudent])
      ↓
Form clears + success message
      ↓
Updated list appears without refresh
```

## Data storage note

The internship task does not require a database. New records are appended to the Flask in-memory `STUDENTS` list, so they remain available while the Flask process is running and reset when the backend restarts.
