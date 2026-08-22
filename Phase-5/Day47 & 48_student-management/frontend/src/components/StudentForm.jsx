import { useState } from "react";
import { addStudent } from "../api";

export default function StudentForm({ onStudentAdded }) {
  const [form, setForm] = useState({ name: "", email: "", course: "" });
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState(null);

  function handleChange(e) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  async function handleSubmit(e) {
    e.preventDefault();
    setLoading(true);
    setMessage(null);
    try {
      const newStudent = await addStudent(form);
      onStudentAdded(newStudent);
      setMessage({ type: "success", text: "Student registered successfully!" });
      setForm({ name: "", email: "", course: "" });
    } catch (err) {
      setMessage({ type: "error", text: err.message || "Failed to register student" });
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="form-card">
      <div className="form-card-title">
        <span>➕</span> Register New Student
      </div>
      <form onSubmit={handleSubmit} className="student-form">
        <div className="input-wrapper">
          <input
            name="name"
            placeholder="Full Name (e.g. Alex Morgan)"
            value={form.name}
            onChange={handleChange}
            required
            autoComplete="name"
          />
        </div>
        <div className="input-wrapper">
          <input
            name="email"
            type="email"
            placeholder="Email Address (e.g. alex@example.com)"
            value={form.email}
            onChange={handleChange}
            required
            autoComplete="email"
          />
        </div>
        <div className="input-wrapper">
          <input
            name="course"
            placeholder="Degree / Course (e.g. B.Tech AI & DS)"
            value={form.course}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit" className="btn-primary" disabled={loading}>
          {loading ? (
            <>
              <span className="spinner"></span> Registering...
            </>
          ) : (
            "Add Student"
          )}
        </button>
      </form>

      {message && (
        <div className={`alert-box ${message.type}`} role="status">
          <span>{message.type === "success" ? "✅" : "⚠️"}</span>
          {message.text}
        </div>
      )}
    </div>
  );
}
