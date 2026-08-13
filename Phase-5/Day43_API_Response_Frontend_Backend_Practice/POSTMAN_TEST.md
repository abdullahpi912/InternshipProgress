# Day 42 – Postman API Test

## 1. Test the POST endpoint before React integration

Method:

```text
POST
```

URL:

```text
http://127.0.0.1:5000/api/students
```

Headers:

```text
Content-Type: application/json
```

Body → raw → JSON:

```json
{
  "name": "Kavin Kumar",
  "email": "kavin@example.com",
  "course": "B.Tech AI & DS"
}
```

Expected status:

```text
201 Created
```

Expected response shape:

```json
{
  "message": "Student created successfully.",
  "student": {
    "id": 6,
    "name": "Kavin Kumar",
    "email": "kavin@example.com",
    "course": "B.Tech AI & DS"
  },
  "success": true
}
```

## 2. Test validation

Send an empty JSON object:

```json
{}
```

Expected status:

```text
400 Bad Request
```

Expected response contains:

```text
name, email, and course are required.
```

## 3. Verify the GET endpoint

After the successful POST, send:

```text
GET http://127.0.0.1:5000/api/students
```

The newly created student should be present in the returned list.

## 4. React integration

Once the POST request works in Postman:

1. Start Flask.
2. Start the React frontend.
3. Fill Student Name, Email, and Course.
4. Click **Add Student**.
5. Observe the loading spinner and disabled button.
6. Verify the success message.
7. Verify the form fields are cleared.
8. Verify the new student appears in the list without refreshing the page.
