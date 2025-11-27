# ✈️ Flight Price Prediction

## 📌 Project Overview

This project focuses on predicting flight ticket prices using machine learning techniques based on various travel-related features such as airline, source, destination, duration, total stops, and journey date. The goal is to analyze the factors affecting flight prices and build an accurate regression model that can estimate ticket fares for future journeys.

The entire workflow is implemented in a Jupyter Notebook: **Flight_Price_Prediction.ipynb**.

---

## 🎯 Objectives

* Perform Exploratory Data Analysis (EDA) on flight data
* Understand the relationship between different features and ticket price
* Preprocess and transform raw data into model-ready format
* Train and evaluate multiple regression models
* Select the best-performing model for price prediction

---

## 🧠 Machine Learning Problem Type

* **Category:** Supervised Learning
* **Task:** Regression
* **Target Variable:** Price

---

## 📂 Project Structure

```
Flight Price Prediction/
│
├── Flight_Price_Prediction.ipynb   # Main notebook
├── README.md                       # Project documentation
├── data/                           # Dataset (if included)
└── models/                         # Saved models (optional)
```

---

## 🛠️ Tools & Technologies Used

* Python
* Jupyter Notebook
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn

---

## 🔍 Key Steps Performed

### 1. Data Loading

* Imported the flight dataset
* Checked shape, data types, and basic statistics

### 2. Data Cleaning

* Handled missing values
* Removed unnecessary columns
* Converted date and time features into numerical format

### 3. Feature Engineering

* Extracted:

  * Journey Day
  * Journey Month
  * Departure Hour & Minute
  * Arrival Hour & Minute
  * Duration in minutes

### 4. Exploratory Data Analysis (EDA)

* Visualized price trends
* Analyzed impact of airlines, stops, and routes
* Identified correlations using heatmaps

### 5. Encoding

* Label Encoding & One-Hot Encoding for categorical variables

### 6. Model Building

Trained multiple regression models including:

* Linear Regression
* Random Forest Regressor
* Decision Tree Regressor (if applicable)

### 7. Model Evaluation

Used evaluation metrics such as:

* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)

Best model selected based on performance comparison.

---

## ✅ Results

* Successfully built a model capable of predicting flight prices with good accuracy
* Identified key factors influencing price such as airline, duration, and number of stops
---

## 📈 Future Improvements

* Hyperparameter tuning using GridSearchCV
* Use advanced models like XGBoost or LightGBM
* Deploy model as a web app using Streamlit or Flask
* Add real-time ticket price prediction feature

---

## 🙌 Author

**Farhan Mughal**
Aspiring AI/ML Engineer

---

## 📎 License

This project is open-source and available for learning and educational purposes.

---

If you found this project helpful, don't forget to ⭐ the repository and share your feedback!
