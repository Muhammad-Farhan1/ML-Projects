import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load('car_price_model.pkl')

st.title("🚗 Car Price Prediction App")
st.write("Enter the car details below to predict its estimated price:")

# --- Create two columns ---
col1, col2 = st.columns(2)

# --- Input fields in two columns ---
with col1:
    manufacturer = st.selectbox("Brand", [
        'Toyota', 'Mercedes-Benz', 'BMW', 'Lexus', 'Honda', 'Ford', 'Chevrolet', 
        'Nissan', 'Audi', 'Hyundai', 'Kia', 'Volkswagen', 'Porsche', 'Mitsubishi',
        'Subaru', 'Mazda', 'Jeep', 'Land Rover', 'other'
    ])

    category = st.selectbox("Category", [
        'Sedan', 'SUV', 'Hatchback', 'Coupe', 'Convertible', 'Minivan', 
        'Pickup', 'Wagon', 'Crossover', 'Van', 'other'
    ])

    year = st.number_input("Manufacture Year", min_value=1990, max_value=2025, value=1990, step=1)

    
    leather_interior = st.selectbox("Leather Interior", ['No', 'Yes'])

    fuel_type = st.selectbox("Fuel Type", ['Petrol', 'Diesel', 'Hybrid'])

with col2:

    engine_volume = st.number_input("Engine Volume (Liters)", min_value=0.5, max_value=10.0, value=2.0, step=0.1)

    mileage = st.number_input("Mileage (Km)", min_value=0.0, max_value=500000.0, value=0.0, step=500.0)

    gear_type = st.selectbox("Gear Type", ['Manual', 'Automatic'])

    drive_wheels = st.selectbox("Drive Wheels", ['FWD', 'RWD', 'AWD'])

# --- Prediction button ---
if st.button("Predict Price"):
    input_data = pd.DataFrame({
        'Manufacturer': [manufacturer],
        'year': [year],
        'Category': [category],
        'Leather interior': [leather_interior],
        'Fuel type': [fuel_type],
        'Engine volume': [engine_volume],
        'Mileage(Km)': [mileage],
        'Gear Type': [gear_type],
        'Drive wheels': [drive_wheels]
    })

    try:
        prediction = model.predict(input_data)[0]
        st.success(f"💰 Estimated Car Price: ${prediction:,.2f}")
    except Exception as e:
        st.error(f"Prediction failed — please check input format.\nError: {str(e)}")
