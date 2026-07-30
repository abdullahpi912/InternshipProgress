import { useState } from "react";
import NamePreview from "./components/NamePreview";
import ThemeToggle from "./components/ThemeToggle";
import "./App.css";

function App() {
  const [isDarkMode, setIsDarkMode] = useState(false);

  const toggleTheme = () => {
    setIsDarkMode((prev) => !prev);
  };

  return (
    <div className={`app ${isDarkMode ? "dark-mode" : "light-mode"}`}>
      <div className="container">
        <h1>Day 28 — Hooks & useState</h1>
        <NamePreview />
        <ThemeToggle isDarkMode={isDarkMode} toggleTheme={toggleTheme} />
      </div>
    </div>
  );
}

export default App;
