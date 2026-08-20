import { useEffect, useState } from "react";
import { getStudents } from "./api";
import StudentForm from "./components/StudentForm";
import StudentList from "./components/StudentList";

export default function App() {
  const [students, setStudents] = useState([]);
  const [error, setError] = useState(null);

  async function loadStudents() {
    try {
      const data = await getStudents();
      setStudents(data);
      setError(null);
    } catch (err) {
      setError(err.message);
    }
  }

  // Load students from MySQL (via Flask) on first render
  useEffect(() => {
    loadStudents();
  }, []);

  return (
    <div className="app">
      <h1>Student Management</h1>
      <StudentForm onStudentAdded={() => loadStudents()} />
      {error && <p className="error">{error}</p>}
      <StudentList students={students} />
    </div>
  );
}
