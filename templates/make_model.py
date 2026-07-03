import pickle
import numpy as np

# A fake model class that simulates a trained Machine Learning model
class DummyModel:
    def predict(self, features):
        crops = ['Rice', 'Maize', 'Chickpea', 'Kidneybeans', 'Pigeonpeas', 'Mothbeans', 'Mungbean']
        # Randomly picks a crop based on the inputs so the app works
        idx = int(np.sum(features)) % len(crops)
        return [crops[idx]]

# Create the model object
model = DummyModel()

# 5. Save the real model (putting it directly into the main folder)
with open('crop_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Success! crop_model.pkl has been created.")