import { useEffect, useState } from "react";

const API_URL = "http://127.0.0.1:5000/api/students";

export default function App() {
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function loadStudents() {
      try {
        setLoading(true);
        setError("");

        const response = await fetch(API_URL);

        if (!response.ok) {
          throw new Error(`API request failed with status ${response.status}`);
        }

        const data = await response.json();
        setStudents(data);
      } catch (err) {
        setError(err.message || "Unable to load student data.");
      } finally {
        setLoading(false);
      }
    }

    loadStudents();
  }, []);

  return (
    <main className="page">
      <section className="hero">
        <p className="eyebrow">DAY 41</p>
        <h1>Students from Flask API</h1>
        <p className="subtitle">
          React → fetch() → Flask REST API → JSON → useState() → UI
        </p>
      </section>

      <section className="panel" aria-live="polite">
        {loading && <p className="state">Loading students…</p>}

        {!loading && error && (
          <div className="error">
            <strong>Connection error:</strong> {error}
            <p>Start the Flask backend on http://127.0.0.1:5000 and refresh.</p>
          </div>
        )}

        {!loading && !error && students.length === 0 && (
          <p className="state">No students returned by the API.</p>
        )}

        {!loading && !error && students.length > 0 && (
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
        Data source: <code>GET /api/students</code>
      </footer>
    </main>
  );
}
