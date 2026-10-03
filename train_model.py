import pandas as pd
import numpy as np
import os
import json
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import xgboost as xgb

def train_and_evaluate():
    data_path = 'data/cleaned/cleaned_crop_data.csv'
    if not os.path.exists(data_path):
        print(f"Error: Data file not found at {data_path}")
        return
        
    print("Loading data...")
    df = pd.read_csv(data_path)
    
    # Features and Target
    # We want to predict Yield (tons/hectare). We will use State_Name, District_Name, Season, Crop, Rainfall, Temperature, Soil_Type
    features = ['State_Name', 'District_Name', 'Season', 'Crop', 'Rainfall', 'Temperature', 'Soil_Type']
    target = 'Yield'
    
    X = df[features]
    y = df[target]
    
    # Preprocessing
    print("Preprocessing data...")
    label_encoders = {}
    X_encoded = X.copy()
    
    categorical_cols = ['State_Name', 'District_Name', 'Season', 'Crop', 'Soil_Type']
    for col in categorical_cols:
        le = LabelEncoder()
        X_encoded[col] = le.fit_transform(X[col])
        label_encoders[col] = le
        
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)
    
    # Scale numerical features (optional for trees, but good practice)
    scaler = StandardScaler()
    num_cols = ['Rainfall', 'Temperature']
    X_train[num_cols] = scaler.fit_transform(X_train[num_cols])
    X_test[num_cols] = scaler.transform(X_test[num_cols])
    
    # 1. Random Forest
    print("\nTraining Random Forest...")
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    rf_preds = rf_model.predict(X_test)
    
    print("Random Forest Results:")
    print(f"R2 Score: {r2_score(y_test, rf_preds):.4f}")
    print(f"RMSE: {np.sqrt(mean_squared_error(y_test, rf_preds)):.4f}")
    
    # 2. XGBoost
    print("\nTraining XGBoost...")
    xgb_model = xgb.XGBRegressor(n_estimators=100, random_state=42)
    xgb_model.fit(X_train, y_train)
    xgb_preds = xgb_model.predict(X_test)
    
    print("XGBoost Results:")
    print(f"R2 Score: {r2_score(y_test, xgb_preds):.4f}")
    print(f"RMSE: {np.sqrt(mean_squared_error(y_test, xgb_preds)):.4f}")
    
    # Select Best Model (Assuming XGBoost or RF performs best, let's export XGBoost)
    best_model = xgb_model if r2_score(y_test, xgb_preds) > r2_score(y_test, rf_preds) else rf_model
    best_name = "XGBoost" if best_model == xgb_model else "Random Forest"
    print(f"\nBest Model: {best_name}")
    
    # Exporting artifacts
    print("Exporting model and preprocessors...")
    os.makedirs('../backend/app/trained_model', exist_ok=True)
    
    joblib.dump(best_model, '../backend/app/trained_model/model.pkl')
    joblib.dump(scaler, '../backend/app/trained_model/scaler.pkl')
    
    # Save label encoders mapping
    encoder_mapping = {}
    for col, le in label_encoders.items():
        encoder_mapping[col] = list(le.classes_)
        
    with open('../backend/app/trained_model/feature_config.json', 'w') as f:
        json.dump(encoder_mapping, f, indent=4)
        
    print("Training complete! Model artifacts saved to backend/app/trained_model/")

if __name__ == "__main__":
    train_and_evaluate()
