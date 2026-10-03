import pandas as pd
import numpy as np
import os

def generate_synthetic_agri_data(num_records=10000):
    states = ['Tamil Nadu', 'Karnataka', 'Maharashtra', 'Punjab', 'Uttar Pradesh', 'Gujarat']
    districts = {
        'Tamil Nadu': ['Coimbatore', 'Madurai', 'Trichy', 'Salem'],
        'Karnataka': ['Bangalore', 'Mysore', 'Hubli', 'Mangalore'],
        'Maharashtra': ['Pune', 'Nagpur', 'Nashik', 'Aurangabad'],
        'Punjab': ['Ludhiana', 'Amritsar', 'Jalandhar', 'Patiala'],
        'Uttar Pradesh': ['Lucknow', 'Kanpur', 'Agra', 'Varanasi'],
        'Gujarat': ['Ahmedabad', 'Surat', 'Vadodara', 'Rajkot']
    }
    crops = ['Rice', 'Wheat', 'Maize', 'Sugarcane', 'Cotton', 'Groundnut']
    seasons = ['Kharif', 'Rabi', 'Summer', 'Whole Year']
    soil_types = ['Alluvial', 'Black', 'Red', 'Laterite', 'Loamy']

    data = []
    
    np.random.seed(42)
    
    for _ in range(num_records):
        state = np.random.choice(states)
        district = np.random.choice(districts[state])
        crop = np.random.choice(crops)
        season = np.random.choice(seasons)
        soil = np.random.choice(soil_types)
        
        # Area in hectares
        area = np.random.uniform(1, 1000)
        
        # Environmental factors based loosely on region/season
        rainfall = np.random.uniform(500, 3000) # mm
        temperature = np.random.uniform(20, 35) # Celsius
        
        # Base yield calculation (tons per hectare)
        base_yield = {
            'Rice': 3.5,
            'Wheat': 3.0,
            'Maize': 2.5,
            'Sugarcane': 70.0,
            'Cotton': 0.5,
            'Groundnut': 1.5
        }[crop]
        
        # Introduce variations
        temp_effect = 1.0 - abs(temperature - 28) * 0.02
        rain_effect = 1.0 if (rainfall > 800 and rainfall < 2000) else 0.8
        soil_effect = np.random.uniform(0.9, 1.1)
        
        noise = np.random.uniform(0.8, 1.2)
        
        actual_yield = base_yield * temp_effect * rain_effect * soil_effect * noise
        actual_yield = max(0.1, actual_yield) # Ensure positive yield
        
        production = actual_yield * area
        
        data.append({
            'State_Name': state,
            'District_Name': district,
            'Crop_Year': np.random.randint(2010, 2024),
            'Season': season,
            'Crop': crop,
            'Area': round(area, 2),
            'Rainfall': round(rainfall, 2),
            'Temperature': round(temperature, 2),
            'Soil_Type': soil,
            'Yield': round(actual_yield, 3),
            'Production': round(production, 2)
        })
        
    df = pd.DataFrame(data)
    
    # Save to raw data folder
    output_dir = 'data/raw'
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, 'synthetic_crop_data.csv')
    df.to_csv(file_path, index=False)
    print(f"Generated {num_records} records of synthetic data at {file_path}")

if __name__ == '__main__':
    generate_synthetic_agri_data(10000)
