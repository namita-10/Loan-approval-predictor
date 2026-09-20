from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

# Initialize FastAPI
app = FastAPI(title="Loan Approval Predictor API")

# Load trained ML model
with open("models/loan_model.pkl", "rb") as file:
    model = pickle.load(file)


# Input data format
class LoanDetails(BaseModel):
    income: float
    credit_score: int
    loan_amount: float
    employment_years: int


# Home route
@app.get("/")
def home():
    return {
        "message": "Loan Approval Predictor API is running!"
    }


# Prediction route
@app.post("/predict")
def predict_loan(data: LoanDetails):

    input_data = pd.DataFrame([{
        "income": data.income,
        "credit_score": data.credit_score,
        "loan_amount": data.loan_amount,
        "employment_years": data.employment_years
    }])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        result = "Loan Approved"
    else:
        result = "Loan Not Approved"

    return {
        "prediction": int(prediction),
        "result": result
    }