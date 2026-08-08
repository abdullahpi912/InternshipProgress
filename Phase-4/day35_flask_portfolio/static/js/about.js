// Maps a skill name to a Font Awesome icon; falls back to a generic code icon
function iconForSkill(name) {
  const key = name.toLowerCase();
  if (key.includes('python')) return 'fa-brands fa-python';
  if (key.includes('sql') || key.includes('database')) return 'fa-solid fa-database';
  if (key.includes('flask') || key.includes('backend') || key.includes('django')) return 'fa-solid fa-server';
  if (key.includes('react') || key.includes('javascript') || key.includes('js')) return 'fa-brands fa-js';
  if (key.includes('machine learning') || key.includes('ml') || key.includes('ai')) return 'fa-solid fa-robot';
  if (key.includes('power bi') || key.includes('chart') || key.includes('eda')) return 'fa-solid fa-chart-simple';
  return 'fa-solid fa-code';
}

async function loadSkills() {
  const container = document.getElementById('skillsContainer');
  try {
    const res = await fetch('/api/skills');
    const skills = await res.json();

    if (!skills.length) {
      container.innerHTML = '<p class="subtitle">No skills added yet.</p>';
      return;
    }

    container.innerHTML = skills.map(skill => `
      <article class="skill-card">
        <i class="${iconForSkill(skill.name)}"></i>
        <h3>${skill.name}</h3>
      </article>
    `).join('');
  } catch (err) {
    container.innerHTML = '<p class="subtitle">Could not load skills right now.</p>';
  }
}

async function loadCertifications() {
  const container = document.getElementById('certContainer');
  try {
    const res = await fetch('/api/certifications');
    const certs = await res.json();

    if (!certs.length) {
      container.innerHTML = '<p class="subtitle">No certifications added yet.</p>';
      return;
    }

    container.innerHTML = certs.map(cert => {
      const link = cert.credential_url
        ? `<a href="${cert.credential_url}" target="_blank" rel="noopener">${cert.title}</a>`
        : `<span>${cert.title}</span>`;
      const issued = cert.issue_date ? ` &middot; ${cert.issue_date}` : '';
      return `
        <article class="certificate-card">
          ${link}
          <figcaption>${cert.issuer || ''}${issued}</figcaption>
        </article>
      `;
    }).join('');
  } catch (err) {
    container.innerHTML = '<p class="subtitle">Could not load certifications right now.</p>';
  }
}

loadSkills();
loadCertifications();
