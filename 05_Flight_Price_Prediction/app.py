import streamlit as st
import pandas as pd
import joblib

# --- Load Trained Model ---
model = joblib.load('flight_price_prediction_model.pkl')  # make sure this file is in the same folder

# --- Streamlit App Setup ---
st.set_page_config(page_title="✈️ Flight Price Prediction App", layout="centered")
st.title("✈️ Flight Price Prediction App")
st.write("Enter flight details below to estimate the ticket price:")

# --- Input Fields with Help Text ---
airline = st.selectbox(
    "Airline",
    ['SpiceJet', 'AirAsia', 'Vistara', 'Indigo', 'GO_FIRST', 'Air_India'],
    help="Select the airline for your flight."
)

source_city = st.selectbox(
    "Source City",
    ['Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Chennai', 'Hyderabad'],
    help="Select the city from where your flight departs."
)

destination_city = st.selectbox(
    "Destination City",
    ['Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Chennai', 'Hyderabad'],
    help="Select your destination city."
)

departure_time = st.selectbox(
    "Departure Time",
    ['Early_Morning', 'Morning', 'Afternoon', 'Evening', 'Night', 'Late_Night'],
    help="Select when your flight departs."
)

arrival_time = st.selectbox(
    "Arrival Time",
    ['Early_Morning', 'Morning', 'Afternoon', 'Evening', 'Night', 'Late_Night'],
    help="Select when your flight arrives."
)

stops = st.selectbox(
    "Number of Stops",
    ['zero', 'one', 'two_or_more'],
    help="Choose how many stops your flight has."
)

flight_class = st.selectbox(
    "Travel Class",
    ['Economy', 'Business'],
    help="Select your travel class (Economy or Business)."
)

duration = st.number_input(
    "⏱Duration (in hours)",
    min_value=0.0, max_value=50.0, step=0.1,
    help="Enter total flight duration in hours."
)

days_left = st.number_input(
    "Days Left Before Departure",
    min_value=0, max_value=365, step=1,
    help="Number of days left until the flight date."
)

# --- Prediction Button ---
if st.button("Predict Price 💰"):
    # Create input dataframe
    input_data = pd.DataFrame({
        'airline': [airline],
        'source_city': [source_city],
        'departure_time': [departure_time],
        'stops': [stops],
        'arrival_time': [arrival_time],
        'destination_city': [destination_city],
        'class': [flight_class],
        'duration': [duration],
        'days_left': [days_left]
    })

    # Make prediction
    prediction = model.predict(input_data)[0]

    st.success(f"💰 **Predicted Flight Price:** ₹{prediction:,.2f}")

# --- Footer ---
st.markdown("---")
st.caption("Developed by Farhan | Machine Learning Project: Flight Price Prediction")
