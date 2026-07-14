from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

students = {
    101:{"name":"Raghav", "marks":100, "grade":"A"},
    102:{"name":"Rajesh", "marks":80, "grade":"B"},
    103:{"name":"Rajesh", "marks":70, "grade":"C"},
    104:{"name":"Rajesh", "marks":60, "grade":"D"},
    105:{"name":"Rajesh", "marks":50, "grade":"E"},
    106:{"name":"Rajesh", "marks":40, "grade":"F"},
    107:{"name":"Rajesh", "marks":30, "grade":"G"},
    108:{"name":"Rajesh", "marks":20, "grade":"H"},
    109:{"name":"Rajesh", "marks":10, "grade":"I"},
    110:{"name":"Rajesh", "marks":0, "grade":"J"},
}

class student(BaseModel):
    student_id:int
    name:str
    marks:int
    grade:str


@app.get("/students/{student_id}")
def get_student(student_id:int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id]


