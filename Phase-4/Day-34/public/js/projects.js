const API_BASE = window.location.origin;

const listEl = document.getElementById('projectList');
const formEl = document.getElementById('projectForm');
const formStatus = document.getElementById('formStatus');
const formTitle = document.getElementById('formTitle');
const idField = document.getElementById('projectId');
const titleField = document.getElementById('projectTitle');
const descField = document.getElementById('projectDescription');
const techField = document.getElementById('projectTech');
const cancelEditBtn = document.getElementById('cancelEdit');

async function loadProjects() {
  listEl.innerHTML = '<p>Loading...</p>';
  try {
    const res = await fetch(`${API_BASE}/api/projects`);
    const projects = await res.json();
    renderProjects(projects);
  } catch (err) {
    listEl.innerHTML = `<p style="color:var(--danger)">Failed to load projects: ${err.message}</p>`;
  }
}

function renderProjects(projects) {
  if (!projects.length) {
    listEl.innerHTML = '<p>No projects yet. Add one below.</p>';
    return;
  }

  listEl.innerHTML = projects.map(p => `
    <div class="card project-card">
      <span class="tech-tag">${escapeHtml(p.tech || 'N/A')}</span>
      <h3>${escapeHtml(p.title)}</h3>
      <p>${escapeHtml(p.description)}</p>
      <div class="card-actions">
        <button class="btn-edit" data-action="edit" data-id="${p.id}">Edit</button>
        <button class="btn-delete" data-action="delete" data-id="${p.id}">Delete</button>
      </div>
    </div>
  `).join('');
}

function escapeHtml(str) {
  const div = document.createElement('div');
  div.textContent = str;
  return div.innerHTML;
}

listEl.addEventListener('click', async (event) => {
  const btn = event.target.closest('button[data-action]');
  if (!btn) return;
  const id = btn.dataset.id;

  if (btn.dataset.action === 'delete') {
    if (!confirm('Delete this project?')) return;
    await fetch(`${API_BASE}/api/projects/${id}`, { method: 'DELETE' });
    loadProjects();
  }

  if (btn.dataset.action === 'edit') {
    const res = await fetch(`${API_BASE}/api/projects/${id}`);
    const project = await res.json();
    idField.value = project.id;
    titleField.value = project.title;
    descField.value = project.description;
    techField.value = project.tech || '';
    formTitle.textContent = `Edit Project #${project.id}`;
    cancelEditBtn.style.display = 'inline-block';
  }
});

cancelEditBtn.addEventListener('click', resetForm);

function resetForm() {
  formEl.reset();
  idField.value = '';
  formTitle.textContent = 'Add a New Project';
  cancelEditBtn.style.display = 'none';
  formStatus.textContent = '';
}

formEl.addEventListener('submit', async (event) => {
  event.preventDefault();
  const payload = {
    title: titleField.value,
    description: descField.value,
    tech: techField.value
  };
  const id = idField.value;
  const method = id ? 'PUT' : 'POST';
  const url = id ? `${API_BASE}/api/projects/${id}` : `${API_BASE}/api/projects`;

  formStatus.style.color = '';
  formStatus.textContent = 'Saving...';

  try {
    const res = await fetch(url, {
      method,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    if (!res.ok) {
      const data = await res.json().catch(() => ({}));
      throw new Error(data.error || `Request failed (${res.status})`);
    }
    formStatus.style.color = 'var(--success)';
    formStatus.textContent = id ? 'Project updated.' : 'Project added.';
    resetForm();
    loadProjects();
  } catch (err) {
    formStatus.style.color = 'var(--danger)';
    formStatus.textContent = `Error: ${err.message}`;
  }
});

loadProjects();
