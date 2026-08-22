# Day 46 — ML Model Integration

Plugging the Phase 2 crop recommendation model into the Student Management
Flask backend as a `/api/predict` endpoint, alongside the existing
`/api/students` APIs. All results below are from a real run — model loaded,
Flask started, requests actually sent and answered.

## Task 01 — Model verification (standalone, before touching Flask)

- **Model file:** `crop_recommendation_model.pkl` (Phase 2, Day 20)
- **Model type:** `RandomForestClassifier` (scikit-learn), tuned with
  `GridSearchCV` (`n_estimators=200`, `max_depth=None`)
- **Libraries required:** `scikit-learn==1.6.1` (the version it was trained
  with — loading it under 1.8 threw an `InconsistentVersionWarning`, so the
  backend pins the matching version), `pandas`
- **Input format:** 7 numeric features, in this exact order —
  `N, P, K, temperature, humidity, ph, rainfall`
- **Output format:** a single string — the predicted crop name (one of 22
  classes, e.g. `"rice"`, `"banana"`, `"mango"`)
- **Preprocessing:** none. It's a tree-based model trained on raw feature
  values, so no scaling/encoding step is needed before prediction.

**Standalone test** (`ml/model.py` run directly, no Flask involved):

```
Model loaded in 1.176 s
Expected input fields: ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
Sample input: {'N': 90, 'P': 42, 'K': 43, 'temperature': 20.87, 'humidity': 82.0, 'ph': 6.5, 'rainfall': 202.9}
Prediction: rice
```

✅ Loads · ✅ Accepts input · ✅ Predicts · ✅ No errors

## Task 02 — Prediction module

`backend/ml/model.py` holds all the model logic, separate from `app.py`:

```
backend/
└── ml/
    ├── __init__.py
    ├── model.py                        # load_model(), predict()
    └── crop_recommendation_model.pkl
```

`model.py` exposes exactly two functions: `load_model()` (called once) and
`predict(values: dict) -> str` (called per request). `app.py` never touches
pickle, pandas, or the model object directly.

## Task 03 — Loading the model correctly

`app.py` calls `load_model()` once at module level, right after `CORS(app)`
— it runs when the Flask process starts, not inside the route handler.
Confirmed by the startup log showing the model load happens before the
server starts accepting requests, and by Task 07 below (three repeated
requests, ~10ms range, no reload delay on any of them).

## Task 04 — POST /api/predict

```python
@app.route("/api/predict", methods=["POST"])
def predict_crop():
    ...
```

**Request:**
```json
{ "N": 90, "P": 42, "K": 43, "temperature": 20.87, "humidity": 82.0, "ph": 6.5, "rainfall": 202.9 }
```

**Response (200 OK):**
```json
{ "success": true, "prediction": "rice" }
```

## Task 05 — Invalid ML input

All sent to `POST /api/predict`. Nothing crashed the server.

| # | Case | Request Body | Status | Response |
|---|------|---------------|--------|----------|
| 1 | Missing required field | `{"N":90,"P":42,"temperature":20.87,"humidity":82.0,"ph":6.5,"rainfall":202.9}` (no `K`) | 400 | `{"success":false,"error":"Missing required input: K"}` |
| 2 | Empty input | `"N": ""` (rest valid) | 400 | `{"success":false,"error":"N cannot be empty"}` |
| 3 | Incorrect data type | `"N": "high"` (rest valid) | 400 | `{"success":false,"error":"N must be a number"}` |
| 4 | Invalid values (out of range) | `"ph": 25` (rest valid) | 400 | `{"success":false,"error":"ph must be between 0 and 14"}` |
| 5 | Empty JSON body | `{}` | 400 | `{"success":false,"error":"Missing required input: N"}` |
| 6 | No request body | *(none sent)* | 400 | `{"success":false,"error":"Missing required input: N"}` |

Validation runs in three stages before the model ever sees the input:
presence → non-empty → numeric type, followed by two range checks (`ph`
0–14, `humidity` 0–100) that catch nonsense values a type check alone
wouldn't. Cases 5 and 6 both land on the same "missing N" message because
`request.get_json(silent=True) or {}` turns a missing/empty body into `{}`,
same as Day 45's `/api/students` handling.

## Task 06 — Postman testing

Two folders in the **Student Management API** Postman collection:
- `POST /api/predict - Valid prediction` and `...(different crop)` — both
  200 OK.
- `Invalid Input Tests (Task 05)` — all six cases above, all 400.

✅ Status codes correct · ✅ requests accepted · ✅ inference runs ·
✅ predictions returned · ✅ valid JSON throughout

## Task 07 — Prediction consistency

Same valid input (`N=90, P=42, K=43, temperature=20.87, humidity=82.0,
ph=6.5, rainfall=202.9`) sent 3 times in a row:

| Attempt | Status | Prediction |
|---------|--------|------------|
| 1 | 200 | rice |
| 2 | 200 | rice |
| 3 | 200 | rice |

A second, different valid input was also sent to confirm the endpoint isn't
just returning a constant:

| Input | Status | Prediction |
|-------|--------|------------|
| `N=100, P=82, K=50, temperature=27.4, humidity=80.3, ph=5.9, rainfall=104.6` | 200 | banana |

Same input → same output every time, response shape never changes, server
stayed up throughout. The Random Forest is deterministic at inference time
(no randomness left after training), so this is expected — but it's worth
confirming Flask isn't introducing any per-request variance (e.g. reloading
the model, or a stale/half-initialized state).

## Task 08 — Coexistence with the Student APIs

With the ML model loaded and `/api/predict` live, `/api/students` was
re-tested and still returns `200 OK` with all 6 rows (5 seed + 1 from Day
45's testing) — the existing endpoints work unmodified alongside the new
one. Backend now serves both:

```
/api/students   (GET, POST)   → MySQL
/api/predict    (POST)        → ML model
```

## Task 09 — Summary table

| Test | Method | Result | Status |
|------|--------|--------|--------|
| Valid Prediction | POST | Passed | 200 |
| Valid Prediction (different input) | POST | Passed | 200 |
| Consistency (3x same input) | POST | Passed | 200 (x3) |
| Missing Input | POST | Passed | 400 |
| Empty Input | POST | Passed | 400 |
| Incorrect Data Type | POST | Passed | 400 |
| Invalid Values (out of range) | POST | Passed | 400 |
| Empty JSON | POST | Passed | 400 |
| No Request Body | POST | Passed | 400 |
| Existing GET /api/students | GET | Passed (unbroken) | 200 |

## Screenshots

Add Postman screenshots for the requests above here — capture them from the
collection's new **ML Prediction API (Day 46)** folder when running it
locally.
