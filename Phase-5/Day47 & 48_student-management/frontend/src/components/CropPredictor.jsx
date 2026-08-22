import { useState } from "react";
import { predictCrop } from "../api";

const PRESETS = [
  {
    name: "Paddy / Rice",
    icon: "🌾",
    desc: "High moisture & rainfall",
    values: { N: 90, P: 42, K: 43, temperature: 20.88, humidity: 82.0, ph: 6.5, rainfall: 202.94 }
  },
  {
    name: "Tropical Banana",
    icon: "🍌",
    desc: "Warm & humid climate",
    values: { N: 100, P: 82, K: 50, temperature: 27.4, humidity: 80.3, ph: 5.9, rainfall: 104.6 }
  },
  {
    name: "Orchard Apple",
    icon: "🍎",
    desc: "High potassium & moderate rain",
    values: { N: 20, P: 130, K: 200, temperature: 22.5, humidity: 92.5, ph: 5.8, rainfall: 110.0 }
  },
  {
    name: "Coffee Plantation",
    icon: "☕",
    desc: "Balanced nitrogen & steady rain",
    values: { N: 100, P: 20, K: 30, temperature: 26.5, humidity: 58.0, ph: 6.8, rainfall: 160.0 }
  }
];

const CROP_ICONS = {
  rice: "🌾",
  banana: "🍌",
  apple: "🍎",
  coffee: "☕",
  maize: "🌽",
  cotton: "🧶",
  mango: "🥭",
  orange: "🍊",
  papaya: "🍈",
  coconut: "🥥",
  grapes: "🍇",
  watermelon: "🍉",
  muskmelon: "🍈",
  jute: "🌿",
  chickpea: "🌱",
  kidneybeans: "🫘",
  pigeonpeas: "🌱",
  mothbeans: "🌱",
  mungbean: "🌱",
  blackgram: "🌱",
  lentil: "🌱",
  pomegranate: "🫐"
};

export default function CropPredictor() {
  const [form, setForm] = useState({
    N: "90",
    P: "42",
    K: "43",
    temperature: "20.88",
    humidity: "82.0",
    ph: "6.5",
    rainfall: "202.94"
  });

  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  function handleChange(e) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  function applyPreset(preset) {
    const stringified = {};
    for (const key in preset.values) {
      stringified[key] = String(preset.values[key]);
    }
    setForm(stringified);
    setResult(null);
    setError(null);
  }

  async function handleSubmit(e) {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const payload = {
        N: parseFloat(form.N),
        P: parseFloat(form.P),
        K: parseFloat(form.K),
        temperature: parseFloat(form.temperature),
        humidity: parseFloat(form.humidity),
        ph: parseFloat(form.ph),
        rainfall: parseFloat(form.rainfall)
      };
      const prediction = await predictCrop(payload);
      setResult(prediction);
    } catch (err) {
      setError(err.message || "Failed to generate prediction");
    } finally {
      setLoading(false);
    }
  }

  const cropKey = result ? result.toLowerCase().trim() : "";
  const cropEmoji = CROP_ICONS[cropKey] || "🌱";

  return (
    <div className="ml-card">
      <div className="ml-header">
        <h2>
          <span>🌱</span> Smart Crop Recommendation AI
        </h2>
        <p className="subtitle">
          Intelligent agronomic recommendation engine powered by Random Forest machine learning inference.
        </p>
      </div>

      {/* Preset Profiles */}
      <div className="presets-section">
        <span className="presets-label">Benchmark Soil & Climate Presets</span>
        <div className="preset-grid">
          {PRESETS.map((preset) => (
            <button
              key={preset.name}
              type="button"
              className="preset-card"
              onClick={() => applyPreset(preset)}
            >
              <span className="preset-icon">{preset.icon}</span>
              <div className="preset-info">
                <strong>{preset.name}</strong>
                <span>{preset.desc}</span>
              </div>
            </button>
          ))}
        </div>
      </div>

      {/* Structured Prediction Form */}
      <form onSubmit={handleSubmit} className="ml-form">
        {/* Section 1: Soil Nutrients */}
        <div className="feature-group">
          <div className="group-title">
            <span>🧪</span> Soil Macronutrients (NPK)
          </div>
          <div className="fields-grid">
            <div className="field-item">
              <label className="field-label">
                Nitrogen (N)
                <span className="unit-tag">kg/ha</span>
              </label>
              <input
                type="number"
                step="any"
                name="N"
                value={form.N}
                onChange={handleChange}
                placeholder="e.g. 90"
                required
              />
            </div>

            <div className="field-item">
              <label className="field-label">
                Phosphorus (P)
                <span className="unit-tag">kg/ha</span>
              </label>
              <input
                type="number"
                step="any"
                name="P"
                value={form.P}
                onChange={handleChange}
                placeholder="e.g. 42"
                required
              />
            </div>

            <div className="field-item">
              <label className="field-label">
                Potassium (K)
                <span className="unit-tag">kg/ha</span>
              </label>
              <input
                type="number"
                step="any"
                name="K"
                value={form.K}
                onChange={handleChange}
                placeholder="e.g. 43"
                required
              />
            </div>
          </div>
        </div>

        {/* Section 2: Climate & Environment */}
        <div className="feature-group">
          <div className="group-title">
            <span>🌦️</span> Climate & Atmospheric Conditions
          </div>
          <div className="fields-grid">
            <div className="field-item">
              <label className="field-label">
                Temperature
                <span className="unit-tag">°C</span>
              </label>
              <input
                type="number"
                step="any"
                name="temperature"
                value={form.temperature}
                onChange={handleChange}
                placeholder="e.g. 24.5"
                required
              />
            </div>

            <div className="field-item">
              <label className="field-label">
                Relative Humidity
                <span className="unit-tag">% (0–100)</span>
              </label>
              <input
                type="number"
                step="any"
                min="0"
                max="100"
                name="humidity"
                value={form.humidity}
                onChange={handleChange}
                placeholder="e.g. 80.0"
                required
              />
            </div>
          </div>
        </div>

        {/* Section 3: Soil Acidity & Hydrology */}
        <div className="feature-group">
          <div className="group-title">
            <span>💧</span> Soil pH & Annual Precipitation
          </div>
          <div className="fields-grid">
            <div className="field-item">
              <label className="field-label">
                Soil pH Level
                <span className="unit-tag">scale 0–14</span>
              </label>
              <input
                type="number"
                step="any"
                min="0"
                max="14"
                name="ph"
                value={form.ph}
                onChange={handleChange}
                placeholder="e.g. 6.5"
                required
              />
            </div>

            <div className="field-item">
              <label className="field-label">
                Rainfall
                <span className="unit-tag">mm</span>
              </label>
              <input
                type="number"
                step="any"
                min="0"
                name="rainfall"
                value={form.rainfall}
                onChange={handleChange}
                placeholder="e.g. 202.9"
                required
              />
            </div>
          </div>
        </div>

        <button type="submit" className="btn-predict" disabled={loading}>
          {loading ? (
            <>
              <span className="spinner"></span> Running ML Inference...
            </>
          ) : (
            <>
              <span>⚡</span> Run Crop Recommendation Inference
            </>
          )}
        </button>
      </form>

      {error && (
        <div className="alert-box error" style={{ marginTop: "1.25rem" }} role="alert">
          <span>⚠️</span> {error}
        </div>
      )}

      {result && (
        <div className="prediction-hero" role="region" aria-live="polite">
          <div className="result-content">
            <div className="result-badge-icon">{cropEmoji}</div>
            <div className="result-meta">
              <span className="result-meta-label">Optimal Recommended Crop</span>
              <span className="result-crop-name">{result}</span>
            </div>
          </div>
          <span className="result-tag">High Yield Match</span>
        </div>
      )}
    </div>
  );
}
