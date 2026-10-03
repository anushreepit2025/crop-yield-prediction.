@echo off
echo ==========================================
echo Starting Crop Yield Prediction Project...
echo ==========================================

echo [1/2] Starting FastAPI Backend on port 8000...
start cmd /k "cd backend && ..\.venv\Scripts\activate && python -m uvicorn app.main:app --reload --port 8000"

echo [2/2] Starting Streamlit Frontend on port 8501...
start cmd /k "cd streamlit_app && ..\.venv\Scripts\activate && streamlit run app.py --server.port 8501"

echo.
echo Project started! The Streamlit interface should open in your browser shortly.
echo If it doesn't open automatically, go to: http://localhost:8501
echo To stop the servers later, simply close the two black terminal windows that just opened.
echo.
pause
