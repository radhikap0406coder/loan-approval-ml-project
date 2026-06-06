import streamlit as st
import requests

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Loan Approval Prediction")
st.write("Enter applicant details and predict loan approval status.")

# -----------------------------
# Input Section
# -----------------------------
col1, col2 = st.columns(2)

with col1:

    no_of_dependents = st.number_input(
        "Number of Dependents",
        min_value=0,
        step=1
    )

    education = st.selectbox(
        "Education",
        ["Graduate", "Not Graduate"]
    )

    self_employed = st.selectbox(
        "Self Employed",
        ["Yes", "No"]
    )

    income_annum = st.number_input(
        "Annual Income",
        min_value=0.0,
        step=10000.0,
        format="%.0f"
    )

    loan_amount = st.number_input(
        "Loan Amount",
        min_value=0.0,
        step=10000.0,
        format="%.0f"
    )

with col2:

    loan_term = st.number_input(
        "Loan Term (Months)",
        min_value=1,
        step=1
    )

    cibil_score = st.slider(
        "CIBIL Score",
        min_value=300,
        max_value=900,
        value=750
    )

    residential_assets_value = st.number_input(
        "Residential Assets Value",
        min_value=0.0,
        step=10000.0,
        format="%.0f"
    )

    commercial_assets_value = st.number_input(
        "Commercial Assets Value",
        min_value=0.0,
        step=10000.0,
        format="%.0f"
    )

    luxury_assets_value = st.number_input(
        "Luxury Assets Value",
        min_value=0.0,
        step=10000.0,
        format="%.0f"
    )

    bank_asset_value = st.number_input(
        "Bank Asset Value",
        min_value=0.0,
        step=10000.0,
        format="%.0f"
    )

# -----------------------------
# Predict Button
# -----------------------------
if st.button("Predict Loan Status"):

    payload = {
        "no_of_dependents": no_of_dependents,
        "education": education,
        "self_employed": self_employed,
        "income_annum": income_annum,
        "loan_amount": loan_amount,
        "loan_term": loan_term,
        "cibil_score": cibil_score,
        "residential_assets_value": residential_assets_value,
        "commercial_assets_value": commercial_assets_value,
        "luxury_assets_value": luxury_assets_value,
        "bank_asset_value": bank_asset_value
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload
        )

        result = response.json()

        st.divider()

        # -----------------------------
        # Error handling
        # -----------------------------
        if "error" in result:
            st.error(f"❌ Backend Error: {result['error']}")
            st.stop()

        # -----------------------------
        # Output
        # -----------------------------
        if result["loan_status"] == "Approved":
            st.success("✅ Loan Approved")
        else:
            st.error("❌ Loan Rejected")

        st.metric(
            "Confidence Score",
            f"{result['confidence']:.2%}"
        )

    except Exception:
        st.error(
            "❌ Could not connect to FastAPI server. Make sure it is running."
        )