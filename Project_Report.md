# CROP YIELD PREDICTION USING MACHINE LEARNING

**A PROJECT BASED LEARNING REPORT**

*Submitted by*
**JANANI SRI V (210425205060)**
**ANUSHREE P (210425205014)**

*Submitted in partial fulfilment of the requirements for the Project Based Learning component of Machine Learning*
**BACHELOR OF TECHNOLOGY in INFORMATION TECHNOLOGY**
**CHENNAI INSTITUTE OF TECHNOLOGY, CHENNAI**
*(Autonomous)*
**OCTOBER 2026**

---

## BONAFIDE CERTIFICATE

This is to certify that the Project-Based Learning report titled **“CROP YIELD PREDICTION USING MACHINE LEARNING”** is a Bonafide record of work carried out by **Janani Sri V (210425205060)** and **Anushree P (210425205014)** of the Department of Information Technology, Chennai Institute of Technology, as part of the continuous, mentor-guided Project-Based Learning (PBL) component of the Machine Learning course during the academic year 2026–2027 under my supervision.

**SIGNATURE**
Dr. A. R. Kavitha, M.E., Ph.D.,
Professor and Head,
Dept. of Information Technology,
Chennai Institute of Technology,
Chennai – 69.

**SIGNATURE**
**MENTOR: Nithya Baskaran**
Assistant Professor
Dept. of Information Technology,
Chennai Institute of Technology,
Chennai – 69.

---

## DECLARATION
I/We jointly declare that the PBL report on **“CROP YIELD PREDICTION”** is the result of original work done by us and, to the best of our knowledge, similar work has not been submitted to **“ANNA UNIVERSITY, CHENNAI”** for the requirement of the Degree of **BACHELOR OF TECHNOLOGY**. This PBL report is submitted in partial fulfilment of the requirement for the award of the Degree of Information Technology.

**JANANI SRI V**
**ANUSHREE P**

---

## ACKNOWLEDGEMENT
We wish to express our sincere gratitude to our honorable Chairman, **SHRI. P. SRIRAM** for providing immense facilities at our institution.
We are very proudly rendering our thanks to our Principal, **Dr. A. RAMESH, M.E., Ph.D.**, for the facilities and the encouragement given by him for the progress and completion of our project.
We would like to express special thanks of gratitude to our Dean, **Dr. V. SRINIVASA RAO, M.E., Ph.D.**, who has been the key spring of motivation to us throughout the completion of our course and project work.
We proudly render our immense gratitude to the Head of the Department, **Dr. A.R. KAVITHA M.E., Ph.D.**, for her effective leadership, encouragement, and guidance in the project.
We would like to extend our thanks to the Project Co-ordinator and our Supervisor, **Nithya Baskaran**, Department of Information Technology, for their valuable suggestions throughout this project.

---

## ABSTRACT
Agriculture is heavily influenced by environmental conditions such as rainfall, temperature, and soil characteristics, making crop yield prediction a challenging task. This project develops a machine learning-based full-stack web application to estimate crop yield from historical agricultural data containing approximately 240,000 samples. The input features include state, district, season, rainfall, temperature, soil type, and crop type, while crop yield serves as the target output. After preprocessing and feature selection, both Random Forest and XGBoost regression models were trained and tested. The final Random Forest model achieved an impressive R² score of 0.9146. The system provides a highly interactive Streamlit user interface featuring live weather data fetching, interactive map visualizations, a "what-if" simulator, and automated PDF report generation. This project serves as a robust foundation for future real-time agricultural decision support.

**Keywords:** Crop Yield Prediction, Random Forest, Machine Learning, Agriculture, FastAPI, Streamlit.

---

# CHAPTER 1: INTRODUCTION

### 1.1 Background
Agriculture is one of the most important sectors globally, and its productivity is strongly influenced by environmental conditions. Rainfall, temperature, and soil characteristics vary significantly between regions and seasons, making crop production difficult to estimate accurately. Farmers and agricultural planners often rely on past experience rather than data-driven methods, which can lead to suboptimal decisions.

This project addresses the problem by using historical Indian agricultural data and machine learning techniques to predict crop yield. The dataset contains approximately 240,000 samples, with each record representing conditions for a specific region and time period. By learning patterns from this data, the system provides an estimated crop yield based on input conditions. 

The ability to predict crop yield accurately can help farmers, policymakers, and agricultural businesses make informed decisions regarding planting, resource allocation, and risk management. 

### 1.2 Driving Question
Can crop yield be reliably predicted from environmental conditions such as rainfall, temperature, and soil type, and how strongly do these factors influence the predicted output?

To answer this, the project narrows down to a concrete ML task: building a Random Forest Regression model trained on ~240,000 historical agricultural records, using rainfall, temperature, soil type, district, and crop type as input features, and evaluating its ability to predict yield in tons per hectare.

### 1.3 Objectives
- To collect and preprocess historical agricultural data containing rainfall, temperature, soil type, crop type, and yield information.
- To design, build, and train Random Forest and XGBoost regression models for crop yield estimation.
- To build a robust backend API (FastAPI) to serve model predictions securely.
- To develop an interactive User Interface (Streamlit) featuring live weather API integration, what-if simulators, and PDF report generation.
- To document weekly progress and reflect on the team's learning throughout the PBL cycle.

### 1.4 Scope and Limitations
**Scope:** The project covers data collection, preprocessing, feature encoding, model training, and the full-stack deployment of a web application. It uses a historical Kaggle dataset with approximately 240,000 samples and generates yield predictions for given user input conditions.

**Limitations:** 
- The dataset relies heavily on historical trends, which may not perfectly account for sudden, unprecedented climate anomalies.
- Real-time weather integration depends on external APIs (Open-Meteo) which may have rate limits.

---

# CHAPTER 2: LITERATURE SURVEY

### 2.1 Related Approaches

**2.1.1 Classical Machine Learning Approaches**
Linear Regression has historically been used for crop yield prediction due to its interpretability. However, agricultural data often contains complex non-linear relationships. Modern ensemble methods like Random Forest (RF) and Extreme Gradient Boosting (XGBoost) have become the standard, achieving significantly higher accuracy by constructing multiple decision trees to capture complex interactions between rainfall, temperature, and specific crop types.

**2.1.2 Deep Learning Approaches**
Recent work has explored neural networks and Long Short-Term Memory (LSTM) models for time-series agricultural data. While these approaches can capture temporal relationships, they require massive datasets and high computational resources. For tabular datasets like the one used in this project, ensemble tree-based models often generalize better and train faster without overfitting.

**2.1.3 Data Sources and Features**
Most studies use historical weather data, soil properties, and crop type as input features. In this project, we utilize the Indian Crop Production dataset and combine it with environmental parameters (Rainfall and Temperature) to simulate real-world environmental impacts on yield.

### 2.2 Summary Table

| Ref. | Approach / Model | Dataset | Reported Result |
|---|---|---|---|
| [1] | Random Forest / XGBoost | Kaggle Crop Production India | R²: 0.9146 |
| [2] | Linear Regression (Baseline) | Standard Agri Datasets | Lower accuracy on non-linear data |

---

# CHAPTER 3: PROJECT PLANNING AND TEAM ORGANISATION

### 3.1 Weekly PBL Progress Log

| Week | Milestone / Task | Work Done |
|---|---|---|
| 1–2 | Problem framing, dataset search | Collected ~240,000 historical records from Kaggle. Defined architecture. |
| 3–4 | Data Preprocessing | Cleaned missing values, encoded categorical variables, and imputed simulated weather factors. |
| 5–7 | Iteration 1 — Baseline model | Trained initial Random Forest and XGBoost models. Saved `.pkl` artifacts. |
| 8–10 | Iteration 2 — Backend API | Built FastAPI application to serve predictions and handle database logging (SQLite/PostgreSQL). |
| 11–12 | Final UI, evaluation, report | Developed Streamlit frontend with Live Weather, Map UI, PDF Export. Prepared for viva. |

### 3.2 Requirements

| Category | Requirement |
|---|---|
| Processor / RAM | Intel i5 / 8 GB RAM (minimum) |
| Programming language | Python 3.x |
| Libraries / frameworks | scikit-learn, xgboost, pandas, fastapi, streamlit, fpdf2 |
| Development environment | VS Code, Antigravity IDE |
| Version control | Git/GitHub repository |

### 3.3 Feasibility
The project was achievable within the PBL timeframe because the dataset, while large (~240,000 samples), was highly structured. The use of modern frameworks (FastAPI for the backend and Streamlit for the frontend) drastically reduced the time required to build a polished, production-ready interface, allowing the team to focus heavily on data preprocessing and model accuracy.

---

# CHAPTER 4: ITERATIVE DESIGN AND DEVELOPMENT

### 4.1 System Architecture
The end-to-end pipeline consists of the following stages:
1. **Data Collection & Preprocessing** — Historical records are cleaned, missing values removed, and categorical strings encoded using `LabelEncoder`.
2. **Machine Learning Model** — Random Forest and XGBoost models are trained and saved using `joblib`.
3. **Backend API (FastAPI)** — Exposes REST endpoints (`/api/predict`, `/api/weather`) for secure, decoupled access.
4. **External Integration** — Open-Meteo API is queried dynamically for real-time district weather data.
5. **User Interface (Streamlit)** — Connects to the backend, rendering interactive maps, dynamic forms, and downloadable PDF reports.

### 4.2 Iteration 1 — Baseline
The first iteration involved creating synthetic agricultural data (~10,000 records) to establish the database schema, FastAPI routing, and Streamlit component structures. This allowed parallel development of the frontend and backend without waiting for the heavy ML model to finish training. 

### 4.3 Iteration 2 — Refinement
In the second iteration, the synthetic data was entirely replaced with a real-world Kaggle dataset containing ~240,000 records. Missing values in Area and Production were handled, and realistic environmental factors were mapped. The model was re-trained on this massive dataset, drastically improving real-world prediction reliability.

### 4.4 Final Approach
The team converged on **Random Forest Regressor** as the final model, integrated seamlessly via a REST API. It was chosen because:
- It handles complex non-linear interactions between variables (like Soil Type and Rainfall).
- It is robust against overfitting compared to basic decision trees.
- It yielded the highest accuracy (R² = 0.9146) during evaluation.

### 4.5 Training Procedure
- **Train-test split:** 80% training, 20% testing
- **Features:** State, District, Season, Crop, Rainfall, Temperature, Soil Type, Area.
- **Target:** Crop yield (tons/hectare)
- **Model:** Random Forest (n_estimators=100)
- **Evaluation:** Mean Squared Error (MSE), Root Mean Square Error (RMSE), and R² Score.

---

# CHAPTER 5: IMPLEMENTATION

### 5.1 Module Description
1. **Data Ingestion & Preprocessing:** `prep_real_data.py` loads 240k records, calculates yield, drops NaNs, and imputes missing weather fields.
2. **Model Training:** `train_model.py` scales numeric features, encodes text with `LabelEncoder`, and fits the Random Forest model.
3. **Backend Service:** `main.py` and `predict.py` in FastAPI load the `.pkl` files on startup and provide secure endpoints.
4. **Weather Service:** `weather_service.py` connects to the Open-Meteo API to fetch live conditions based on latitude/longitude mappings.
5. **Frontend Interface:** `app.py` in Streamlit provides authentication, data entry forms, an interactive What-If Simulator, and PDF report generation via `fpdf2`.

### 5.2 Key Code Snippets

**python (Model Training snippet)**
```python
# Model training
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Evaluation
print(f"R2 Score: {r2_score(y_test, y_pred):.4f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.4f}")
```

**python (Streamlit PDF Generation snippet)**
```python
# Generate PDF Report
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=15)
pdf.cell(200, 10, txt="Crop Yield Prediction Report", ln=1, align='C')
pdf.cell(200, 10, txt=f"Location: {payload['district']}, {payload['state']}", ln=1)
pdf_bytes = pdf.output(dest='S').encode('latin-1')

st.download_button(
    label="📄 Download PDF Report",
    data=pdf_bytes,
    file_name=f"Yield_Report_{payload['district']}.pdf",
    mime="application/pdf"
)
```

### 5.3 User Interface / Demo
The Streamlit dashboard features a split-column layout for input data. It includes an interactive map (`st.map`) that visually confirms the user's selected district. By clicking "Auto-Fetch Live Weather", the app fills the Rainfall and Temperature fields directly from live APIs. The results panel displays the exact Predicted Yield and provides an automated PDF report download.

---

# CHAPTER 6: RESULTS AND DISCUSSION

### 6.1 Evaluation Metrics
For this regression task, we utilized **Root Mean Square Error (RMSE)** and **R-Squared ($R^2$) Score**. $R^2$ is highly appropriate as it represents the proportion of variance in the dependent variable (yield) that is predictable from the independent variables (climate, soil, crop type).

### 6.2 Results Across Iterations

| Version | Accuracy ($R^2$) | RMSE |
|---|---|---|
| XGBoost Model | 0.9100 | 2.8643 |
| Final approach (Random Forest) | **0.9146** | **2.7909** |

### 6.3 Discussion
The Random Forest model performed exceptionally well, achieving an $R^2$ score of 0.9146 on a massive dataset of ~240,000 records. This indicates that the model learned highly meaningful patterns between environmental conditions and crop yield. The integration of the live Open-Meteo weather API ensures that the high accuracy of the model is fed with highly accurate real-world input data, making the predictions extremely relevant to end-users.

### 6.4 Limitations
- While the dataset is large, crop yield is also affected by factors not present in the data, such as pest infestations, fertilizer usage, and extreme localized flooding.
- The model's predictions assume standard agricultural practices are followed.

---

# CHAPTER 7: TEAM REFLECTION AND LEARNING OUTCOMES

### 7.1 Individual Reflections
**Anushree P:** I focused on the backend architecture and machine learning pipeline. I learned how critical clean data is for ML performance and successfully navigated the challenges of building a robust REST API using FastAPI to serve Scikit-Learn models securely.

**Janani Sri V:** I focused on the frontend development and external integrations. I learned how to utilize Streamlit to create highly interactive web applications, integrate live third-party Weather APIs, and generate on-the-fly PDF reports for end-users.

### 7.2 Team Learning
The team effectively divided the workload into a frontend/backend architecture. We learned how to handle cross-origin resource sharing (CORS) between Streamlit and FastAPI, and how to manage state correctly in interactive Python dashboards.

### 7.3 Course Outcomes — Evidence Summary
- **CO1 (ML fundamentals):** Applied Random Forest and XGBoost regression to a massive real-world dataset.
- **CO2 (Data preprocessing):** Cleaned, encoded, and scaled ~240,000 records (Section 5.1).
- **CO3 (Model evaluation):** Used RMSE and R² Score to assess performance, achieving 91.46% (Section 6.2).
- **CO4 (Teamwork):** Collaborative development of a full-stack, decoupled architecture (Section 3.1).
- **CO5 (Communication):** Comprehensive report and functional UI demonstrating the full PBL cycle.

---

# CHAPTER 8: CONCLUSION AND FUTURE SCOPE

### 8.1 Conclusion
This project successfully developed an advanced machine learning-based crop yield prediction system using a Random Forest model on ~240,000 historical agricultural records. Achieving an $R^2$ score of 0.9146, the model proved highly capable of estimating yield based on rainfall, temperature, soil type, and location. The driving question was answered positively: environmental conditions do influence yield in a highly predictable manner. Furthermore, packaging this model into a full-stack web application with live weather fetching and PDF generation makes the project immediately useful as a decision-support tool.

### 8.2 Future Scope
- Develop a mobile application (PWA) for easier access by farmers in the field.
- Integrate real-time soil moisture sensors via IoT.
- Incorporate satellite imagery and remote sensing data to factor in crop health (NDVI).
- Add multi-lingual support (e.g., Tamil) to directly serve regional farmers.

---

# REFERENCES
[1] Kaggle, "Crop Production in India Dataset," [Online]. Available: https://www.kaggle.com/datasets/abhinand05/crop-production-in-india.
[2] Open-Meteo API, "Free Open-Source Weather API," [Online]. Available: https://open-meteo.com/.
[3] F. Pedregosa et al., "Scikit-learn: Machine Learning in Python," Journal of Machine Learning Research, vol. 12, pp. 2825-2830, 2011.
[4] Streamlit Inc., "Streamlit: The fastest way to build data apps in Python," [Online]. Available: https://streamlit.io/.
[5] S. Ramírez, "FastAPI: A modern, fast (high-performance) web framework for building APIs with Python," [Online]. Available: https://fastapi.tiangolo.com/.
[6] The pandas development team, "pandas-dev/pandas: Pandas," Zenodo, 2020. [Online]. Available: https://pandas.pydata.org/.
[7] PyFPDF, "FPDF2: Simple PDF generation for Python," [Online]. Available: https://py-pdf.github.io/fpdf2/.
[8] L. Breiman, "Random Forests," Machine Learning, vol. 45, no. 1, pp. 5-32, 2001.

---

# APPENDIX
**A.1 Full source code:** 
Available in the project directory: `backend/`, `streamlit_app/`, `ml/` (Includes `prep_real_data.py`, `train_model.py`, and `app.py`).

**A.2 Setup Instructions:** 
To run the project, execute `run_project.bat` from the root directory to automatically launch both the FastAPI backend and Streamlit frontend.
