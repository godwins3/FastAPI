from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
import uvicorn
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Student(BaseModel):
    id: str
    name: str
    subject: List[str] = []


@app.get('/')
async def home():
    return {'Message': 'Hello FastAPI'}

@app.get('/hello/{name}/{age}')
async def Hello(name: str, age: int):

    return {f'My name is {name} and am {age} years old'}

@app.post('/students')
async def student_data(s1: Student):

    return s1

@app.post("/students_data")
async def student_data(name:str=Body(...), marks:int=Body(...)):

    return {"name":name, "marks": marks}

@app.get('/templates')
async def templates():
    temp = """
<html>
<head></head>
<body>
<p> Hello World</p>
</body>
</html>
"""
    return HTMLResponse(content=temp)


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=5000, reload=True)