from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Loan_application(BaseModel):
    age:int
    income:float
    loan_amount:float
    employment_year:int

