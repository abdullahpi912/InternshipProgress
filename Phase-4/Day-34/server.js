const express = require('express');
const cors = require('cors');
const path = require('path');

const app = express();
const PORT = 5000;

app.use(cors());
app.use(express.json());

// ==========================================
// CUSTOM MIDDLEWARES
// ==========================================

// 1. Request logger — runs on every request, logs method/path/timestamp
function requestLogger(req, res, next) {
  req.startTime = Date.now();
  console.log(`[REQUEST] ${req.method} ${req.originalUrl}`);
  next();
}

// 2. Response timer — wraps res.send so the X-Response-Time-Ms header is
//    attached BEFORE headers are flushed, and logs the final duration
function responseTimer(req, res, next) {
  const originalSend = res.send.bind(res);
  res.send = (body) => {
    const durationMs = Date.now() - req.startTime;
    res.set('X-Response-Time-Ms', `${durationMs}`);
    return originalSend(body);
  };
  res.on('finish', () => {
    const durationMs = Date.now() - req.startTime;
    console.log(`[RESPONSE] ${req.method} ${req.originalUrl} -> ${res.statusCode} (${durationMs}ms)`);
  });
  next();
}

// 3. Body validator — only applies to POST/PUT on /api/projects, checks
//    required fields exist before the route handler runs
function validateProjectBody(req, res, next) {
  if (req.method === 'GET' || req.method === 'DELETE') return next();

  const { title, description } = req.body || {};
  if (!title || !description) {
    return res.status(400).json({ error: 'title and description are required' });
  }
  next();
}

app.use(requestLogger);
app.use(responseTimer);
app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
  res.redirect('/home.html');
});

// ==========================================
// In-memory project store
// ==========================================
let projects = [
  { id: 1, title: 'Smart Crop Advisory Platform', description: 'ML-based crop & fertilizer recommendation system.', tech: 'Flask, React, scikit-learn' },
  { id: 2, title: 'Country Data Analysis', description: 'Exploratory data analysis of global country indicators.', tech: 'R' }
];
let nextId = 3;

// ==========================================
// REST API — /api/projects
// ==========================================

// GET all projects
app.get('/api/projects', (req, res) => {
  res.status(200).json(projects);
});

// GET single project
app.get('/api/projects/:id', (req, res) => {
  const project = projects.find(p => p.id === Number(req.params.id));
  if (!project) return res.status(404).json({ error: `Project ${req.params.id} not found` });
  res.status(200).json(project);
});

// POST create project
app.post('/api/projects', validateProjectBody, (req, res) => {
  const project = {
    id: nextId++,
    title: req.body.title,
    description: req.body.description,
    tech: req.body.tech || ''
  };
  projects.push(project);
  res.status(201).json(project);
});

// PUT update project
app.put('/api/projects/:id', validateProjectBody, (req, res) => {
  const project = projects.find(p => p.id === Number(req.params.id));
  if (!project) return res.status(404).json({ error: `Project ${req.params.id} not found` });

  project.title = req.body.title;
  project.description = req.body.description;
  project.tech = req.body.tech || project.tech;

  res.status(200).json(project);
});

// DELETE project
app.delete('/api/projects/:id', (req, res) => {
  const exists = projects.some(p => p.id === Number(req.params.id));
  if (!exists) return res.status(404).json({ error: `Project ${req.params.id} not found` });

  projects = projects.filter(p => p.id !== Number(req.params.id));
  res.status(200).json({ message: `Project ${req.params.id} deleted` });
});

app.get('/api/health', (req, res) => {
  res.status(200).json({ status: 'ok' });
});

app.listen(PORT, () => {
  console.log(`Day 34 server running at http://127.0.0.1:${PORT}`);
});
