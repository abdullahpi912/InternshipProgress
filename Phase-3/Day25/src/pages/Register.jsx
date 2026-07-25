import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';

export default function Register({ showToast }) {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    fullname: '',
    email: '',
    region: '',
    soilType: 'clayey',
    password: '',
    confirmPassword: '',
    terms: true
  });

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (formData.password !== formData.confirmPassword) {
      showToast?.('Passwords do not match! Please check again.', 'error');
      return;
    }
    showToast?.('Farm Profile created successfully! Welcome to AgriSense.', 'success');
    navigate('/dashboard');
  };

  return (
    <main>
      <section className="auth-section">
        <div className="auth-container">
          <div className="auth-card" style={{ maxWidth: '580px' }}>
            <div className="auth-header">
              <div className="auth-badge"><i className="fa-solid fa-user-plus"></i> Free Farm Account</div>
              <h2>Create Your Farm Profile</h2>
              <p>Register to securely store your field NPK logs, save historical crop ML predictions, and manage multi-plot data.</p>
            </div>

            <form className="auth-form" onSubmit={handleSubmit}>
              <div className="form-grid">
                <div className="form-field form-field-full">
                  <label htmlFor="fullname">Full Name / Farm Manager Name</label>
                  <div className="input-wrapper">
                    <input
                      type="text"
                      id="fullname"
                      name="fullname"
                      placeholder="e.g. Abdullah P I"
                      required
                      className="input-control"
                      value={formData.fullname}
                      onChange={handleChange}
                    />
                    <i className="fa-solid fa-user"></i>
                  </div>
                </div>

                <div className="form-field form-field-full">
                  <label htmlFor="email">Email Address</label>
                  <div className="input-wrapper">
                    <input
                      type="email"
                      id="email"
                      name="email"
                      placeholder="e.g. farmer@example.com"
                      required
                      className="input-control"
                      value={formData.email}
                      onChange={handleChange}
                    />
                    <i className="fa-solid fa-envelope"></i>
                  </div>
                </div>

                <div className="form-field">
                  <label htmlFor="region">Farm Location / District</label>
                  <div className="input-wrapper">
                    <input
                      type="text"
                      id="region"
                      name="region"
                      placeholder="e.g. Kerala, India"
                      required
                      className="input-control"
                      value={formData.region}
                      onChange={handleChange}
                    />
                    <i className="fa-solid fa-location-dot"></i>
                  </div>
                </div>

                <div className="form-field">
                  <label htmlFor="soilType">Primary Soil Type</label>
                  <div className="input-wrapper" style={{ position: 'relative' }}>
                    <select
                      id="soilType"
                      name="soilType"
                      className="input-control select-control"
                      required
                      style={{ paddingLeft: '2.75rem', width: '100%' }}
                      value={formData.soilType}
                      onChange={handleChange}
                    >
                      <option value="clayey">Clayey Soil</option>
                      <option value="loamy">Loamy Soil</option>
                      <option value="sandy">Sandy Soil</option>
                      <option value="alluvial">Alluvial Soil</option>
                      <option value="black">Black Cotton Soil</option>
                      <option value="red">Red / Laterite Soil</option>
                    </select>
                    <i className="fa-solid fa-mound" style={{ position: 'absolute', left: '1.1rem', top: '50%', transform: 'translateY(-50%)', color: 'var(--primary-light)' }}></i>
                  </div>
                </div>

                <div className="form-field">
                  <label htmlFor="password">Create Password</label>
                  <div className="input-wrapper">
                    <input
                      type="password"
                      id="password"
                      name="password"
                      placeholder="Min. 8 characters"
                      required
                      minLength={8}
                      className="input-control"
                      value={formData.password}
                      onChange={handleChange}
                    />
                    <i className="fa-solid fa-lock"></i>
                  </div>
                </div>

                <div className="form-field">
                  <label htmlFor="confirmPassword">Confirm Password</label>
                  <div className="input-wrapper">
                    <input
                      type="password"
                      id="confirmPassword"
                      name="confirmPassword"
                      placeholder="Re-enter password"
                      required
                      className="input-control"
                      value={formData.confirmPassword}
                      onChange={handleChange}
                    />
                    <i className="fa-solid fa-shield-check"></i>
                  </div>
                </div>
              </div>

              <div className="form-options" style={{ marginTop: '1rem' }}>
                <label className="checkbox-label" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', cursor: 'pointer' }}>
                  <input
                    type="checkbox"
                    name="terms"
                    required
                    checked={formData.terms}
                    onChange={handleChange}
                  />
                  <span>I agree to AgriSense Farm Advisory Terms and Data Privacy Policy</span>
                </label>
              </div>

              <div className="form-actions" style={{ marginTop: '1.5rem' }}>
                <button type="submit" className="btn btn-terracotta btn-block">
                  <i className="fa-solid fa-user-plus"></i> Register Farm Profile
                </button>
              </div>
            </form>

            <div className="auth-footer">
              <p>Already registered? <Link to="/login" className="auth-accent-link">Sign In to Existing Account <i className="fa-solid fa-arrow-right"></i></Link></p>
            </div>
          </div>
        </div>
      </section>
    </main>
  );
}
