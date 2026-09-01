<<<<<<< HEAD
# 🚀 ATTRIA — Employee Attrition Prediction System

> An AI-powered Employee Attrition Prediction and HR Analytics System that predicts whether an employee is likely to stay with or leave an organization.

---

## 📌 Overview

ATTRIA is a Machine Learning-based Employee Attrition Prediction System designed to help organizations identify employees who may be at risk of leaving.

The system analyzes employee demographic, professional, and workplace-related factors and predicts the likelihood of employee attrition.

It provides an interactive Streamlit dashboard where users can enter employee details, generate predictions, view attrition probabilities, and analyze the risk level.

---

## 🎯 Problem Statement

Employee attrition can significantly affect organizations through increased recruitment costs, productivity loss, knowledge loss, and workforce instability.

ATTRIA aims to provide an intelligent and data-driven approach to identifying employees who may be likely to leave the organization.

---

## 💡 Solution

ATTRIA uses Machine Learning classification algorithms to analyze employee-related factors and predict employee attrition.

The system compares multiple Machine Learning models and uses the trained models to generate predictions through an interactive web-based dashboard.

---

## ✨ Key Features

- 👤 Employee demographic and professional information input
- 📊 Employee attrition prediction
- 🤖 Multiple Machine Learning models
- 📈 Attrition probability calculation
- 🟢 Low-risk, 🟡 medium-risk, and 🔴 high-risk classification
- 📉 Interactive attrition risk visualization
- 📊 Model performance comparison
- 🎨 Dark-themed interactive Streamlit dashboard
- 📄 Project documentation
- 💾 Pre-trained Machine Learning models
- 🔍 HR analytics-oriented prediction system

---

## 🤖 Machine Learning Models

ATTRIA evaluates the following classification algorithms:

### 1. Logistic Regression

Used as a baseline classification model for predicting employee attrition.

### 2. Decision Tree

A tree-based classification model used to identify decision patterns associated with employee attrition.

### 3. Random Forest

An ensemble learning model consisting of multiple decision trees to improve prediction robustness.

---

## 📊 Model Performance

The models were evaluated using:

- Accuracy
- F1 Score
- ROC-AUC Score

| Model | Accuracy | F1 Score | ROC-AUC |
|---|---:|---:|---:|
| Logistic Regression | 86.39% | 39.39% | 79.03% |
| Decision Tree | 71.77% | 45.05% | 72.00% |
| Random Forest | 82.65% | 19.05% | 79.02% |

Logistic Regression achieved the highest accuracy among the evaluated models.

---

## 🖥️ Application Screenshots

### Employee Attrition Dashboard

![Dashboard](output%20ss/dashboard.png)

### Employee Details

![Employee Details](output%20ss/employee-details.png)

### Prediction Result

![Prediction Result](output%20ss/prediction-result.png)

### Risk Analysis

![Risk Analysis](output%20ss/risk-analysis.png)

### Model Comparison

![Model Comparison](output%20ss/model-comparison.png)

---

## 🛠️ Tech Stack

### Programming Language

- Python

### Machine Learning

- Scikit-learn
- Logistic Regression
- Decision Tree
- Random Forest

### Data Processing

- Pandas
- NumPy

### Model Serialization

- Joblib

### Visualization

- Plotly

### Web Application

- Streamlit

### Development Tools

- Jupyter Notebook
- Visual Studio Code
- Git
- GitHub

---

## 📁 Project Structure

```text
ATTRIA/
│
├── app/
│   ├── app.py
│   └── style.css
│
├── Documentation/
│   └── Attria_Project_Documentation.pdf
│
├── model/
│   ├── best_model.pkl
│   ├── dt_model.pkl
│   ├── feature_scaler.pkl
│   ├── label_encoders.pkl
│   ├── logistic_model.pkl
│   ├── model_info.pkl
│   ├── rf_model.pkl
│   ├── scaler.pkl
│   └── target_encoder.pkl
│
├── notebook/
│   ├── Employee_Attrition.ipynb
│   └── dataset.csv
│
├── output ss/
│   ├── dashboard.png
│   ├── employee-details.png
│   ├── prediction-result.png
│   ├── risk-analysis.png
│   └── model-comparison.png
│
├── .gitignore
├── README.md
└── requirements.txt
=======
# Attria-Employee-Attrition-Prediction
>>>>>>> 076d41fc10d4cad59a83216c3f733674d7624881
