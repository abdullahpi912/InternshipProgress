const contactForm = document.getElementById('contactForm');
const contactStatus = document.getElementById('contactStatus');

contactForm.addEventListener('submit', async (e) => {
  e.preventDefault();

  const payload = {
    name: document.getElementById('contactName').value.trim(),
    email: document.getElementById('contactEmail').value.trim(),
    subject: document.getElementById('contactSubject').value.trim(),
    message: document.getElementById('contactMessage').value.trim()
  };

  const res = await fetch('/api/messages', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });

  if (!res.ok) {
    const err = await res.json();
    contactStatus.textContent = err.error || 'Something went wrong. Please try again.';
    contactStatus.style.color = 'var(--danger)';
    return;
  }

  contactStatus.textContent = 'Thanks for reaching out! Your message has been saved.';
  contactStatus.style.color = 'var(--success)';
  contactForm.reset();
});
