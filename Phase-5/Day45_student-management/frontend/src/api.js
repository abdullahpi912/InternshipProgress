const BASE_URL = "http://localhost:5000/api/students";

export async function getStudents() {
  const res = await fetch(BASE_URL);
  const json = await res.json();
  if (!json.success) throw new Error(json.message || "Failed to load students");
  return json.data;
}

export async function addStudent(student) {
  const res = await fetch(BASE_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(student),
  });
  const json = await res.json();
  if (!json.success) throw new Error(json.message || "Failed to add student");
  return json.data;
}
