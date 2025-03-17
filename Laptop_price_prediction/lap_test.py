import streamlit as st
import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("cleaned_laptop_prices.csv")

# Conversion rate (Example: 1 Euro = 90 INR, adjust as needed)
EURO_TO_INR = 90

# Ensure numeric columns exist and drop any missing values
df = df.dropna()
if 'Price_euros' not in df.columns:
    st.error("Error: 'Price_euros' column not found in dataset.")
else:
    df['Price_INR'] = df['Price_euros'] * EURO_TO_INR

def predict_price(features):
    """Mock function for price prediction."""
    return np.random.randint(500, 3000)  # Replace with ML model later

# Streamlit UI
st.title("Laptop Price Prediction App")
st.write("Enter laptop specifications below to predict its price in INR.")

# Input fields
ram = st.selectbox("Select RAM (GB)", df['Ram'].unique())
storage = st.selectbox("Select Primary Storage", df['PrimaryStorage'].unique())
screen_size = st.selectbox("Select Screen Size (Inches)", df['Inches'].unique())
weight = st.selectbox("Select Weight (Kg)", df['Weight'].unique())

touch_screen = st.selectbox("Touch Screen", ['Yes', 'No'])
ssd = st.selectbox("SSD Available", ['Yes', 'No'])
ips_display = st.selectbox("IPS Display", ['Yes', 'No'])

# Predict button
if st.button("Predict Price"):
    price_euros = predict_price([ram, storage, screen_size, weight, touch_screen, ssd, ips_display])
    price_inr = price_euros * EURO_TO_INR
    st.success(f"Predicted Price: {price_inr} INR")
