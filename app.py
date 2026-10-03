import streamlit as st
import requests
import json
import pandas as pd
import numpy as np
from fpdf import FPDF

# API URL for FastAPI backend
API_BASE_URL = "http://localhost:8000"

st.set_page_config(
    page_title="Crop Yield Predictor",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 Crop Yield Prediction Dashboard")
st.markdown("Predict crop yields, analyze historical trends, and make informed agricultural decisions.")

# Initialize session state for authentication and weather
if "token" not in st.session_state:
    st.session_state.token = None
if "rainfall" not in st.session_state:
    st.session_state.rainfall = 800.0
if "temperature" not in st.session_state:
    st.session_state.temperature = 28.0

# Sidebar - Authentication
st.sidebar.title("Authentication")
if st.session_state.token is None:
    auth_mode = st.sidebar.radio("Mode", ["Login", "Register"])
    
    if auth_mode == "Login":
        with st.sidebar.form("login_form"):
            username = st.text_input("Email (Username)")
            password = st.text_input("Password", type="password")
            submit_login = st.form_submit_button("Login")
            
        if submit_login:
            try:
                response = requests.post(
                    f"{API_BASE_URL}/api/auth/login",
                    data={"username": username, "password": password}
                )
                if response.status_code == 200:
                    st.session_state.token = response.json().get("access_token")
                    st.success("Logged in successfully!")
                    st.rerun()
                else:
                    st.error("Invalid credentials.")
            except Exception as e:
                st.error(f"Could not connect to backend: {e}")
                
    else:
        with st.sidebar.form("register_form"):
            new_name = st.text_input("Name")
            new_email = st.text_input("Email")
            new_password = st.text_input("Password", type="password")
            submit_register = st.form_submit_button("Register")
            
        if submit_register:
            try:
                response = requests.post(
                    f"{API_BASE_URL}/api/auth/register",
                    json={"name": new_name, "email": new_email, "password": new_password}
                )
                if response.status_code == 200:
                    st.success("Account created! You can now log in.")
                else:
                    st.error(f"Error: {response.text}")
            except Exception as e:
                st.error(f"Could not connect to backend: {e}")
else:
    st.sidebar.success("You are logged in.")
    if st.sidebar.button("Logout"):
        st.session_state.token = None
        st.rerun()

# Tabs
tab1, tab2, tab3 = st.tabs(["🔮 Yield Prediction", "📈 Historical Data", "🧪 Simulator"])

with tab1:
    st.header("Predict Crop Yield")
    
    col1, col2 = st.columns(2)
    
    with col1:
        state = st.text_input("State", value="Tamil Nadu")
        district = st.selectbox("District", ["Coimbatore", "Madurai", "Bangalore", "Pune", "Lucknow", "Other"])
        if district == "Other":
            district = st.text_input("Enter District Name", value="Chennai")
            
        # Map visualization
        DISTRICT_COORDS = {
            "Coimbatore": [11.0168, 76.9558],
            "Madurai": [9.9252, 78.1198],
            "Bangalore": [12.9716, 77.5946],
            "Pune": [18.5204, 73.8567],
            "Lucknow": [26.8467, 80.9462],
        }
        coords = DISTRICT_COORDS.get(district, [20.5937, 78.9629])
        map_df = pd.DataFrame({'latitude': [coords[0]], 'longitude': [coords[1]]})
        st.map(map_df, zoom=5, use_container_width=True)

        season = st.selectbox("Season", ["Kharif", "Rabi", "Whole Year"])
        crop = st.text_input("Crop", value="Rice")
        soil_type = st.selectbox("Soil Type", ["Alluvial", "Black", "Red", "Clay", "Sandy"])
        
    with col2:
        area = st.number_input("Area (Hectares)", min_value=0.1, value=5.0)
        
        st.markdown("---")
        if st.button("🌤️ Auto-Fetch Live Weather for District"):
            try:
                res = requests.get(f"{API_BASE_URL}/api/weather/{district}")
                if res.status_code == 200:
                    data = res.json()
                    st.session_state.rainfall = float(data["rainfall_est"])
                    st.session_state.temperature = float(data["temperature_avg"])
                    st.rerun()
                else:
                    st.error("Could not fetch weather data")
            except Exception as e:
                st.error(f"Error connecting to API: {e}")
                
        rainfall = st.number_input("Rainfall (mm)", min_value=0.0, key="rainfall")
        temperature = st.number_input("Temperature (°C)", min_value=-10.0, max_value=55.0, key="temperature")
        st.markdown("---")
        
        save_log = st.checkbox("Save Prediction Log", value=True)
        
    if st.button("Predict Yield 🚀"):
        if st.session_state.token is None:
            st.warning("Please log in from the sidebar to make a prediction.")
        else:
            payload = {
                "state": state,
                "district": district,
                "season": season,
                "crop": crop,
                "area": area,
                "rainfall": rainfall,
                "temperature": temperature,
                "soil_type": soil_type,
                "save_log": save_log
            }
            
            headers = {"Authorization": f"Bearer {st.session_state.token}"}
            
            try:
                with st.spinner("Predicting..."):
                    res = requests.post(f"{API_BASE_URL}/api/predict", json=payload, headers=headers)
                
                if res.status_code == 200:
                    data = res.json()
                    st.success("Prediction Successful!")
                    
                    # Display Results
                    r_col1, r_col2, r_col3 = st.columns(3)
                    r_col1.metric("Predicted Yield (tons/ha)", f"{data['predicted_yield']:.2f}")
                    r_col2.metric("Total Production (tons)", f"{data['production']:.2f}")
                    r_col3.metric("Confidence Interval", f"[{data['confidence_lower']:.2f}, {data['confidence_upper']:.2f}]")
                    
                    if "recommendations" in data and data["recommendations"]:
                        st.info(f"💡 Recommendation: {data['recommendations']}")
                        
                    # Generate PDF Report
                    pdf = FPDF()
                    pdf.add_page()
                    pdf.set_font("Arial", size=15)
                    pdf.cell(200, 10, txt="Crop Yield Prediction Report", ln=1, align='C')
                    pdf.ln(10)
                    pdf.set_font("Arial", size=12)
                    pdf.cell(200, 10, txt=f"Location: {payload['district']}, {payload['state']}", ln=1)
                    pdf.cell(200, 10, txt=f"Crop: {payload['crop']} | Season: {payload['season']}", ln=1)
                    pdf.cell(200, 10, txt=f"Area: {payload['area']} ha | Soil: {payload['soil_type']}", ln=1)
                    pdf.cell(200, 10, txt=f"Rainfall: {payload['rainfall']} mm | Temp: {payload['temperature']} C", ln=1)
                    pdf.ln(5)
                    pdf.set_font("Arial", 'B', 14)
                    pdf.cell(200, 10, txt=f"Predicted Yield: {data['predicted_yield']:.2f} tons/ha", ln=1)
                    pdf.cell(200, 10, txt=f"Total Production: {data['production']:.2f} tons", ln=1)
                    
                    pdf_bytes = pdf.output(dest='S').encode('latin-1')
                    st.download_button(
                        label="📄 Download PDF Report",
                        data=pdf_bytes,
                        file_name=f"Yield_Report_{payload['district']}.pdf",
                        mime="application/pdf"
                    )
                        
                else:
                    st.error(f"Error: {res.text}")
            except Exception as e:
                st.error(f"Failed to connect to the API: {e}")

with tab2:
    st.header("Historical Yield Trends")
    st.markdown("Simulated dashboard for historical yield exploration.")
    
    # Generate some dummy data for visualization
    years = list(range(2010, 2024))
    yield_data = [np.random.normal(3.5, 0.5) for _ in years]
    
    df = pd.DataFrame({
        "Year": years,
        "Yield (tons/ha)": yield_data
    })
    
    st.line_chart(df.set_index("Year"))
    
with tab3:
    st.header("What-If Simulator")
    st.markdown("Adjust rainfall and temperature to see how the predicted yield changes for a standard baseline (e.g., Rice in Coimbatore, 5 Hectares).")
    
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        sim_crop = st.selectbox("Crop", ["Rice", "Wheat", "Maize"], key="sim_crop")
        sim_area = st.number_input("Area (Hectares)", min_value=0.1, value=5.0, key="sim_area")
    with col_s2:
        sim_rainfall = st.slider("Rainfall (mm)", 0, 3000, 800, key="sim_rain")
        sim_temp = st.slider("Temperature (°C)", 10, 50, 28, key="sim_temp")
    
    if st.button("Run Simulation 🧪"):
        if st.session_state.token is None:
            st.warning("Please log in from the sidebar to run simulations.")
        else:
            payload = {
                "state": "Tamil Nadu",
                "district": "Coimbatore",
                "season": "Kharif",
                "crop": sim_crop,
                "area": sim_area,
                "rainfall": sim_rainfall,
                "temperature": sim_temp,
                "soil_type": "Black",
                "save_log": False
            }
            
            headers = {"Authorization": f"Bearer {st.session_state.token}"}
            try:
                with st.spinner("Simulating..."):
                    res = requests.post(f"{API_BASE_URL}/api/predict", json=payload, headers=headers)
                
                if res.status_code == 200:
                    data = res.json()
                    st.success("Simulation Complete!")
                    
                    r_col1, r_col2 = st.columns(2)
                    r_col1.metric("Predicted Yield", f"{data['predicted_yield']:.2f} tons/ha", delta_color="normal")
                    r_col2.metric("Total Production", f"{data['production']:.2f} tons", delta_color="normal")
                    
                    if "recommendations" in data and data["recommendations"]:
                        st.info(f"💡 Recommendation: {data['recommendations']}")
                else:
                    st.error(f"Error: {res.text}")
            except Exception as e:
                st.error(f"Failed to connect to the API: {e}")

