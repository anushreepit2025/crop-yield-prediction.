# 🌾 Crop Yield Prediction — Master Plan

**Course:** ITS305 – Machine Learning | **Team:** Anushree P (210425205014), Jananisri V (210425205060) | **Supervisor:** Nithya Baskaran

---

## 1. Project Analysis (from the current PPT)

| Slide | What it says | Gap to fill before building |
|---|---|---|
| Introduction | Agriculture matters, yield depends on many factors, ML improves accuracy | No specific crops/regions named |
| Problem Statement | Farmers can't predict yield, climate change, traditional methods weak | No dataset source cited |
| Project Description | Uses historical data, ML algorithms, soil/weather factors | No algorithm named, no architecture |
| Aim & Scope | Predict yield, support decisions, real-time extension mentioned | This is exactly what the web app should deliver |

**Conclusion:** the deck sets up the *why*, not the *how*. The web application is your chance to show the *how* — this plan turns the four bullet-point slides into a real, demoable product.

---

## 2. Recommended Tech Stack

| Layer | Choice | Why |
|---|---|---|
| Frontend | React + Tailwind CSS | Fast to build, clean dashboards, easy charts |
| Backend / API | Python + FastAPI (or Flask) | Native fit with ML libraries, async, auto-generated docs |
| ML Model | scikit-learn (Random Forest / XGBoost) baseline, optional LSTM for time-series weather | RF/XGBoost handle tabular agri-data well and are explainable |
| Database | PostgreSQL or SQLite (for demo) | Store historical yield, soil, weather records |
| Deployment | Render / Railway (backend) + Vercel/Netlify (frontend) | Free tiers, quick for a college project |
| Data Source | Kaggle "Crop Yield Prediction" dataset, data.gov.in agri stats, or Open-Meteo API for live weather | Real, citable data strengthens the report |

---

## 3. Core Features (map directly to your slides)

1. **Yield Prediction Form** — user enters state/district, crop, season, area, rainfall, temperature, soil type → model returns predicted yield (tons/hectare).
2. **Historical Data Explorer** — charts of past yield trends by crop/region (addresses "Uses historical agricultural data").
3. **Factor Analysis Dashboard** — visualize how rainfall, temperature, soil pH correlate with yield (addresses "Analyzes factors like soil and weather").
4. **Model Confidence / Accuracy Panel** — show R², RMSE, MAE so the prediction isn't a black box.
5. **Recommendation Engine** — simple rule-based tips ("increase irrigation by X%") layered on top of the ML output.

## 4. Additional Features (to make it stand out)

| Feature | Impact |
|---|---|
| 🌦️ **Live weather API integration** | Auto-fill temperature/rainfall instead of manual entry — realizes the "can be extended with real-time data" line directly |
| 🗺️ **Interactive map (India districts)** | Click a district → auto-load its historical averages |
| 📊 **Crop comparison tool** | Compare predicted yield of 2–3 crops for the same land to help decision-making |
| 🔔 **Risk alerts** | Flag low-yield-risk conditions (drought/excess rain) using threshold rules |
| 📈 **What-if simulator** | Slider for rainfall/fertilizer → live-updates predicted yield (great demo feature) |
| 🌐 **Multilingual UI (English/Tamil)** | Real relevance for farmer end-users |
| 📱 **PWA / mobile-responsive** | Usable in the field on a phone |
| 🔒 **Farmer login + saved fields** | Persist their land profile, revisit predictions |
| 📤 **Export report (PDF)** | Downloadable prediction report — ties back nicely to your ML course deliverable |
| 🤖 **Chatbot / Q&A assistant** | Answer basic farming queries using an LLM API, optional stretch goal |

---

## 5. System Architecture

```
[React Frontend]
     │  (REST calls)
     ▼
[FastAPI Backend] ── /predict, /history, /weather, /report
     │
     ├── [Trained ML Model .pkl] (scikit-learn)
     ├── [PostgreSQL DB] (historical yield, soil, user data)
     └── [Weather API] (Open-Meteo / OpenWeather)
```

---

## 6. Step-by-Step Implementation Plan

### Phase 1 — Data & Model (Week 1–2)
1. Collect dataset (Kaggle crop yield dataset / state agri department data).
2. Clean data: handle missing values, encode categorical (crop, season, state).
3. EDA: correlation heatmap of rainfall/temp/soil vs yield (use for your PPT's "Analysis" slide too).
4. Train baseline models: Linear Regression → Random Forest → XGBoost; compare R²/RMSE.
5. Select best model, save as `model.pkl` with `joblib`.

### Phase 2 — Backend API (Week 2–3)
6. Set up FastAPI project structure (`/app`, `/models`, `/routes`).
7. Build `/predict` endpoint: accepts JSON (crop, area, rainfall, temp, soil), returns predicted yield + confidence.
8. Build `/history` endpoint: returns historical yield data for charts.
9. Integrate weather API for auto-fetch by district/coordinates.
10. Add PostgreSQL models for storing user inputs & predictions (for the report/export feature).

### Phase 3 — Frontend (Week 3–4)
11. Scaffold React app, set up Tailwind, routing (Home / Predict / Dashboard / History / Login).
12. Build prediction form with live validation.
13. Build results panel: predicted yield, confidence interval, recommendation text.
14. Build dashboard: charts (line/bar) using Recharts for historical trends and factor correlations.
15. Add the what-if simulator (sliders → re-call `/predict` on change, debounce for performance).
16. Add map view (Leaflet + India GeoJSON) for district selection.

### Phase 4 — Polish & Extras (Week 4–5)
17. Add PDF export of prediction report (backend: reportlab/weasyprint).
18. Add login/auth (JWT) + saved field profiles.
19. Add Tamil/English toggle (i18next).
20. Responsive/mobile pass, accessibility check.

### Phase 5 — Deployment & Demo (Week 5–6)
21. Deploy backend (Render/Railway), frontend (Vercel).
22. Load-test `/predict`, fix latency issues (cache model in memory, not reload per request).
23. Prepare demo script: enter real district → show prediction → run what-if simulator live → export report.
24. Update the PPT: add screenshots, architecture diagram, model accuracy metrics, and a "Results" slide — this is what will most improve your project's grade over the current deck.

---

## 7. Evaluation Metrics to Report

- **R² Score**, **RMSE**, **MAE** for the regression model
- Feature importance chart (which factors matter most — great visual for your final presentation)
- Comparison table: Linear Regression vs Random Forest vs XGBoost

---

## 8. Suggested Repo Structure

```
crop-yield-prediction/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── routes/ (predict.py, history.py, weather.py)
│   │   ├── models/ (schema.py, model.pkl)
│   │   └── db/
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── pages/ (Home, Predict, Dashboard, History, Login)
│   │   ├── components/
│   │   └── App.jsx
│   └── package.json
├── ml/
│   ├── data/ (raw, cleaned)
│   ├── notebooks/ (EDA.ipynb, training.ipynb)
│   └── train_model.py
└── README.md
```

---

## 9. Immediate Next Steps

1. Confirm/find the dataset you'll use (I can help pull a suitable one).
2. Decide scope: full-stack build vs. Streamlit-only quick prototype (faster if the deadline is tight).
3. I can scaffold either the FastAPI backend or a Streamlit MVP right now if you want working code instead of just the plan.
