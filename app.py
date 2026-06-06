from fastapi import FastAPI, HTTPException

from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse

from model.predict import predict_loan

app = FastAPI(
    title="Loan Approval Prediction API",
    description="Predict whether a loan application will be approved or rejected",
    version="1.0.0"
)


@app.get("/")
def home():
    return {"message": "Loan Approval Prediction API Running"}


@app.post( "/predict",
    response_model=PredictionResponse,
    summary="Predict Loan Approval",
    description="""
    This endpoint predicts whether a loan application
    will be approved or rejected based on applicant details.

    Input:
    - Personal Information
    - Income Details
    - Asset Information
    - CIBIL Score

    Output:
    - Approved
    - Rejected
    """)
def predict(data: UserInput):

    try:
        prediction, confidence = predict_loan(
            data.model_dump()
        )

        result = "Approved" if prediction == 1 else "Rejected"

        return PredictionResponse(
            loan_status=result,
            confidence=float(confidence)
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    
