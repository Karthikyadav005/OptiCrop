# 🌾 OptiCrop: Smart Agricultural Production Optimization Engine 🚀

OptiCrop is an AI-powered crop recommendation web application that helps farmers choose the most suitable crop based on soil nutrients and environmental conditions. Using Machine Learning, the application analyzes soil chemistry and weather parameters to recommend the crop with the highest probability of successful growth and better yield.

---

## 🌐 Live Demo

🔗 **Try the application here:**  
https://opticrop-2-bx5c.onrender.com

---

## 📋 Problem Statement

Traditional farming often relies on experience or historical practices to select crops. However, choosing crops without considering soil nutrients and climatic conditions can reduce productivity and lead to poor resource utilization.

**OptiCrop** addresses this challenge by using Machine Learning to analyze agricultural parameters such as Nitrogen (N), Phosphorus (P), Potassium (K), temperature, humidity, pH, and rainfall. Based on these inputs, the system predicts the most suitable crop for cultivation.

---

## 🔍 Exploratory Data Analysis (EDA)

During data exploration, the following analyses were performed:

- Verified **100% data completeness** with no missing values.
- Analyzed **7 numerical input features** and **1 categorical target feature**.
- Examined crop distribution across multiple classes.
- Visualized relationships between soil nutrients and crop labels.
- Studied feature correlations to understand environmental dependencies.

### Input Features

| Feature | Description |
|----------|-------------|
| Nitrogen (N) | Soil Nitrogen content |
| Phosphorus (P) | Soil Phosphorus content |
| Potassium (K) | Soil Potassium content |
| Temperature | Temperature (°C) |
| Humidity | Relative Humidity (%) |
| pH | Soil pH value |
| Rainfall | Rainfall (mm) |

### Output

- Recommended Crop

---

## 🛠️ Features

- ✅ AI-powered crop recommendation
- ✅ Soil nutrient analysis
- ✅ Weather parameter evaluation
- ✅ Machine Learning prediction using Logistic Regression
- ✅ Interactive Flask web application
- ✅ Responsive HTML5 & CSS interface
- ✅ Data visualization using Matplotlib & Seaborn
- ✅ Real-time prediction results
- ✅ Easy-to-use user interface

---

## 🧠 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Selection
5. Data Scaling
6. Train-Test Split (80:20)
7. Model Training
8. Model Evaluation
9. Deployment using Flask
10. Prediction through Web Interface

---

## 📊 Model Performance

- **Algorithm Used:** Logistic Regression
- **Training/Test Split:** 80% / 20%
- **Prediction Type:** Multi-Class Classification
- **Model Accuracy:** **100%** on the evaluation dataset

---

## 💻 Tech Stack

### Backend
- Python
- Flask

### Machine Learning
- Scikit-Learn
- Pandas
- NumPy

### Data Visualization
- Matplotlib
- Seaborn

### Frontend
- HTML5
- CSS3
- Flexbox
- CSS Grid

---

## 📁 Project Structure

```
OptiCrop/
│
├── app.py
├── model.pkl
├── scaler.pkl
├── crop_recommendation.csv
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── style.css
│   ├── images/
│   └── charts/
│
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/OptiCrop.git
```

### 2. Navigate to Project Directory

```bash
cd OptiCrop
```

### 3. Install Required Libraries

```bash
pip install flask pandas numpy scikit-learn matplotlib seaborn
```

Or install using requirements.txt

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

The Flask server will start locally.

Open your browser and visit

```
http://127.0.0.1:5000/
```

---

## 🌍 Deployed Application

You can also access the deployed application here:

👉 **https://opticrop-2-bx5c.onrender.com**

---

## 📈 Input Parameters

The application accepts the following values:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Soil pH
- Rainfall

---

## 🎯 Prediction Output

The application predicts the most suitable crop for cultivation based on the provided environmental conditions.

Example:

```
Input:

N = 90
P = 42
K = 43
Temperature = 20.8°C
Humidity = 82%
pH = 6.5
Rainfall = 202 mm

Output:

Recommended Crop:
Rice
```

---

## 📊 Visualizations

The application also generates graphical comparisons of:

- User NPK values
- Ideal NPK values for the predicted crop

using **Matplotlib** and **Seaborn**.

---

## 🔮 Future Enhancements

- 🌦️ Live Weather API Integration
- 🌱 Fertilizer Recommendation System
- 📷 Plant Disease Detection
- 🛰️ Satellite-based Soil Analysis
- 📱 Mobile Application
- 🌍 Multi-language Support
- 🤖 Deep Learning-based Crop Prediction

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create your feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push to your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📜 License

This project is developed for educational and learning purposes.

---

## 👨‍💻 Author

**Venkata Karthik**

GitHub: https://github.com/yourusername

---

⭐ If you found this project helpful, don't forget to **Star ⭐ the repository!**
