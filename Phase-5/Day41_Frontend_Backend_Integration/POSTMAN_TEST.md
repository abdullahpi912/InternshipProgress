# Day 41 API Test

## Request

Method:

```text
GET
```

URL:

```text
http://127.0.0.1:5000/api/students
```

## Expected status

```text
200 OK
```

## Expected JSON shape

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

The actual API returns five student records.

## Browser test

1. Start the Flask backend with `python app.py`.
2. Open `http://127.0.0.1:5000/api/students`.
3. Verify that JSON appears in the browser.

## Postman test

1. Create a new request.
2. Select `GET`.
3. Enter `http://127.0.0.1:5000/api/students`.
4. Click **Send**.
5. Confirm the status is `200 OK`.
6. Confirm that five records are returned.
