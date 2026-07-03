from flask import Flask, render_template, request
import pandas as pd
import pickle
# Import your chart generation function
from generate_charts import create_metrics_chart

app = Flask(__name__)

# Load the newly enhanced machine learning model
with open('crop_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # 1. Retrieve input metrics from our styled HTML form
            n_val = float(request.form['N'])
            p_val = float(request.form['P'])
            k_val = float(request.form['K'])
            
            inputs = [
                n_val,
                p_val,
                k_val,
                float(request.form['temperature']),
                float(request.form['humidity']),
                float(request.form['ph']),
                float(request.form['rainfall'])
            ]
            
            # 2. Trigger the dynamic chart rendering for Epic 8
            create_metrics_chart(n_val, p_val, k_val)
            
            # 3. Run prediction through Logistic Regression model
            feature_names = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
            df_input = pd.DataFrame([inputs], columns=feature_names)
            
            prediction = model.predict(df_input)
            recommended_crop = prediction[0].capitalize()
            
            return render_template('result.html', crop=recommended_crop)
        except Exception as e:
            return f"An error occurred during prediction: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)