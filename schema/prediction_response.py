from pydantic import BaseModel, Field

class PredictionResponse(BaseModel):

    loan_status: str = Field(
        description="Predicted loan approval status"
    )

    confidence: float = Field(
        description="Prediction confidence score"
    )