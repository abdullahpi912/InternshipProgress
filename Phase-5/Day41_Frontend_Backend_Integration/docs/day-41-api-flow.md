# Day 41 – API/Data Flow Documentation

## Task 01: API Flow Documentation

### 1. Purpose of `/api/students`

`GET /api/students` is a REST API endpoint exposed by the Flask backend. Its purpose is to return the available student records to the frontend as JSON.

The endpoint returns at least five student objects. Each object contains:

- `id`
- `name`
- `email`
- `course`

The React application does **not** store the student records directly. It requests them from the Flask API when the page loads.

### 2. What is an HTTP Request?

An HTTP request is a message sent by a client (such as a browser or React application) to a server to ask for a resource or perform an operation.

For this task the request is:

```http
GET /api/students HTTP/1.1
Host: 127.0.0.1:5000
```

Important parts:

- `GET` is the HTTP method.
- `/api/students` is the requested API route.
- The Flask application receives the request and executes the matching route function.

### 3. What is a JSON Response?

JSON (JavaScript Object Notation) is a lightweight text format used to exchange structured data between systems.

The Flask API returns a response similar to:

```json
[
  {
    "id": 1,
    "name": "Abdullah",
    "email": "abdullah@example.com",
    "course": "B.Tech AI & DS"
  }
]
```

The browser receives the response body as JSON, and React converts it into a JavaScript value with:

```javascript
const data = await response.json();
```

### 4. How data travels from Flask Backend → React Frontend

1. The React component is rendered.
2. `useEffect()` runs after the component loads.
3. `fetch()` sends a `GET` request to `http://127.0.0.1:5000/api/students`.
4. Flask receives the request at `/api/students`.
5. Flask creates a JSON response containing student records.
6. The response travels back over HTTP.
7. React calls `response.json()` to parse the JSON.
8. React stores the parsed data in `students` using `useState()`.
9. React re-renders because state changed.
10. The table maps over `students` and displays the backend data.

## Complete API/Data Flow Architecture Diagram

```text
┌───────────────────────────────┐
│        React Frontend         │
│                               │
│  Component loads              │
│       │                       │
│       ▼                       │
│  useEffect()                  │
│       │                       │
│       ▼                       │
│  fetch(GET /api/students)     │
└───────────────┬───────────────┘
                │
                │ HTTP GET Request
                ▼
┌───────────────────────────────┐
│        Flask Backend          │
│       127.0.0.1:5000         │
│                               │
│  @app.route("/api/students")  │
│       │                       │
│       ▼                       │
│  Student records prepared     │
│       │                       │
│       ▼                       │
│  jsonify(STUDENTS)            │
└───────────────┬───────────────┘
                │
                │ HTTP 200 JSON Response
                ▼
┌───────────────────────────────┐
│        React Frontend         │
│                               │
│  response.json()              │
│       │                       │
│       ▼                       │
│  setStudents(data)            │
│       │                       │
│       ▼                       │
│  React re-renders             │
│       │                       │
│       ▼                       │
│  Responsive Student Table     │
└───────────────────────────────┘
```

## Expected Workflow

```text
Flask API
   ↓
JSON Response
   ↓
React fetch()
   ↓
response.json()
   ↓
useState()
   ↓
React UI
```

## What happens from request to screen?

React starts the request from `useEffect()`. The browser sends an HTTP GET request to the Flask server. Flask matches `/api/students`, creates JSON from the student records, and sends an HTTP response. React receives the response, parses it with `response.json()`, stores the result with `setStudents()`, and the updated state causes React to render the student table.

This is the core frontend ↔ backend API integration flow used in modern web applications.
