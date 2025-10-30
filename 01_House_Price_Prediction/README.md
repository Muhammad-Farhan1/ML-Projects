# 🏡 House Price Prediction

This project aims to **predict house prices** based on various features such as the number of rooms, area, location, and other factors. The goal was to understand how different attributes influence house prices and to build a machine learning model that can make accurate predictions.

---

## 📘 Project Overview

The **House Price Prediction** project is a supervised machine learning regression problem where we predict the target variable — **Price** — using multiple independent features.

The project demonstrates a complete **end-to-end machine learning workflow** including:
- Data understanding and cleaning
- Exploratory Data Analysis (EDA)
- Feature engineering
- Model training and evaluation
- Saving and deploying the model using Streamlit

---

## 🧩 Steps We Followed

### 1. **Data Loading**
- Imported the dataset using **Pandas**.
- Displayed the first few rows to understand its structure.

### 2. **Data Cleaning**
- Checked for **missing values** and handled them appropriately.
- Detected and treated **outliers** using boxplots and statistical methods.
- Converted categorical variables to numeric using **encoding techniques**.

### 3. **Exploratory Data Analysis (EDA)**
- Visualized relationships between features and target using:
  - **Scatter plots** (Area vs Price)
  - **Correlation heatmap**
  - **Box plots** (to identify price trends by category)
- Identified the most influential features affecting house prices.

### 4. **Feature Engineering**
- Selected the most important columns for modeling.
- Split the dataset into **features (X)** and **target (y)**.
- Performed **train-test split** to evaluate model performance properly.

### 5. **Model Building**
- Used **Linear Regression** to train the model.
- Evaluated the model using performance metrics:
  - **R² Score**
  - **Mean Absolute Error (MAE)**
  - **Mean Squared Error (MSE)**

### 6. **Model Deployment**
- Saved the trained model using `joblib`.
- Built an interactive **Streamlit web app** where users can:
  - Input house details
  - Get predicted house price instantly

---

## 🧠 Technologies Used
- **Python**
- **Pandas** – Data manipulation
- **NumPy** – Numerical operations
- **Matplotlib & Seaborn** – Data visualization
- **Scikit-learn** – Machine learning model
- **Joblib** – Model saving
- **Streamlit** – Model deployment

---
