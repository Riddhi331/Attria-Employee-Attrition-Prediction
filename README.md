# 🚀 Attria — Employee Attrition Prediction System

> **An end-to-end Machine Learning application that predicts employee attrition risk using workplace, demographic, and job-related factors.**

[![Live Demo](https://img.shields.io/badge/🚀%20Live%20Demo-Streamlit-red?style=for-the-badge)](https://attria-employee-attrition-prediction-das8cv66kjs7lk9ttvuyp9.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-ML-blue?style=for-the-badge\&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge\&logo=streamlit)](https://streamlit.io/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge\&logo=scikit-learn)](https://scikit-learn.org/)

---

## 🌐 Live Demo

### 👉 [Launch Attria — Employee Attrition Prediction System](https://attria-employee-attrition-prediction-das8cv66kjs7lk9ttvuyp9.streamlit.app/)

Try the deployed application by entering employee information and generating an attrition prediction.

---

## 📌 Project Overview

**Attria** is a Machine Learning-based Employee Attrition Prediction System designed to help organizations identify employees who may be at risk of leaving.

The application analyzes employee demographic, workplace, compensation, and job-related factors and uses trained classification models to predict whether an employee is likely to **stay or leave** the organization.

The system provides an interactive interface where users can enter employee details and receive:

* Employee attrition prediction
* Probability of leaving
* Probability of staying
* Risk information
* Model performance comparison
* Best-performing model information

---

## 🎯 Problem Statement

Employee attrition can have a significant impact on organizations.

High employee turnover may result in:

* Increased recruitment costs
* Loss of experienced employees
* Reduced productivity
* Increased workload on existing employees
* Training and onboarding expenses
* Disruption to teams and projects

Attria aims to provide a predictive analytics solution that can help identify potential attrition risks and support data-driven HR decision-making.

---

## ✨ Key Features

### 👤 Employee Details

Users can provide information including:

* Age
* Department
* Job Role
* Monthly Income
* Years at Company
* Total Working Years
* Overtime
* Distance From Home
* Job Satisfaction
* Environment Satisfaction
* Work-Life Balance
* Number of Companies Worked
* Marital Status
* Business Travel
* Education Field
* Gender

### 🤖 Multiple Machine Learning Models

The project implements and compares three classification algorithms:

* **Logistic Regression**
* **Decision Tree**
* **Random Forest**

### 🏆 Best Model Selection

The trained models are evaluated using multiple performance metrics:

* Accuracy
* F1 Score
* ROC AUC

The best-performing model is selected for the final prediction.

### 📊 Prediction & Risk Analysis

The application provides:

* Attrition prediction
* Employee leave probability
* Employee stay probability
* Risk percentage
* Best model information

### 📈 Interactive Dashboard

The application uses **Streamlit** for the user interface and **Plotly** for interactive visualizations.

---

## 🧠 Machine Learning Workflow

```text
                    Employee Dataset
                           │
                           ▼
                  Data Preprocessing
                           │
                           ▼
                Categorical Encoding
                           │
                           ▼
                   Feature Scaling
                           │
                           ▼
                   Model Training
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
       Logistic         Decision      Random
       Regression         Tree         Forest
             │             │             │
             └─────────────┼─────────────┘
                           ▼
                  Model Evaluation
                           │
                           ▼
                  Model Comparison
                           │
                           ▼
                  Best Model Selection
                           │
                           ▼
                 Streamlit Application
                           │
                           ▼
              Employee Attrition Prediction
```

---

## 🤖 Machine Learning Models

### 1. Logistic Regression

Logistic Regression is used as a baseline classification model for predicting the probability of employee attrition.

It is particularly useful for binary classification problems such as:

```text
Stay → No
Leave → Yes
```

### 2. Decision Tree

Decision Tree uses a series of feature-based decisions to classify employees into attrition categories.

It provides an interpretable tree-based approach to classification.

### 3. Random Forest

Random Forest is an ensemble learning algorithm that combines multiple decision trees to improve prediction robustness and generalization.

---

## 📊 Model Evaluation

The models are evaluated using three important classification metrics:

| Metric       | Description                                                 |
| ------------ | ----------------------------------------------------------- |
| **Accuracy** | Measures the percentage of correctly classified predictions |
| **F1 Score** | Balances precision and recall                               |
| **ROC AUC**  | Measures the model's ability to distinguish between classes |

The application displays the performance of the trained models directly in the Streamlit dashboard.

---

## 🗂️ Dataset

The project uses the **IBM HR Analytics Employee Attrition & Performance** dataset.

The dataset contains employee information such as:

* Demographics
* Job information
* Compensation
* Work experience
* Job satisfaction
* Work environment
* Business travel
* Overtime
* Employee attrition

The target variable is:

```text
Attrition
```

with two possible outcomes:

```text
Yes → Employee is likely to leave
No  → Employee is likely to stay
```

---

## 🛠️ Technology Stack

### Programming

* Python

### Machine Learning

* Scikit-Learn
* NumPy
* Pandas
* Joblib

### Visualization

* Plotly

### Application

* Streamlit

### Development

* Jupyter Notebook
* Git
* GitHub

### Deployment

* Streamlit Community Cloud

---

## 📁 Project Structure

```text
Attria-Employee-Attrition-Prediction/
│
├── app/
│   ├── app.py
│   └── style.css
│
├── model/
│   ├── best_model.pkl
│   ├── logistic_model.pkl
│   ├── dt_model.pkl
│   ├── rf_model.pkl
│   ├── feature_scaler.pkl
│   ├── label_encoders.pkl
│   ├── target_encoder.pkl
│   └── model_info.pkl
│
├── Documentation/
│   └── Attria_Project_Documentation.pdf
│
├── notebook/
│   ├── Employee_Attrition.ipynb
│   └── WA_Fn-UseC_-HR-Employee-Attrition (1).csv
│
├── output ss/
│   ├── best_model.png
│   ├── dashboard.png
│   ├── Employee_details.png
│   ├── model_comaprison.png
│   ├── Prediction_result.png
│   └── risk_analysis.png
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 📸 Application Screenshots

### 🏠 Dashboard

![Attria Dashboard](output%20ss/dashboard.png)

### 👤 Employee Details

![Employee Details](output%20ss/Employee_details.png)

### 📊 Prediction Result

![Prediction Result](output%20ss/Prediction_result.png)

### ⚠️ Risk Analysis

![Risk Analysis](output%20ss/risk_analysis.png)

### 🏆 Best Model

![Best Model](output%20ss/best_model.png)

### 📈 Model Comparison

![Model Comparison](output%20ss/model_comaprison.png)

---

## 📄 Project Documentation

Detailed project documentation is included in the repository.

### 📘 [View Attria Project Documentation](Documentation/Attria_Project_Documentation.pdf)

The documentation covers:

* Project introduction
* Problem statement
* Dataset
* Data preprocessing
* Exploratory analysis
* Machine learning methodology
* Model training
* Model evaluation
* Application development
* Results
* Future scope

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Riddhi331/Attria-Employee-Attrition-Prediction.git
```

### 2. Navigate to the project directory

```bash
cd Attria-Employee-Attrition-Prediction
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run app/app.py
```

The application will open in your browser.

---

## 🚀 Deployment

The application is deployed using **Streamlit Community Cloud**.

### 🌐 Live Application

**[Open Attria Live Demo →](https://attria-employee-attrition-prediction-das8cv66kjs7lk9ttvuyp9.streamlit.app/)**

---

## 🔮 Future Improvements

Future versions of Attria could include:

* 📊 Advanced HR analytics dashboards
* 🔍 Explainable AI using SHAP
* 📈 Feature importance visualization
* 👥 Role-specific attrition analysis
* 💡 Personalized employee retention recommendations
* 📧 Automated HR alerts
* 🗄️ Database integration
* 🔐 Authentication and role-based access
* 📱 Improved mobile responsiveness
* 📉 Advanced employee risk trend analysis

---

## ⚠️ Disclaimer

Attria is developed for **educational and demonstration purposes**.

Machine learning predictions should not be used as the sole basis for employment-related decisions. Real-world HR applications should include appropriate validation, fairness evaluation, privacy protection, and human oversight.

---

## 👩‍💻 Author

### Riddhi Parmar

**Computer Science & Engineering — AI/ML**

### 🔗 Project Links

🚀 **Live Demo:**
[Attria — Employee Attrition Prediction System](https://attria-employee-attrition-prediction-das8cv66kjs7lk9ttvuyp9.streamlit.app/)

💻 **GitHub Repository:**
[Attria — Employee Attrition Prediction System](https://github.com/Riddhi331/Attria-Employee-Attrition-Prediction)

📘 **Project Documentation:**
[Attria Project Documentation](Documentation/Attria_Project_Documentation.pdf)

---

⭐ **If you found this project useful or interesting, consider giving the repository a star!**
