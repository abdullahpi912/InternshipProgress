import { useState } from "react";

function NamePreview() {
  const [name, setName] = useState("");

  return (
    <div className="card">
      <h2>Name Preview</h2>
      <input
        type="text"
        placeholder="Enter your name"
        value={name}
        onChange={(e) => setName(e.target.value)}
        className="name-input"
      />
      <p className="greeting">
        {name.trim() ? `Hello, ${name}! 👋` : "Hello, Guest! 👤"}
      </p>
    </div>
  );
}

export default NamePreview;
