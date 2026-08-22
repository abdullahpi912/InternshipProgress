import { useEffect, useState } from "react";
import { getStudents } from "./api";
import StudentForm from "./components/StudentForm";
import StudentList from "./components/StudentList";
import CropPredictor from "./components/CropPredictor";

export default function App() {
  const [activeTab, setActiveTab] = useState("students");
  const [students, setStudents] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  async function loadStudents() {
    setLoading(true);
    try {
      const data = await getStudents();
      setStudents(data);
      setError(null);
    } catch (err) {
      setError(err.message || "Failed to load student registry");
    } finally {
      setLoading(false);
    }
  }

  // Initial load from MySQL backend
  useEffect(() => {
    loadStudents();
  }, []);

  return (
    <div className="app-container">
      {/* Executive Header */}
      <header className="app-header">
        <h1>Student Registry & AI Crop Platform</h1>
        <p className="header-subtitle">
          Unified full-stack management portal integrating relational student records with machine learning agricultural intelligence.
        </p>

        {/* Navigation Tabs */}
        <nav className="tab-nav" aria-label="Main Navigation">
          <button
            type="button"
            className={`tab-btn ${activeTab === "students" ? "active" : ""}`}
            onClick={() => setActiveTab("students")}
          >
            <span>👨‍🎓</span> Student Management
          </button>
          <button
            type="button"
            className={`tab-btn ${activeTab === "ml" ? "active" : ""}`}
            onClick={() => setActiveTab("ml")}
          >
            <span>🌱</span> Crop Intelligence AI
          </button>
        </nav>
      </header>

      {/* Main Content Area */}
      <main className="main-content">
        {activeTab === "students" && (
          <section className="section-card" aria-labelledby="students-heading">
            <div className="section-header">
              <h2 id="students-heading">
                <span>📚</span> Student Records Directory
              </h2>
              <span className="counter-badge">
                {loading ? "Refreshing..." : `${students.length} Total Enrolled`}
              </span>
            </div>

            <StudentForm onStudentAdded={() => loadStudents()} />

            {error && (
              <div className="alert-box error" role="alert">
                <span>⚠️</span> {error}
              </div>
            )}

            <StudentList students={students} />
          </section>
        )}

        {activeTab === "ml" && (
          <section className="section-card" aria-labelledby="ml-heading">
            <CropPredictor />
          </section>
        )}
      </main>
    </div>
  );
}
