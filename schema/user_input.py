from typing import Annotated
from pydantic import BaseModel, Field
from pydantic import field_validator


class UserInput(BaseModel):

    no_of_dependents: Annotated[
        int,
        Field(
            ge=0,
            le=20,
            description="Number of dependents"
        )
    ]

    education: Annotated[
        str,
        Field(
            description="Education level: Graduate or Not Graduate"
        )
    ]

    self_employed: Annotated[
        str,
        Field(
            description="Employment status: Yes or No"
        )
    ]

    income_annum: Annotated[
        float,
        Field(
            gt=0,
            description="Annual income in rupees"
        )
    ]

    loan_amount: Annotated[
        float,
        Field(
            gt=0,
            description="Requested loan amount"
        )
    ]

    loan_term: Annotated[
        int,
        Field(
            ge=1,
            le=30,
            description="Loan term in years"
        )
    ]

    cibil_score: Annotated[
        int,
        Field(
            ge=300,
            le=900,
            description="Applicant CIBIL score"
        )
    ]

    residential_assets_value: Annotated[
        float,
        Field(
            ge=0,
            description="Value of residential assets"
        )
    ]

    commercial_assets_value: Annotated[
        float,
        Field(
            ge=0,
            description="Value of commercial assets"
        )
    ]

    luxury_assets_value: Annotated[
        float,
        Field(
            ge=0,
            description="Value of luxury assets"
        )
    ]

    bank_asset_value: Annotated[
        float,
        Field(
            ge=0,
            description="Bank asset value"
        )
    ]

    @field_validator("education")
    @classmethod
    def validate_education(cls, value):

        allowed = ["Graduate", "Not Graduate"]

        if value not in allowed:
            raise ValueError(
                f"Education must be one of {allowed}"
            )

        return value

    @field_validator("self_employed")
    @classmethod
    def validate_self_employed(cls, value):

        allowed = ["Yes", "No"]

        if value not in allowed:
            raise ValueError(
                f"Self employed must be one of {allowed}"
            )

        return value