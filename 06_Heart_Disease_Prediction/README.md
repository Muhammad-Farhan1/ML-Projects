# ❤️ Heart Disease Prediction

## 📌 Project Overview

This project focuses on predicting the likelihood of heart disease in patients using machine learning techniques. The notebook performs complete data preprocessing, exploratory data analysis (EDA), feature engineering, and model training to build an accurate classification system.

The goal is to help identify individuals at risk of heart disease based on their health and lifestyle attributes.

---

## 🎯 Objective

To build a reliable machine learning model that predicts whether a person has heart disease using medical and lifestyle indicators.

---

## 📂 Dataset Description

The dataset includes various health-related features such as:

- HeartDisease (Target Variable)
- BMI
- Smoking
- AlcoholDrinking
- Stroke
- PhysicalHealth
- MentalHealth
- DiffWalking
- Sex
- AgeCategory
- Race
- Diabetic
- PhysicalActivity
- GenHealth
- SleepTime
- Asthma
- KidneyDisease
- SkinCancer

Target Variable:
- HeartDisease  
  - 1 → Has Heart Disease  
  - 0 → No Heart Disease

---

## 🧠 Workflow

### 1️⃣ Data Loading
- Imported dataset using Pandas
- Displayed dataset structure and basic statistics

### 2️⃣ Data Preprocessing
- Binary conversion (Yes/No → 1/0)
- Encoding categorical features
- Missing value handling
- Feature scaling

### 3️⃣ Exploratory Data Analysis (EDA)
- Distribution analysis
- Feature correlation insights
- Visualizations using Matplotlib

### 4️⃣ Model Building
Models explored:
- Logistic Regression  
- Random Forest  
- Other classification algorithms

### 5️⃣ Model Evaluation
Evaluation metrics:
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- ROC-AUC Score

---

## 📊 Results

The model successfully predicts the presence of heart disease with strong accuracy and reliable performance across evaluation metrics.

---

## 🛠️ Technologies Used

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Scikit-learn  
- Jupyter Notebook  

---

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/your-username/heart-disease-prediction.git
