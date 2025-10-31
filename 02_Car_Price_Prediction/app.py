import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load('car_price_model.pkl')

st.title("🚗 Car Price Prediction App")
st.write("Enter the car details below to predict its estimated price:")

# --- Input fields ---
manufacturer = st.selectbox("Manufacturer", [
    'Toyota', 'Mercedes-Benz', 'BMW', 'Lexus', 'Honda', 'Ford', 'Chevrolet', 
    'Nissan', 'Audi', 'Hyundai', 'Kia', 'Volkswagen', 'Porsche', 'Mitsubishi',
    'Subaru', 'Mazda', 'Jeep', 'Land Rover', 'other'
])

year = st.number_input("Manufacture Year", min_value=1990, max_value=2025, value=2018)

category = st.selectbox("Category", [
    'Sedan', 'SUV', 'Hatchback', 'Coupe', 'Convertible', 'Minivan', 
    'Pickup', 'Wagon', 'Crossover', 'Van', 'other'
])

leather_interior = st.selectbox("Leather Interior", [0, 1], help="1 = Yes, 0 = No")
fuel_type = st.selectbox("Fuel Type", [0, 1, 2], help="Encoded: e.g., 0 = Petrol, 1 = Diesel, 2 = Hybrid (match your model encoding)")
engine_volume = st.number_input("Engine Volume (Liters)", min_value=0.5, max_value=10.0, value=2.0, step=0.1)
mileage = st.number_input("Mileage (Km)", min_value=0.0, max_value=500000.0, value=50000.0, step=500.0)
gear_type = st.selectbox("Gear Type", [0, 1], help="Encoded: e.g., 0 = Manual, 1 = Automatic (match your model encoding)")
drive_wheels = st.selectbox("Drive Wheels", [0, 1, 2], help="Encoded: e.g., 0 = FWD, 1 = RWD, 2 = AWD (match your model encoding)")

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
