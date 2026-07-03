import pandas as pd

# Load the agricultural dataset
data = pd.read_csv('Crop_recommendation.csv')

print("--- Dataset Information ---")
print(data.info())

print("\n--- Missing Values Check ---")
print(data.isnull().sum())

print("\n--- Available Crops in Dataset ---")
print(data['label'].unique())