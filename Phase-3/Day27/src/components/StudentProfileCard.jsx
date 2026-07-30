function StudentProfileCard({ name, department, college, email, skills }) {
  // Generate initials for avatar
  const initials = name
    .split(" ")
    .map((n) => n[0])
    .join("")
    .slice(0, 2)
    .toUpperCase();

  return (
    <div className="student-card">
      <div className="card-header-bg"></div>
      <div className="card-body">
        <div className="avatar-wrapper">
          <div className="avatar">{initials}</div>
        </div>
        <h2 className="student-name">{name}</h2>
        <span className="badge">Student Profile</span>

        <div className="info-section">
          <div className="info-item">
            <span className="info-icon">🎓</span>
            <div className="info-text">
              <label>Department</label>
              <p>{department}</p>
            </div>
          </div>

          <div className="info-item">
            <span className="info-icon">🏛️</span>
            <div className="info-text">
              <label>College</label>
              <p>{college}</p>
            </div>
          </div>

          <div className="info-item">
            <span className="info-icon">✉️</span>
            <div className="info-text">
              <label>Email</label>
              <a href={`mailto:${email}`}>{email}</a>
            </div>
          </div>
        </div>

        <div className="skills-section">
          <h3>Skills & Expertise</h3>
          <div className="skills-tags">
            {skills.map((skill) => (
              <span key={skill} className="skill-pill">
                {skill}
              </span>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

export default StudentProfileCard;

