import Header from "./components/Header";
import Footer from "./components/Footer";
import StudentProfileCard from "./components/StudentProfileCard";
import students from "./data/students";
import "./App.css";

function App() {
  return (
    <div className="app-container">
      <Header />
      <main className="main-content">
        {students.map((student) => (
          <StudentProfileCard
            key={student.name}
            name={student.name}
            department={student.department}
            college={student.college}
            email={student.email}
            skills={student.skills}
          />
        ))}
      </main>
      <Footer />
    </div>
  );
}

export default App;
