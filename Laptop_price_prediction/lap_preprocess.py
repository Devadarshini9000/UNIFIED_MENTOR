import pandas as pd
import numpy as np
import os

# Load dataset
file_path = r"D:\UNM\laptop_prices.csv"  # Update this path if needed
df = pd.read_csv(file_path)

# Drop duplicate rows
df.drop_duplicates(inplace=True)

# Handle missing values
df.dropna(inplace=True)  # You can also use imputation methods

# Convert categorical variables to numerical using one-hot encoding
df = pd.get_dummies(df, drop_first=True)

# Define the cleaned dataset file path
output_dir = "D:/UNM"
cleaned_file_path = os.path.join(output_dir, "cleaned_laptop_prices.csv")

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save cleaned dataset
df.to_csv(cleaned_file_path, index=False)

print(f"Preprocessing complete. Cleaned dataset saved at: {cleaned_file_path}")
