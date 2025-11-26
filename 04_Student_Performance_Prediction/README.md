# 🎓 Student Performance Analysis and Grade Prediction

This project is a **Jupyter Notebook-based Machine Learning pipeline** that performs Exploratory Data Analysis (EDA) on student performance data and builds a **multi-class classification model** to predict a student's final grade (A, B, C, D, or Fail) based on demographic and academic features.

The entire workflow — from data analysis to model evaluation and saving — is implemented in the notebook:

```
Student_Performance.ipynb
```

---

## 🎯 Project Objective

The primary goals of this project are to:

* Explore and analyze the relationship between student demographics and academic performance.
* Identify patterns affecting student scores.
* Build a robust machine learning model that predicts a student's **final grade category** using their test scores and background information.

---

## 💾 Dataset Overview

The dataset contains student-level information including personal background, socio-economic context, and test scores.

### 📌 Features Description

| Column Name                 | Description                                |
| --------------------------- | ------------------------------------------ |
| roll_no                     | Unique identifier for each student         |
| gender                      | Student's gender (Male/Female)             |
| race_ethnicity              | Student's ethnic group (Group A–E)         |
| parental_level_of_education | Highest education level of parents         |
| lunch                       | Type of lunch (Standard / Free/Reduced)    |
| test_preparation_course     | Test prep course status (Completed / None) |
| math_score                  | Mathematics score                          |
| reading_score               | Reading score                              |
| writing_score               | Writing score                              |

---

## 🛠️ Workflow Overview

### 1️⃣ Exploratory Data Analysis (EDA)

* Distribution of subject scores
* Comparison of performance across:

  * Gender
  * Parental education level
  * Test preparation course
* Correlation analysis between math, reading, and writing scores
* Visualizations using Matplotlib & Seaborn

---

### 2️⃣ Feature Engineering

A new target variable **Grade** is created based on the average of three subject scores.

| Average Score | Grade |
| ------------- | ----- |
| > 90          | A     |
| > 80          | B     |
| > 70          | C     |
| > 60          | D     |
| ≤ 60          | Fail  |

This transforms the problem into a **multi-class classification task**.

---

### 3️⃣ Preprocessing & Model Building

A complete pipeline is built using `ColumnTransformer`:

#### ✅ Categorical Features

* One-Hot Encoding applied to:

  * gender
  * race_ethnicity
  * parental_level_of_education
  * lunch
  * test_preparation_course

#### ✅ Numerical Features

* StandardScaler applied to:

  * math_score
  * reading_score
  * writing_score

#### 🔍 Model Used

* **Random Forest Classifier** for grade prediction

Pipeline Structure:

```
Preprocessing ➜ Random Forest Classifier ➜ Grade Prediction
```

---

## 📊 Model Evaluation

The model is evaluated using:

* ✅ Accuracy Score
* ✅ Classification Report

  * Precision
  * Recall
  * F1-score
* ✅ Confusion Matrix Visualization

The confusion matrix clearly displays the performance of the model across all grade categories:
**A, B, C, D, Fail**

---

## 🚀 How to Run the Project

### 1️⃣ Install Required Libraries

Make sure Python is installed, then run:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib
```

### 2️⃣ Run the Notebook

Open the notebook in any Jupyter environment and run all cells sequentially:

* Jupyter Notebook
* JupyterLab
* VS Code
* Google Colab

File:

```
Student_Performance.ipynb
```

---

## 💾 Model Saving

The trained model pipeline is saved using `joblib` for reuse:

```python
joblib.dump(model, "student_grade_model.pkl")
```

This allows:

* Direct loading of the model
* Making predictions without retraining
* Easy integration into web or desktop applications

---

## ✅ Key Highlights

* End-to-End Machine Learning Pipeline
* Robust preprocessing using ColumnTransformer
* Multi-class grade classification
* Visualization-driven insights
* Production-ready saved model

---

## 📌 Future Improvements

* Hyperparameter tuning using GridSearchCV
* Trying other classifiers (XGBoost, SVM, Logistic Regression)
* Deployment as a web app using Streamlit or Flask
* Real-time prediction interface

---

## 👨‍🎓 Author

**Farhan Mughal**
Aspiring AI/ML Engineer | Data Science Enthusiast

---

If you found this project helpful, feel free to ⭐ the repository and share your feedback!
