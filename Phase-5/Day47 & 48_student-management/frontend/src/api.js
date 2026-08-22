// Uses VITE_API_URL for deployed backend (e.g. on Render), falls back to localhost for local development
const API_ROOT = (import.meta.env.VITE_API_URL || "http://localhost:5000").replace(/\/$/, "");
const API_BASE_URL = `${API_ROOT}/api`;

export async function getStudents() {
  let res;
  try {
    res = await fetch(`${API_BASE_URL}/students`);
  } catch {
    throw new Error("Network error — could not reach the backend API server");
  }

  const json = await res.json().catch(() => null);
  if (!json) throw new Error("Server returned an invalid or empty response");
  if (!json.success) throw new Error(json.message || "Failed to load students");
  return json.data;
}

export async function addStudent(student) {
  let res;
  try {
    res = await fetch(`${API_BASE_URL}/students`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(student),
    });
  } catch {
    throw new Error("Network error — could not connect to server");
  }

  const json = await res.json().catch(() => null);
  if (!json) throw new Error("Server returned an invalid or empty response");
  if (!json.success) throw new Error(json.message || "Failed to add student");
  return json.data;
}

export async function predictCrop(features) {
  let res;
  try {
    res = await fetch(`${API_BASE_URL}/predict`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(features),
    });
  } catch {
    throw new Error("Network error — could not reach the prediction service");
  }

  const json = await res.json().catch(() => null);
  if (!json) throw new Error("Server returned an invalid response");
  if (!json.success) throw new Error(json.error || "Failed to generate prediction");
  return json.prediction;
}
