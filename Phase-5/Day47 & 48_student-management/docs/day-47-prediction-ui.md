# Day 47 — Displaying ML Predictions in the UI

## Prediction UI Created

Added a new `PredictForm` component (`frontend/src/components/PredictForm.jsx`) below the existing student list on the same page. It follows the same layout pattern as `StudentForm` — a flex-wrapped input row plus a submit button — so the two features feel consistent.

## Input Fields Used

Seven numeric fields, matching the model's exact feature order (`ml/model.py:FEATURES`):

| Field | Label shown in UI |
|---|---|
| N | Nitrogen (N) |
| P | Phosphorus (P) |
| K | Potassium (K) |
| temperature | Temperature (°C) |
| humidity | Humidity (%) |
| ph | Soil pH |
| rainfall | Rainfall (mm) |

All fields are `type="number"` with `required`. The Predict button stays disabled until every field has a non-empty value, so incomplete submissions can't be sent.

## API Endpoint Connected

`POST /api/predict`, called from a new `predictCrop()` function in `frontend/src/api.js`.

## Request Format

```json
{
  "N": 90, "P": 42, "K": 43,
  "temperature": 20.8, "humidity": 82.0,
  "ph": 6.5, "rainfall": 202.9
}
```

## Response Format

Success:
```json
{ "success": true, "prediction": "rice" }
```

Failure:
```json
{ "success": false, "error": "ph must be between 0 and 14" }
```

## Loading State

While the request is in flight, the button text changes to "Generating prediction..." and is disabled, and a matching status line is shown below the form.

## Error Handling

- Backend validation errors (400) → the `error` message from the JSON response is shown directly.
- Backend unreachable / network failure → `predictCrop()` catches the fetch rejection and shows "Network error — could not reach the backend" instead of letting the UI crash.
- Non-JSON or malformed response → caught separately and shown as "Server returned an unexpected response".

Each new prediction clears the previous result and error before the request starts, so stale state is never shown alongside a new one.

## Test Results

Tested against the live local Flask + MySQL stack (same backend used for Day 45/46):

| Case | Result |
|---|---|
| Valid input (rice-range values) | ✅ Prediction displayed correctly |
| Different valid input (banana-range values) | ✅ Prediction updated correctly |
| Missing a required field | ✅ Blocked client-side (button stays disabled) |
| Invalid ph (>14) | ✅ Backend 400 error shown in UI |
| Invalid humidity (>100) | ✅ Backend 400 error shown in UI |
| Backend stopped mid-test | ✅ "Network error" message shown, UI stayed usable |
| Multiple sequential predictions | ✅ Each result replaces the previous one correctly |

## Screenshots

_(To be added: prediction input UI, a successful prediction, and an error state.)_
