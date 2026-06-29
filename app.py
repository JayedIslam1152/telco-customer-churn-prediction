import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("random_forest_model.pkl")

st.set_page_config(
    page_title="Telco Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Telco Customer Churn Prediction")

st.write(
    "Predict whether a telecom customer is likely to churn using a Machine Learning model."
)

st.header("Customer Information")

# -------------------------
# User Input
# -------------------------

gender = st.selectbox("Gender", ["Male", "Female"])
SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
Partner = st.selectbox("Partner", ["Yes", "No"])
Dependents = st.selectbox("Dependents", ["Yes", "No"])

tenure = st.slider(
    "Tenure (Months)",
    0,
    72,
    12
)

PhoneService = st.selectbox("Phone Service", ["Yes", "No"])

MultipleLines = st.selectbox(
    "Multiple Lines",
    ["No", "Yes", "No phone service"]
)

InternetService = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

OnlineSecurity = st.selectbox(
    "Online Security",
    ["No", "Yes", "No internet service"]
)

OnlineBackup = st.selectbox(
    "Online Backup",
    ["No", "Yes", "No internet service"]
)

DeviceProtection = st.selectbox(
    "Device Protection",
    ["No", "Yes", "No internet service"]
)

TechSupport = st.selectbox(
    "Tech Support",
    ["No", "Yes", "No internet service"]
)

StreamingTV = st.selectbox(
    "Streaming TV",
    ["No", "Yes", "No internet service"]
)

StreamingMovies = st.selectbox(
    "Streaming Movies",
    ["No", "Yes", "No internet service"]
)

Contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

PaperlessBilling = st.selectbox(
    "Paperless Billing",
    ["Yes", "No"]
)

PaymentMethod = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

MonthlyCharges = st.number_input(
    "Monthly Charges",
    0.0,
    200.0,
    70.0
)

TotalCharges = st.number_input(
    "Total Charges",
    0.0,
    10000.0,
    1000.0
)

# -------------------------
# Encoding
# -------------------------

gender = {"Female":0,"Male":1}[gender]
Partner = {"No":0,"Yes":1}[Partner]
Dependents = {"No":0,"Yes":1}[Dependents]
PhoneService = {"No":0,"Yes":1}[PhoneService]

MultipleLines = {
    "No":0,
    "Yes":1,
    "No phone service":2
}[MultipleLines]

InternetService = {
    "DSL":0,
    "Fiber optic":1,
    "No":2
}[InternetService]

OnlineSecurity = {
    "No":0,
    "Yes":1,
    "No internet service":2
}[OnlineSecurity]

OnlineBackup = {
    "No":0,
    "Yes":1,
    "No internet service":2
}[OnlineBackup]

DeviceProtection = {
    "No":0,
    "Yes":1,
    "No internet service":2
}[DeviceProtection]

TechSupport = {
    "No":0,
    "Yes":1,
    "No internet service":2
}[TechSupport]

StreamingTV = {
    "No":0,
    "Yes":1,
    "No internet service":2
}[StreamingTV]

StreamingMovies = {
    "No":0,
    "Yes":1,
    "No internet service":2
}[StreamingMovies]

Contract = {
    "Month-to-month":0,
    "One year":1,
    "Two year":2
}[Contract]

PaperlessBilling = {
    "No":0,
    "Yes":1
}[PaperlessBilling]

PaymentMethod = {
    "Electronic check":0,
    "Mailed check":1,
    "Bank transfer (automatic)":2,
    "Credit card (automatic)":3
}[PaymentMethod]

# -------------------------
# Prediction
# -------------------------

if st.button("Predict"):

    input_df = pd.DataFrame({

        "gender":[gender],
        "SeniorCitizen":[SeniorCitizen],
        "Partner":[Partner],
        "Dependents":[Dependents],
        "tenure":[tenure],
        "PhoneService":[PhoneService],
        "MultipleLines":[MultipleLines],
        "InternetService":[InternetService],
        "OnlineSecurity":[OnlineSecurity],
        "OnlineBackup":[OnlineBackup],
        "DeviceProtection":[DeviceProtection],
        "TechSupport":[TechSupport],
        "StreamingTV":[StreamingTV],
        "StreamingMovies":[StreamingMovies],
        "Contract":[Contract],
        "PaperlessBilling":[PaperlessBilling],
        "PaymentMethod":[PaymentMethod],
        "MonthlyCharges":[MonthlyCharges],
        "TotalCharges":[TotalCharges]

    })

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error(
            f"⚠️ Customer is likely to Churn\n\nProbability: {probability[1]:.2%}"
        )
    else:
        st.success(
            f"✅ Customer is likely to Stay\n\nProbability: {probability[0]:.2%}"
        )