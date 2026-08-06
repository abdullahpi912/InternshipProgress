// Simple light/dark theme toggle, persisted for the session
const themeToggle = document.getElementById('themeToggle');

function applyStoredTheme() {
  const isLight = document.body.dataset.theme === 'light';
  document.body.classList.toggle('light', isLight);
}

if (themeToggle) {
  themeToggle.addEventListener('click', () => {
    const isLight = document.body.classList.toggle('light');
    document.body.dataset.theme = isLight ? 'light' : 'dark';
    themeToggle.textContent = isLight ? '🌙' : '☀️';
  });
}
