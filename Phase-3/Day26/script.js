// Regex patterns (Day 26 reference set)
const PATTERNS = {
  fullName: /^[a-zA-Z\s]{3,30}$/,
  email: /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/,
  phone: /^[6-9]\d{9}$/,
  strongPassword: /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%]).{8,}$/,
  mediumPassword: /^(?=.*[a-zA-Z])(?=.*\d).{6,}$/
};

const form = document.getElementById('registerForm');
const fields = ['fullName', 'email', 'phone', 'dob', 'gender', 'password', 'confirmPassword'];
const inputs = Object.fromEntries(fields.map(id => [id, document.getElementById(id)]));
const errors = Object.fromEntries(fields.map(id => [id, document.getElementById(id + 'Error')]));

const strengthBar = document.getElementById('strengthBar');
const strengthLabel = document.getElementById('strengthLabel');
const successMsg = document.getElementById('successMsg');

// Marks a field valid/invalid and shows/clears its inline message
function setFieldState(id, isValid, message) {
  const input = inputs[id];
  input.classList.toggle('input-valid', isValid);
  input.classList.toggle('input-error', !isValid);
  errors[id].textContent = isValid ? '' : message;
  return isValid;
}

function validateFullName() {
  const value = inputs.fullName.value.trim();
  return setFieldState('fullName', PATTERNS.fullName.test(value),
    'Name must be 3-30 letters, no numbers or symbols');
}

function validateEmail() {
  const value = inputs.email.value.trim();
  return setFieldState('email', PATTERNS.email.test(value),
    'Enter a valid email address (name@domain.com)');
}

function validatePhone() {
  const value = inputs.phone.value.trim();
  return setFieldState('phone', PATTERNS.phone.test(value),
    'Enter a valid 10-digit Indian mobile number');
}

function validateDob() {
  const value = inputs.dob.value;
  if (!value) return setFieldState('dob', false, 'Date of birth is required');

  const dob = new Date(value);
  const today = new Date();
  let age = today.getFullYear() - dob.getFullYear();
  const hasHadBirthdayThisYear =
    today.getMonth() > dob.getMonth() ||
    (today.getMonth() === dob.getMonth() && today.getDate() >= dob.getDate());
  if (!hasHadBirthdayThisYear) age--;

  return setFieldState('dob', age >= 18, 'You must be at least 18 years old');
}

function validateGender() {
  return setFieldState('gender', inputs.gender.value !== '', 'Please select a gender');
}

function getPasswordStrength(value) {
  if (PATTERNS.strongPassword.test(value)) return 'strong';
  if (PATTERNS.mediumPassword.test(value)) return 'medium';
  return 'weak';
}

function updateStrengthMeter() {
  const value = inputs.password.value;
  strengthBar.className = 'strength-bar';
  strengthLabel.textContent = '';
  if (!value) return;

  const strength = getPasswordStrength(value);
  strengthBar.classList.add(strength);
  strengthLabel.textContent = `Password strength: ${strength[0].toUpperCase()}${strength.slice(1)}`;
}

function validatePassword() {
  const value = inputs.password.value;
  const isValid = value.length >= 8;
  return setFieldState('password', isValid, 'Password must be at least 8 characters');
}

function validateConfirmPassword() {
  const isValid = inputs.confirmPassword.value === inputs.password.value &&
                   inputs.confirmPassword.value.length > 0;
  return setFieldState('confirmPassword', isValid, 'Passwords do not match');
}

// Live validation as the user types/selects
inputs.fullName.addEventListener('input', validateFullName);
inputs.email.addEventListener('input', validateEmail);
inputs.phone.addEventListener('input', validatePhone);
inputs.dob.addEventListener('change', validateDob);
inputs.gender.addEventListener('change', validateGender);
inputs.password.addEventListener('input', () => {
  updateStrengthMeter();
  validatePassword();
  if (inputs.confirmPassword.value) validateConfirmPassword();
});
inputs.confirmPassword.addEventListener('input', validateConfirmPassword);

// Final check on submit
form.addEventListener('submit', function (event) {
  event.preventDefault();
  successMsg.classList.remove('visible');

  const results = [
    validateFullName(),
    validateEmail(),
    validatePhone(),
    validateDob(),
    validateGender(),
    validatePassword(),
    validateConfirmPassword()
  ];

  const allValid = results.every(Boolean);
  if (allValid) {
    successMsg.classList.add('visible');
  } else {
    const firstInvalid = fields.find(id => inputs[id].classList.contains('input-error'));
    if (firstInvalid) inputs[firstInvalid].focus();
  }
});
