function ThemeToggle({ isDarkMode, toggleTheme }) {
  return (
    <div className="card">
      <h2>Theme Toggle</h2>
      <p className="theme-status">
        Current Theme: <strong>{isDarkMode ? "Dark Mode 🌙" : "Light Mode ☀️"}</strong>
      </p>
      <button onClick={toggleTheme} className="toggle-btn">
        {isDarkMode ? "☀️ Switch to Light Mode" : "🌙 Switch to Dark Mode"}
      </button>
    </div>
  );
}

export default ThemeToggle;
