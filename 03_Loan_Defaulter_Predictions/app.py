import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load('loan_defaulter_model.pkl')

# --- Page Configuration ---
st.set_page_config(page_title="💳 Loan Defaulter Prediction App", layout="centered")

# --- App Title ---
st.title("💳 Loan Defaulter Prediction App")
st.write("Provide the customer details below to predict whether they are likely to default (Churn).")

# --- Input Fields with Help ---
gender = st.selectbox(
    "Gender", 
    ['Male', 'Female'],
    help="Encoded: e.g., Male or Female (ensure it matches the model's encoding)"
)

SeniorCitizen = st.selectbox(
    "Senior Citizen", 
    [0, 1],
    help="Encoded: 0 = No, 1 = Yes"
)

Partner = st.selectbox(
    "Has Partner", 
    [0, 1],
    help="Encoded: 0 = No partner, 1 = Has partner"
)

Dependents = st.selectbox(
    "Has Dependents", 
    [0, 1],
    help="Encoded: 0 = No dependents, 1 = Has dependents"
)

tenure = st.number_input(
    "Tenure (Months)", 
    min_value=0, max_value=100, value=12,
    help="Number of months the customer has stayed with the company"
)

PhoneService = st.selectbox(
    "Phone Service", 
    [0, 1],
    help="Encoded: 0 = No phone service, 1 = Has phone service"
)

MultipleLines = st.selectbox(
    "Multiple Lines", 
    ['No', 'Yes', 'No phone service'],
    help="Options: Customer with multiple lines or not"
)

InternetService = st.selectbox(
    "Internet Service", 
    ['DSL', 'Fiber optic', 'No'],
    help="Type of internet connection the customer uses"
)

OnlineSecurity = st.selectbox(
    "Online Security", 
    ['No', 'Yes', 'No internet service'],
    help="Whether the customer has online security add-on"
)

OnlineBackup = st.selectbox(
    "Online Backup", 
    ['No', 'Yes', 'No internet service'],
    help="Whether the customer uses online backup service"
)

DeviceProtection = st.selectbox(
    "Device Protection", 
    ['No', 'Yes', 'No internet service'],
    help="Whether the customer has device protection service"
)

TechSupport = st.selectbox(
    "Tech Support", 
    ['No', 'Yes', 'No internet service'],
    help="Whether the customer has tech support service"
)

StreamingTV = st.selectbox(
    "Streaming TV", 
    ['No', 'Yes', 'No internet service'],
    help="Whether the customer subscribes to streaming TV"
)

StreamingMovies = st.selectbox(
    "Streaming Movies", 
    ['No', 'Yes', 'No internet service'],
    help="Whether the customer subscribes to streaming movies"
)

Contract = st.selectbox(
    "Contract Type", 
    ['Month-to-month', 'One year', 'Two year'],
    help="Type of contract: shorter contracts usually indicate higher churn risk"
)

PaperlessBilling = st.selectbox(
    "Paperless Billing", 
    [0, 1],
    help="Encoded: 0 = No, 1 = Yes (whether billing is paperless)"
)

PaymentMethod = st.selectbox(
    "Payment Method", 
    ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'],
    help="Customer’s preferred payment method"
)

MonthlyCharges = st.number_input(
    "Monthly Charges ($)", 
    min_value=0.0, max_value=200.0, value=70.0,
    help="The amount charged to the customer monthly"
)

TotalCharges = st.number_input(
    "Total Charges ($)", 
    min_value=0.0, max_value=10000.0, value=2000.0,
    help="Total amount charged to the customer over their tenure"
)

# --- Prediction Section ---
if st.button("🔮 Predict Loan Default"):
    input_data = pd.DataFrame({
        'gender': [gender],
        'SeniorCitizen': [SeniorCitizen],
        'Partner': [Partner],
        'Dependents': [Dependents],
        'tenure': [tenure],
        'PhoneService': [PhoneService],
        'MultipleLines': [MultipleLines],
        'InternetService': [InternetService],
        'OnlineSecurity': [OnlineSecurity],
        'OnlineBackup': [OnlineBackup],
        'DeviceProtection': [DeviceProtection],
        'TechSupport': [TechSupport],
        'StreamingTV': [StreamingTV],
        'StreamingMovies': [StreamingMovies],
        'Contract': [Contract],
        'PaperlessBilling': [PaperlessBilling],
        'PaymentMethod': [PaymentMethod],
        'MonthlyCharges': [MonthlyCharges],
        'TotalCharges': [TotalCharges]
    })

    # Predict using the model
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ This customer is **likely to default (Churn)**.")
    else:
        st.success("✅ This customer is **not likely to default**.")
