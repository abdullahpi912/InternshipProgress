const express = require("express");
const path = require("path");

const app = express();
const PORT = 3000;

// Serves style.css and Images/ from the public folder
app.use(express.static(path.join(__dirname, "public")));

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "home.html"));
});

app.get("/about", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "about.html"));
});

app.get("/contact", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "contact.html"));
});

// Task: "Pass text as a response" + "Use GET method to get a response"
app.get("/hello", (req, res) => {
  res.send("Hello, Express! This route returns plain text instead of an HTML file.");
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
