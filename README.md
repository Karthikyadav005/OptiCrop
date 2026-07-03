# OptiCrop: Smart Agricultural Production Optimization Engine 🌾🚀

OptiCrop is an AI-driven web application designed to maximize farming yields by providing real-time, data-driven crop recommendations. The system evaluates soil chemistry and regional weather inputs using a Machine Learning pipeline to match farmlands with optimal crop choices.

---

## 📋 Problem Statement & Project Understanding (Epic 1)
Traditional farming often relies on guesswork or historical habits to select crops, which can lead to poor yields, soil degradation, and wasted resources if the soil chemistry doesn't match the crop's biological needs. 

The **OptiCrop Engine** solves this problem by using predictive analytics. It ingests precision agriculture metrics—specifically soil macronutrients (Nitrogen, Phosphorus, Potassium), pH levels, and localized climate data (temperature, humidity, rainfall)—to scientifically recommend the absolute highest-yielding crop for that specific environment.

---

## 🔍 Exploratory Data Analysis (Epic 2)
During the initial data discovery phase, we analyzed the agricultural dataset structure to ensure high data integrity:
- **Data Completeness:** Verified 100% data integrity with zero null/missing values across all environmental columns.
- **Feature Schema:** Evaluated 7 independent numeric features (`N`, `P`, `K`, `temperature`, `humidity`, `ph`, `rainfall`) against 1 categorical target label (`label`).
- **Target Distribution:** Analyzed multi-class crop labels (including Rice, Maize, Coffee, Grapes, and Mango) to map out distinct soil nutrient boundaries for each profile.

---

## 🛠️ Features Completed

- **Epic 3 (Data Pre-processing):** Cleaned agricultural records, applied data scaling methods, and established robust training (80%) and testing (20%) datasets.
- **Epic 4 & 6 (Model Building & Evaluation):** Replaced temporary mock logic with a production-ready Logistic Regression classifier, achieving 100% accuracy on multi-class evaluation splits.
- **Epic 5 & 7 (Application & Deployment):** Formed an interactive web portal using Flask, HTML5, and customized agricultural CSS to deliver instant predictions.
- **Epic 8 (Advanced Analytics):** Integrated dynamic data charting using Matplotlib and Seaborn to provide visual feedback, comparing user soil NPK levels against a crop's ideal baseline.

---

## 💻 Tech Stack Used
- **Backend Framework:** Flask (Python)
- **Machine Learning & Analysis:** Scikit-Learn, Pandas, NumPy
- **Data Visualizations:** Matplotlib, Seaborn
- **Frontend Design:** Semantic HTML5, CSS Grid & Flexbox

---

## 🚀 How to Run the Project
1. Clone the repository and navigate into the project root directory.
2. Ensure dependencies are installed:
   ```bash
   pip install flask pandas scikit-learn matplotlib seaborn