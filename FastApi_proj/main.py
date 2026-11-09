from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
arr = {1: {'name': 'kiran'}, 2: {'name': 'kumar'}}


class EmployeeCreate(BaseModel):
    emp_id: int
    emp_name: str

@app.get('/employees/{emp_id}')
def get_employees(emp_id:int):
    if emp_id in arr:
        data = arr[emp_id]
        return data
    else:
        return "Employee details not found"


# @app.post('/employees')
# def get_employees(data: EmployeeCreate):
#     arr[data['emp_id']] = 