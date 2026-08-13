# Day 42 – POST API & Form Submission

## Objective

Extend the Day 41 React + Flask integration so React can send a new student to Flask using a POST request and update the displayed list without refreshing the page.

## Task 01 – Flask POST API

Endpoint:

```http
POST /api/students
```

The Flask route reads JSON with `request.get_json()`, validates that `name`, `email`, and `course` are non-empty strings, creates a new student with the next available ID, appends it to the in-memory list, and returns the created record as JSON.

Successful response:

```http
201 Created
Content-Type: application/json
```

## Task 02 – React Controlled Form

The form uses `useState()` for all three fields:

```text
form.name
form.email
form.course
```

Each input is controlled with a `value` from state and updates state through `onChange`.

The form uses:

```javascript
<form onSubmit={handleSubmit}>
```

and prevents the browser's default page submission with:

```javascript
event.preventDefault();
```

## Task 03 – React → Flask POST

The submission sends JSON using the native Fetch API:

```javascript
fetch(API_URL, {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify(form),
});
```

The Flask response is parsed with:

```javascript
const data = await response.json();
```

## Task 04 – Loading State

The React component uses `submitting` as the loading state for the POST operation.

Before the request:

```javascript
setSubmitting(true);
```

While the request is active:

- the submit button is disabled
- the button displays a spinner
- the button text changes to `Submitting…`
- form inputs are disabled

After the response or an error:

```javascript
setSubmitting(false);
```

## Task 05 – Update UI After Success

After a successful response:

```javascript
setStudents((currentStudents) => [...currentStudents, data.student]);
setForm(emptyForm);
setSuccess(data.message);
```

This performs three required actions:

1. Adds the created student to the existing list.
2. Clears all form fields.
3. Shows a success message.

React state updates the table immediately, so no page refresh is required.

## Complete API/Data Flow Architecture

```text
┌──────────────────────────────────────┐
│             React Frontend           │
│                                      │
│  Student Name / Email / Course       │
│              │                       │
│              ▼                       │
│       useState() controlled form     │
│              │                       │
│              ▼                       │
│        onSubmit + preventDefault()   │
│              │                       │
│              ▼                       │
│       loading = true + spinner       │
└──────────────┬───────────────────────┘
               │
               │ POST /api/students
               │ Content-Type: application/json
               │ JSON.stringify(form)
               ▼
┌──────────────────────────────────────┐
│             Flask Backend            │
│          127.0.0.1:5000             │
│                                      │
│       POST /api/students             │
│              │                       │
│              ▼                       │
│       Read JSON request body         │
│              │                       │
│              ▼                       │
│ Validate name/email/course           │
│              │                       │
│              ▼                       │
│       Create student record          │
│              │                       │
│              ▼                       │
│       Append to STUDENTS             │
│              │                       │
│              ▼                       │
│      jsonify(created student)        │
└──────────────┬───────────────────────┘
               │
               │ 201 JSON Response
               ▼
┌──────────────────────────────────────┐
│             React Frontend           │
│                                      │
│       response.json()                │
│              │                       │
│              ▼                       │
│       loading = false                │
│              │                       │
│      ┌───────┴────────┐              │
│      ▼                ▼              │
│ setForm(empty)   setStudents(...)    │
│      │                │              │
│      ▼                ▼              │
│ Success message   Updated list       │
│                                      │
│          NO PAGE REFRESH             │
└──────────────────────────────────────┘
```

## Expected Application Flow

```text
User fills the form
        ↓
Submit
        ↓
loading = true → Spinner appears
        ↓
fetch() POST request
        ↓
Flask /api/students
        ↓
Validation → Create Student → JSON Response
        ↓
loading = false
        ↓
Form clears
        ↓
Student list updates
        ↓
No page refresh required
```

## Validation Flow

```text
POST request
    ↓
Valid JSON object?
    ├── No → 400 Bad Request
    └── Yes
          ↓
name + email + course present and non-empty?
    ├── No → 400 Bad Request + missing_fields
    └── Yes
          ↓
Create record
          ↓
201 Created + student JSON
```
