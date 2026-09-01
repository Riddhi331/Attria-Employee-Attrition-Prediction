import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
from pathlib import Path

# ----------------------------
# PAGE CONFIG
# ----------------------------

st.set_page_config(
    page_title="Attria | Employee Attrition Intelligence",
    page_icon="👨‍💼",
    layout="wide"
)

# ----------------------------
# PATHS
# ----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "model"
CSS_FILE = BASE_DIR / "app" / "style.css"

# ----------------------------
# LOAD CSS
# ----------------------------

if CSS_FILE.exists():
    with open(CSS_FILE) as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True
        )

# ----------------------------
# LOAD MODELS
# ----------------------------

try:

    best_model = joblib.load(MODEL_DIR / "best_model.pkl")

    logistic_model = joblib.load(MODEL_DIR / "logistic_model.pkl")

    dt_model = joblib.load(MODEL_DIR / "dt_model.pkl")

    rf_model = joblib.load(MODEL_DIR / "rf_model.pkl")

    scaler = joblib.load(MODEL_DIR / "feature_scaler.pkl")

    label_encoders = joblib.load(MODEL_DIR / "label_encoders.pkl")

    target_encoder = joblib.load(MODEL_DIR / "target_encoder.pkl")

    model_info = joblib.load(MODEL_DIR / "model_info.pkl")

except Exception as e:

    st.error(f"Error loading model files:\n\n{e}")
    st.stop()

# ----------------------------
# MODEL INFORMATION
# ----------------------------

feature_columns = [
    col for col in model_info["feature_columns"]
    if col != "Attrition"
]

categorical_columns = model_info["categorical_columns"]

needs_scaling = model_info["needs_scaling"]

best_model_name = model_info["model_name"]

metrics = model_info["metrics"]

# ----------------------------
# HEADER
# ----------------------------

st.title("👨‍💼 Attria")

st.caption(
    "Predict whether an employee is likely to stay with the company or leave based on workplace and demographic factors."
)

st.markdown("---")

# ----------------------------
# SIDEBAR
# ----------------------------

st.sidebar.title("📊 HR Analytics Dashboard")

st.sidebar.success(
    f"🏆 Best Model\n\n{best_model_name}"
)

st.sidebar.markdown("---")

st.sidebar.subheader("📈 Model Performance")

for model_name, values in metrics.items():

    st.sidebar.markdown(f"### {model_name}")

    st.sidebar.metric(
        "Accuracy",
        f"{values['Accuracy']:.4f}"
    )

    st.sidebar.metric(
        "F1 Score",
        f"{values['F1 Score']:.4f}"
    )

    st.sidebar.metric(
        "ROC AUC",
        f"{values['ROC AUC']:.4f}"
    )

    st.sidebar.markdown("---")

st.sidebar.subheader("ℹ Instructions")

st.sidebar.info(
"""
1. Enter employee information.

2. Click **Predict Employee Attrition**.

3. The app evaluates all three trained models.

4. The best-performing model generates the final prediction.
"""
)

st.sidebar.markdown("---")

st.sidebar.success(
"Developed using Streamlit + Scikit-Learn"
)

# ----------------------------
# INPUT SECTION
# ----------------------------

st.markdown("## 👤 Employee Details")

st.write(
    "Fill in the employee details below."
)

col1, col2 = st.columns(2)

# ----------------------------
# INPUT FIELDS
# ----------------------------

with col1:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=60,
        value=30
    )

    department = st.selectbox(
        "Department",
        [
            "Research & Development",
            "Sales",
            "Human Resources"
        ]
    )

    monthly_income = st.number_input(
        "Monthly Income",
        min_value=1000,
        value=5000,
        step=500
    )

    years_at_company = st.number_input(
        "Years At Company",
        min_value=0,
        value=5
    )

    total_working_years = st.number_input(
        "Total Working Years",
        min_value=0,
        value=10
    )

    overtime = st.selectbox(
        "OverTime",
        ["Yes", "No"]
    )

    distance_from_home = st.number_input(
        "Distance From Home",
        min_value=1,
        max_value=50,
        value=5
    )

    gender = st.radio(
        "Gender",
        ["Male", "Female"],
        horizontal=True
    )

with col2:

    job_role = st.selectbox(
        "Job Role",
        [
            "Healthcare Representative",
            "Human Resources",
            "Laboratory Technician",
            "Manager",
            "Manufacturing Director",
            "Research Director",
            "Research Scientist",
            "Sales Executive",
            "Sales Representative"
        ]
    )

    job_satisfaction = st.slider(
        "Job Satisfaction",
        1,
        4,
        3
    )

    environment_satisfaction = st.slider(
        "Environment Satisfaction",
        1,
        4,
        3
    )

    companies_worked = st.number_input(
        "Number of Companies Worked",
        min_value=0,
        value=2
    )

    worklife_balance = st.slider(
        "Work-Life Balance",
        1,
        4,
        3
    )

    marital_status = st.selectbox(
        "Marital Status",
        [
            "Single",
            "Married",
            "Divorced"
        ]
    )

    business_travel = st.selectbox(
        "Business Travel",
        [
            "Travel_Rarely",
            "Travel_Frequently",
            "Non-Travel"
        ]
    )

    education_field = st.selectbox(
        "Education Field",
        [
            "Life Sciences",
            "Medical",
            "Marketing",
            "Technical Degree",
            "Human Resources",
            "Other"
        ]
    )

st.markdown("<br>", unsafe_allow_html=True)

predict = st.button(
    "🔍 Predict Employee Attrition",
    use_container_width=True,
    type="primary"
)

if predict:

    # ===========================
    # CREATE INPUT DATAFRAME
    # ===========================

    input_data = {
        "Age": age,
        "Department": department,
        "JobRole": job_role,
        "MonthlyIncome": monthly_income,
        "YearsAtCompany": years_at_company,
        "OverTime": overtime,
        "JobSatisfaction": job_satisfaction,
        "TotalWorkingYears": total_working_years,
        "DistanceFromHome": distance_from_home,
        "EnvironmentSatisfaction": environment_satisfaction,
        "NumCompaniesWorked": companies_worked,
        "WorkLifeBalance": worklife_balance,
        "MaritalStatus": marital_status,
        "BusinessTravel": business_travel,
        "EducationField": education_field,
        "Gender": gender
    }

    input_df = pd.DataFrame([input_data])

    # ===========================
    # LABEL ENCODING
    # ===========================

    for column in categorical_columns:
        input_df[column] = label_encoders[column].transform(input_df[column])

    input_df = input_df[feature_columns]

    # ===========================
    # SCALING
    # ===========================

    scaled_input = scaler.transform(input_df)

    # ===========================
    # LOGISTIC REGRESSION
    # ===========================

    log_pred = logistic_model.predict(scaled_input)[0]
    log_prob = logistic_model.predict_proba(scaled_input)[0][1]

    # ===========================
    # DECISION TREE
    # ===========================

    dt_pred = dt_model.predict(input_df)[0]
    dt_prob = dt_model.predict_proba(input_df)[0][1]

    # ===========================
    # RANDOM FOREST
    # ===========================

    rf_pred = rf_model.predict(input_df)[0]
    rf_prob = rf_model.predict_proba(input_df)[0][1]

    # ===========================
    # BEST MODEL PREDICTION
    # ===========================

    if best_model_name == "Logistic Regression":

        prediction = log_pred
        probability = log_prob

    elif best_model_name == "Decision Tree":

        prediction = dt_pred
        probability = dt_prob

    else:

        prediction = rf_pred
        probability = rf_prob

    prediction_label = target_encoder.inverse_transform([prediction])[0]

    leave_probability = probability * 100
    stay_probability = 100 - leave_probability

    st.markdown("---")

    st.subheader("📊 Prediction Result")

    left, right = st.columns([1,1])

    # ===========================
    # RESULT CARD
    # ===========================

    with left:

        if prediction_label == "Yes":

            st.error("### ❌ Employee is likely to Leave")

        else:

            st.success("### ✅ Employee is likely to Stay")

        st.metric(
            "Leave Probability",
            f"{leave_probability:.2f}%"
        )

        st.metric(
            "Stay Probability",
            f"{stay_probability:.2f}%"
        )

        st.progress(int(leave_probability))

        if leave_probability < 30:

            st.success("🟢 Low Attrition Risk")

        elif leave_probability < 70:

            st.warning("🟡 Medium Attrition Risk")

        else:

            st.error("🔴 High Attrition Risk")

    # ===========================
    # GAUGE CHART
    # ===========================

    with right:

        gauge = go.Figure(go.Indicator(

            mode="gauge+number",

            value=leave_probability,

            title={"text":"Attrition Risk (%)"},

            gauge={

                "axis":{"range":[0,100]},

                "bar":{"color":"#7C3AED"},

                "steps":[

                    {"range":[0,40],"color":"#1E3A5F"},

                    {"range":[40,70],"color":"#3D5A80"},

                    {"range":[70,100],"color":"#7C3AED"}

                ]

            }

        ))

        gauge.update_layout(
            height=330,
            margin=dict(l=10,r=10,t=60,b=10)
        )

        st.plotly_chart(
            gauge,
            use_container_width=True
        )

    st.markdown("---")

    chart1, chart2 = st.columns(2)

    # ===========================
    # DOUGHNUT CHART
    # ===========================

    with chart1:

        donut = go.Figure(

            data=[

                go.Pie(

                    labels=["Stay","Leave"],

                    values=[stay_probability,leave_probability],

                    hole=0.65

                )

            ]

        )

        donut.update_layout(

            title="Prediction Probability",

            height=350

        )

        st.plotly_chart(
            donut,
            use_container_width=True
        )

    # ===========================
    # AI RECOMMENDATIONS
    # ===========================

    with chart2:

        st.subheader("💡 AI Recommendation")

        if leave_probability < 30:

            st.success("""
### 🟢 Low Risk

The employee shows a **low probability of attrition**.

#### Suggested Actions

- Continue employee engagement.
- Reward good performance.
- Maintain current work environment.
- Encourage career growth.
            """)

        elif leave_probability < 70:

            st.warning("""
### 🟡 Medium Risk

The employee has a **moderate chance of leaving**.

#### Suggested Actions

- Conduct one-on-one meetings.
- Review salary and incentives.
- Improve work-life balance.
- Provide learning opportunities.
            """)

        else:

            st.error("""
### 🔴 High Risk

The employee is **highly likely to leave**.

#### Suggested Actions

- Immediate HR intervention.
- Discuss career progression.
- Offer retention benefits.
- Review workload and manager feedback.
            """)

    st.markdown("---")

    # ===========================
    # MODEL COMPARISON
    # ===========================

    st.subheader("📈 Model Comparison")

    comparison_df = pd.DataFrame({

        "Model": list(metrics.keys()),

        "Accuracy": [
            metrics["Logistic Regression"]["Accuracy"],
            metrics["Decision Tree"]["Accuracy"],
            metrics["Random Forest"]["Accuracy"]
        ],

        "F1 Score": [
            metrics["Logistic Regression"]["F1 Score"],
            metrics["Decision Tree"]["F1 Score"],
            metrics["Random Forest"]["F1 Score"]
        ],

        "ROC AUC": [
            metrics["Logistic Regression"]["ROC AUC"],
            metrics["Decision Tree"]["ROC AUC"],
            metrics["Random Forest"]["ROC AUC"]
        ]

    })

    st.dataframe(
        comparison_df,
        use_container_width=True,
        hide_index=True
    )

    # ===========================
    # ACCURACY BAR CHART
    # ===========================

    fig = go.Figure()

    fig.add_trace(

        go.Bar(

            x=comparison_df["Model"],

            y=comparison_df["Accuracy"],

            text=[
                f"{x:.4f}" for x in comparison_df["Accuracy"]
            ],

            textposition="outside",

            marker_color=[
                "#00D4FF",
                "#7C3AED",
                "#22C55E"
            ]

        )

    )

    fig.update_layout(

        title="Model Accuracy Comparison",

        xaxis_title="Models",

        yaxis_title="Accuracy",

        template="plotly_dark",

        height=450

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ===========================
    # BEST MODEL CARD
    # ===========================

    st.success(
        f"""
## 🏆 Best Performing Model

**{best_model_name}**

This model achieved the highest evaluation score during training and is used for the final prediction.
"""
    )

    st.markdown("---")

    footer1, footer2, footer3 = st.columns(3)

    footer1.metric(
        "Best Model",
        best_model_name
    )

    footer2.metric(
        "Prediction",
        "Leave" if prediction_label == "Yes" else "Stay"
    )

    footer3.metric(
        "Risk",
        f"{leave_probability:.2f}%"
    )

st.markdown("---")

st.markdown(
"""
<div style='text-align:center;'>

### 👨‍💼 Employee Attrition Prediction System

Developed using **Python • Streamlit • Scikit-Learn • Plotly**

**Logistic Regression | Decision Tree | Random Forest**

</div>
""",
unsafe_allow_html=True
)