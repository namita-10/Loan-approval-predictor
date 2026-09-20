# Loan Approval Predictor – LoanWise

## Project Overview
LoanWise is a Machine Learning-based web application that predicts
loan approval status based on applicant financial details.

The application uses a Random Forest Classifier to predict whether
a loan is likely to be approved or not.

## Features
- Loan approval prediction using Machine Learning
- Interactive Streamlit user interface
- FastAPI backend for prediction
- Displays approval status
- User-friendly LoanWise dashboard

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- FastAPI
- Streamlit
- Joblib

## Machine Learning Model
Algorithm: Random Forest Classifier

Dataset: loans.csv

Input Features:
- Income
- Credit Score
- Loan Amount
- Employment Years

Target Variable:
- Loan Status (Approved / Not Approved)

## Project Structure

Loan-approval-predictor/
├── app.py
├── main.py
├── train_model.py
├── loans.csv
├── requirements.txt
├── README.md
├── .gitignore
└── models/
    └── loan_model.pkl

## Installation & Setup

### 1. Clone the Repository
git clone https://github.com/namita-10/Loan-approval-predictor.git

### 2. Navigate to the Project Folder
cd Loan-approval-predictor

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Start FastAPI Backend
uvicorn main:app --reload

### 5. Start Streamlit Frontend
Open another terminal and run:

streamlit run app.py

## Application Access
Frontend: http://localhost:8501

API Documentation: http://127.0.0.1:8000/docs

## Disclaimer
This project is developed for educational purposes.
Predictions are based on a sample dataset and should not be
used as the sole basis for real-world lending decisions.

