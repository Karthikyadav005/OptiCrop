import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# 1. Load the dataset and split it cleanly
df = pd.read_csv('Crop_recommendation.csv')
X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Force it to read the fresh model file safely
print("Loading model file...")
try:
    with open('crop_model.pkl', 'rb') as f:
        model = pickle.load(f)
except Exception:
    # Backup: try loading it from one folder deep if paths crossed over
    with open('crop_model.pkl', 'rb') as f:
        model = pickle.load(f)

# 3. Predict the test rows using the loaded model
y_pred = model.predict(X_test)

# 4. Display the calculation results
accuracy = accuracy_score(y_test, y_pred)
print("\n--- Model Evaluation Metrics ---")
print(f"Overall Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))