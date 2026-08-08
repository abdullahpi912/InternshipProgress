const projectList = document.getElementById('projectList');
const projectForm = document.getElementById('projectForm');
const projectId = document.getElementById('projectId');
const projectTitle = document.getElementById('projectTitle');
const projectDescription = document.getElementById('projectDescription');
const projectTech = document.getElementById('projectTech');
const projectGithub = document.getElementById('projectGithub');
const formStatus = document.getElementById('formStatus');
const formTitle = document.getElementById('formTitle');
const cancelEdit = document.getElementById('cancelEdit');

async function loadProjects() {
  const res = await fetch('/api/projects');
  const projects = await res.json();
  projectList.innerHTML = '';

  projects.forEach(project => {
    const card = document.createElement('div');
    card.className = 'card project-card';
    card.innerHTML = `
      <h3>${project.title}</h3>
      <p>${project.description}</p>
      ${project.tech_stack ? `<span class="tech-tag">${project.tech_stack}</span>` : ''}
      <div class="card-actions">
        <button class="btn-edit" data-id="${project.id}">Edit</button>
        <button class="btn-delete" data-id="${project.id}">Delete</button>
      </div>
    `;
    projectList.appendChild(card);
  });

  document.querySelectorAll('.btn-edit').forEach(btn => {
    btn.addEventListener('click', () => startEdit(Number(btn.dataset.id), projects));
  });
  document.querySelectorAll('.btn-delete').forEach(btn => {
    btn.addEventListener('click', () => deleteProject(Number(btn.dataset.id)));
  });
}

function startEdit(id, projects) {
  const project = projects.find(p => p.id === id);
  if (!project) return;

  projectId.value = project.id;
  projectTitle.value = project.title;
  projectDescription.value = project.description;
  projectTech.value = project.tech_stack || '';
  projectGithub.value = project.github_url || '';

  formTitle.textContent = 'Edit Project';
  cancelEdit.style.display = 'inline-block';
  window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
}

function resetForm() {
  projectForm.reset();
  projectId.value = '';
  formTitle.textContent = 'Add a New Project';
  cancelEdit.style.display = 'none';
  formStatus.textContent = '';
}

cancelEdit.addEventListener('click', resetForm);

projectForm.addEventListener('submit', async (e) => {
  e.preventDefault();

  const payload = {
    title: projectTitle.value.trim(),
    description: projectDescription.value.trim(),
    tech: projectTech.value.trim(),
    github_url: projectGithub.value.trim()
  };

  const id = projectId.value;
  const url = id ? `/api/projects/${id}` : '/api/projects';
  const method = id ? 'PUT' : 'POST';

  const res = await fetch(url, {
    method,
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });

  if (!res.ok) {
    const err = await res.json();
    formStatus.textContent = err.error || 'Something went wrong.';
    formStatus.style.color = 'var(--danger)';
    return;
  }

  formStatus.textContent = id ? 'Project updated.' : 'Project added.';
  formStatus.style.color = 'var(--success)';
  resetForm();
  loadProjects();
});

async function deleteProject(id) {
  if (!confirm('Delete this project?')) return;
  await fetch(`/api/projects/${id}`, { method: 'DELETE' });
  loadProjects();
}

loadProjects();
