# Day 41 – Connecting Frontend and Backend

Completed the four Day 41 tasks:

1. API flow documentation
2. Flask `GET /api/students` API
3. React + Flask integration using `fetch()`, `useEffect()`, and `useState()`
4. Responsive UI showing data returned by the backend

## Project structure

```text
Day41_Frontend_Backend_Integration/
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
│   └── day-41-api-flow.md
└── README.md
```

## Run the Flask backend

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

The API is available at:

```text
http://127.0.0.1:5000/api/students
```

## Test the API

Open the endpoint in a browser or use Postman:

```http
GET http://127.0.0.1:5000/api/students
```

Expected result: JSON containing at least five student records with `id`, `name`, `email`, and `course`.

## Run the React frontend

Open a second terminal:

```bash
cd frontend
npm install
npm run dev
```

Open the Vite URL shown in the terminal, normally:

```text
http://localhost:5173
```

The frontend automatically calls the Flask API when the component loads.

## Day 41 workflow

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

## Important

Student data is defined only in the Flask backend. React receives and renders that data from the API; it does not hardcode student records.
