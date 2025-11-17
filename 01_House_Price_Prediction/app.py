import streamlit as st
import pandas as pd
import joblib

# Load saved model
model = joblib.load('house_price_model.pkl')

st.title("🏠 House Price Prediction App")
st.write("Enter the house details below to predict its price:")

# Create two columns
col1, col2 = st.columns(2)

# Left column inputs
with col1:
    bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)
    bathrooms = st.number_input("Bathrooms", min_value=1.0, max_value=6.0, value=2.0, step=0.25)
    sqft_living = st.number_input("Living Area (sqft)", min_value=300, max_value=10000, value=1500)
    floors = st.number_input("Floors", min_value=1.0, max_value=3.5, value=1.0, step=0.5)

# Right column inputs
with col2:
    condition = st.number_input("Condition (1–5)", min_value=1, max_value=5, value=3)
    city = st.selectbox("City", ['Shoreline', 'Kent', 'Bellevue', 'Redmond', 'Seattle',
       'Maple Valley', 'North Bend', 'Lake Forest Park', 'Sammamish',
       'Auburn', 'Des Moines', 'Bothell', 'Federal Way', 'Kirkland',
       'Issaquah', 'Woodinville', 'Normandy Park', 'other', 'Renton',
       'Carnation', 'Snoqualmie', 'Duvall', 'Burien', 'Covington',
       'Kenmore', 'Newcastle', 'Mercer Island', 'Tukwila', 'Vashon',
       'SeaTac', 'Enumclaw'])
    house_age = st.number_input("House Age (years)", min_value=0, max_value=150, value=50)
    city_code = st.number_input("City Code", min_value=98001, max_value=98399, value=98133)

# Predict button
if st.button("Predict Price"):
    input_data = pd.DataFrame({
        'bedrooms': [bedrooms],
        'bathrooms': [bathrooms],
        'sqft_living': [sqft_living],
        'floors': [floors],
        'condition': [condition],
        'city': [city],
        'House_Age': [house_age],
        'city_code': [city_code]
    })

    prediction = model.predict(input_data)[0]
    st.success(f"💰 Estimated House Price: ${prediction:,.0f}")
