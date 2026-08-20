export default function StudentList({ students }) {
  if (students.length === 0) return <p>No students found.</p>;

  return (
    <table className="student-list">
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Email</th>
          <th>Course</th>
        </tr>
      </thead>
      <tbody>
        {students.map((s) => (
          <tr key={s.id}>
            <td>{s.id}</td>
            <td>{s.name}</td>
            <td>{s.email}</td>
            <td>{s.course}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
