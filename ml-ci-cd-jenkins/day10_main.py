from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import numpy as np
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from prediction_model.predict import generate_predictions

# Instruction: https://fastapi.tiangolo.com/tutorial/cors/

app = FastAPI(
    title = "Loan Prediction APP using API CI-CD Jenkins",
    description="a simple CICD demo",
    version='1.0'
    )

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class LoanPrediction(BaseModel):  # how incoming data will be past, specify the data type based on train.csv; here it was also mentioned in configuration file: config.py
    Gender: str
    Married: str
    Dependents: str
    Education: str
    Self_Employed: str
    ApplicantIncome: float
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float
    Property_Area: str

@app.get("/")
def index():
    return{"message":"welcome to Loan Prediction APP using API CI-CD Jenkins"}

# if someone is send request to the post 
# when get any data for the function
@app.post("/prediction_api") # the location where it will performing
def predict(loan_detail: LoanPrediction): # create a class for LoanPrediction
    data = loan_detail.model_dump() # convert the incoming data to python dictionary 
    prediction = generate_predictions([data])["prediction"][0] # inside predict.py , currently, the output will be in a dictionary result = {"prediction":output}, 
                                                                #add ["prediction"][0], the first value,  will get the prection value

    if prediction == "Y":
        pred = "Approved"
    else: 
        pred = "Rejected"
    return {"status":pred}


@app.post("/prediction_ui") # another address for another function 
def predict_gui(Gender: str,
    Married: str,
    Dependents: str,
    Education: str,
    Self_Employed: str,
    ApplicantIncome: float,
    CoapplicantIncome: float,
    LoanAmount: float,
    Loan_Amount_Term: float,
    Credit_History: float,
    Property_Area: str):

    input_data = [Gender, Married, Dependents, Education,
       Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount,
       Loan_Amount_Term, Credit_History, Property_Area] # above all
    
    cols = ['Gender', 'Married', 'Dependents', 'Education',
       'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History', 'Property_Area']
    
    data_dict = dict(zip(cols, input_data))
    prediction = generate_predictions([data_dict])["prediction"][0]
    if prediction == "Y":
        pred = "Approved"
    else:
        pred = "Rejected"
    return {"status":pred}

if __name__== "__day10_main__":
    uvicorn.run(app, host="0.0.0.0",port=8005)
    
    
