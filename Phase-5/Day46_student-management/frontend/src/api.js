const API_BASE_URL = "http://localhost:5000/api";

export async function getStudents() {
  const res = await fetch(`${API_BASE_URL}/students`);
  const json = await res.json();
  if (!json.success) throw new Error(json.message || "Failed to load students");
  return json.data;
}

export async function addStudent(student) {
  const res = await fetch(`${API_BASE_URL}/students`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(student),
  });
  const json = await res.json();
  if (!json.success) throw new Error(json.message || "Failed to add student");
  return json.data;
}

export async function predictCrop(features) {
  const res = await fetch(`${API_BASE_URL}/predict`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(features),
  });
  const json = await res.json();
  if (!json.success) throw new Error(json.error || "Failed to predict crop");
  return json.prediction;
}
