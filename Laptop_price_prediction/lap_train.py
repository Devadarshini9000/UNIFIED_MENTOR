import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib

# Load the cleaned dataset
cleaned_file_path = r"D:\UNM\cleaned_laptop_prices.csv"  # Ensure the correct path
df = pd.read_csv(cleaned_file_path)

# Use correct target column name
X = df.drop(columns=['Price_euros'])  # Drop target column
y = df['Price_euros']  # Target variable

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))

# Save trained model
model_path = "D:/UNM/laptop_price_model.pkl"  # Updated path
joblib.dump(model, model_path)
print(f"Model saved at: {model_path}")
