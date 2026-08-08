const themeToggle = document.getElementById('themeToggle');
const body = document.body;

function applyTheme(theme) {
  if (theme === 'light') {
    body.classList.add('light');
    themeToggle.textContent = '🌙';
  } else {
    body.classList.remove('light');
    themeToggle.textContent = '☀️';
  }
}

const savedTheme = body.getAttribute('data-theme') === 'dark' ? 'dark' : 'dark';
applyTheme(savedTheme);

themeToggle.addEventListener('click', () => {
  const isLight = body.classList.contains('light');
  applyTheme(isLight ? 'dark' : 'light');
});
