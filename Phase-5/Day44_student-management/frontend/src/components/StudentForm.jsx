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
      setMessage({ type: "success", text: "Student added successfully!" });
      setForm({ name: "", email: "", course: "" });
    } catch (err) {
      setMessage({ type: "error", text: err.message });
    } finally {
      setLoading(false);
    }
  }

  return (
    <form onSubmit={handleSubmit} className="student-form">
      <input name="name" placeholder="Name" value={form.name} onChange={handleChange} required />
      <input name="email" type="email" placeholder="Email" value={form.email} onChange={handleChange} required />
      <input name="course" placeholder="Course" value={form.course} onChange={handleChange} required />
      <button type="submit" disabled={loading}>
        {loading ? "Adding..." : "Add Student"}
      </button>
      {message && <p className={message.type}>{message.text}</p>}
    </form>
  );
}
