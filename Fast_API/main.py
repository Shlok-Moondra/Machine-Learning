from urllib.parse import quote_plus

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

app = FastAPI()

class Loan_application(BaseModel):
    age:int
    income:float
    loan_amount:int
    employment_year:int
  


@app.post("/predict")
def predict_loan(application:Loan_application):
    if application.income > 50000 and application.employment_year > 2:
        decision = "Approved"
    else:
        decision = "Rejected"
    return{
        "decision":decision,
        "reason":f"The loan was {decision} because the income was {application.income} and the employment year was {application.employment_year}"
    }


@app.get("/search")
def search_google(q: str):
    encoded_query = quote_plus(q.strip())
    url = f"https://www.google.com/search?q={encoded_query}"
    return RedirectResponse(url=url)
