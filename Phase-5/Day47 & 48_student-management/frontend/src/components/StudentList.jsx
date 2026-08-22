import { useState } from "react";

export default function StudentList({ students }) {
  const [searchTerm, setSearchTerm] = useState("");

  const filteredStudents = (students || []).filter((s) => {
    const term = searchTerm.toLowerCase();
    return (
      (s.name && s.name.toLowerCase().includes(term)) ||
      (s.email && s.email.toLowerCase().includes(term)) ||
      (s.course && s.course.toLowerCase().includes(term))
    );
  });

  // Generate deterministic avatar color gradients
  function getAvatarGradient(name = "") {
    const colors = [
      "linear-gradient(135deg, #4f46e5 0%, #3b82f6 100%)",
      "linear-gradient(135deg, #059669 0%, #10b981 100%)",
      "linear-gradient(135deg, #d97706 0%, #f59e0b 100%)",
      "linear-gradient(135deg, #7c3aed 0%, #a855f7 100%)",
      "linear-gradient(135deg, #0284c7 0%, #38bdf8 100%)",
      "linear-gradient(135deg, #e11d48 0%, #f43f5e 100%)",
    ];
    let sum = 0;
    for (let i = 0; i < name.length; i++) {
      sum += name.charCodeAt(i);
    }
    return colors[sum % colors.length];
  }

  function getInitials(name = "") {
    return name
      .split(" ")
      .filter(Boolean)
      .map((part) => part[0])
      .join("")
      .slice(0, 2)
      .toUpperCase();
  }

  if (!students || students.length === 0) {
    return (
      <div className="empty-state">
        <div className="empty-icon">📭</div>
        <p>No student records found in the database.</p>
        <span style={{ fontSize: "0.85rem", color: "var(--text-muted)" }}>
          Use the form above to enroll your first student.
        </span>
      </div>
    );
  }

  return (
    <div className="student-list-container">
      {/* Live Search & Filter Bar */}
      <div className="search-container">
        <input
          type="text"
          className="search-input"
          placeholder="Filter students by name, email, or department/course..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
      </div>

      {filteredStudents.length === 0 ? (
        <div className="empty-state">
          <div className="empty-icon">🔍</div>
          <p>No students match "{searchTerm}"</p>
        </div>
      ) : (
        <div className="table-wrapper">
          <table className="student-table">
            <thead>
              <tr>
                <th style={{ width: "80px" }}>ID</th>
                <th>Student Profile</th>
                <th>Email Address</th>
                <th>Enrolled Course</th>
              </tr>
            </thead>
            <tbody>
              {filteredStudents.map((s) => (
                <tr key={s.id}>
                  <td>
                    <span className="id-badge">#{s.id}</span>
                  </td>
                  <td>
                    <div className="student-name-cell">
                      <div
                        className="avatar-circle"
                        style={{ background: getAvatarGradient(s.name) }}
                      >
                        {getInitials(s.name)}
                      </div>
                      <span>{s.name}</span>
                    </div>
                  </td>
                  <td>
                    <span style={{ color: "var(--text-secondary)" }}>{s.email}</span>
                  </td>
                  <td>
                    <span className="course-pill">{s.course}</span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
