import { useEffect, useState } from "react";

const API_URL = "http://127.0.0.1:5000/api/students";

const emptyForm = {
  name: "",
  email: "",
  course: "",
};

export default function App() {
  const [students, setStudents] = useState([]);
  const [form, setForm] = useState(emptyForm);
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  useEffect(() => {
    async function loadStudents() {
      try {
        setLoading(true);
        setError("");

        const response = await fetch(API_URL);
        const data = await response.json();

        if (!response.ok) {
          throw new Error(data.message || `API request failed with status ${response.status}`);
        }

        if (!Array.isArray(data)) {
          throw new Error("Invalid API response format: expected an array of students.");
        }

        setStudents(data);
      } catch (err) {
        setError(err.message || "Unable to load student data.");
      } finally {
        setLoading(false);
      }
    }

    loadStudents();
  }, []);

  function handleChange(event) {
    const { name, value } = event.target;
    setForm((currentForm) => ({
      ...currentForm,
      [name]: value,
    }));
    setError("");
    setSuccess("");
  }

  async function handleSubmit(event) {
    event.preventDefault();
    setSubmitting(true);
    setError("");
    setSuccess("");

    try {
      const response = await fetch(API_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(form),
      });

      const data = await response.json();

      if (!response.ok) {
        const missing = data.missing_fields?.join(", ");
        throw new Error(missing ? `${data.message} Missing: ${missing}` : data.message || "Unable to create student.");
      }

      if (data.student) {
        setStudents((currentStudents) => [
          ...(Array.isArray(currentStudents) ? currentStudents : []),
          data.student,
        ]);
      }
      setForm(emptyForm);
      setSuccess(data.message || "Student created successfully.");
    } catch (err) {
      setError(err.message || "Unable to create student.");
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <main className="page">
      <section className="hero">
        <p className="eyebrow">DAY 42</p>
        <h1>Student Registration</h1>
        <p className="subtitle">
          React Form → fetch() POST → Flask API → JSON Response → Updated UI
        </p>
      </section>

      <section className="form-panel">
        <div className="section-heading">
          <div>
            <p className="section-label">POST API</p>
            <h2>Add New Student</h2>
          </div>
          <span className="method-badge">POST /api/students</span>
        </div>

        <form onSubmit={handleSubmit} className="student-form">
          <label>
            Student Name
            <input
              type="text"
              name="name"
              value={form.name}
              onChange={handleChange}
              placeholder="Enter student name"
              required
              disabled={submitting}
            />
          </label>

          <label>
            Email
            <input
              type="email"
              name="email"
              value={form.email}
              onChange={handleChange}
              placeholder="student@example.com"
              required
              disabled={submitting}
            />
          </label>

          <label>
            Course
            <input
              type="text"
              name="course"
              value={form.course}
              onChange={handleChange}
              placeholder="B.Tech AI & DS"
              required
              disabled={submitting}
            />
          </label>

          <button type="submit" disabled={submitting}>
            {submitting ? (
              <span className="button-content">
                <span className="spinner" aria-hidden="true" />
                Submitting…
              </span>
            ) : (
              "Add Student"
            )}
          </button>
        </form>

        {success && <div className="success" role="status">✓ {success}</div>}
        {error && <div className="error" role="alert"><strong>Error:</strong> {error}</div>}
      </section>

      <section className="panel" aria-live="polite">
        <div className="list-heading">
          <div>
            <p className="section-label">GET API</p>
            <h2>Student List</h2>
          </div>
          <span className="count-badge">{students.length} students</span>
        </div>

        {loading && <p className="state">Loading students…</p>}

        {!loading && !error && students.length === 0 && (
          <p className="state">No students returned by the API.</p>
        )}

        {!loading && students.length > 0 && (
          <div className="table-wrap">
            <table>
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Name</th>
                  <th>Email</th>
                  <th>Course</th>
                </tr>
              </thead>
              <tbody>
                {students.map((student) => (
                  <tr key={student.id}>
                    <td>{student.id}</td>
                    <td>{student.name}</td>
                    <td>{student.email}</td>
                    <td>{student.course}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </section>

      <footer>
        Data source: <code>GET /api/students</code> · Create: <code>POST /api/students</code>
      </footer>
    </main>
  );
}
