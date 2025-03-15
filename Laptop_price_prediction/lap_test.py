import streamlit as st
import pandas as pd
import joblib

# Load trained model
model_path = "laptop_price_model.pkl"  # Ensure the correct path
model = joblib.load(model_path)

# Load cleaned dataset for reference
cleaned_file_path = "cleaned_laptop_prices.csv"
df = pd.read_csv(cleaned_file_path)

# Get all feature names used during training (excluding target column)
feature_columns = [col for col in df.columns if col != 'Price_euros']

st.title("Laptop Price Prediction App")

st.write("Enter the laptop features below to predict its price in Euros:")

# Select only required features
selected_features = ["Inches", "Ram", "PrimaryStorage", "Processor"]
input_data = {}

# Dropdown for Processor selection
processor_options = ["Intel", "AMD Ryzen", "Apple M1", "Apple M2", "Other"]
input_data["Processor"] = st.selectbox("Select Processor", processor_options)

# Numeric inputs for other features
for feature in ["Inches", "Ram", "PrimaryStorage"]:
    input_data[feature] = st.number_input(f"Enter {feature}", value=float(df[feature].median()))

# Convert categorical 'Processor' to numerical encoding
input_df = pd.DataFrame([input_data])

# Encode 'Processor' as numerical values
processor_mapping = {processor: idx for idx, processor in enumerate(processor_options)}
input_df["Processor"] = input_df["Processor"].map(processor_mapping)

# Ensure all features match those from training
for col in feature_columns:
    if col not in input_df.columns:
        input_df[col] = 0  # Add missing features with default value 0

# Reorder columns to match model training
input_df = input_df[feature_columns]

# Predict price
if st.button("Predict Price"):
    predicted_price = model.predict(input_df)[0]
    st.success(f"Predicted Laptop Price: **€{predicted_price:.2f}**")
