from fastapi import FastAPI, Body, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from pydantic import BaseModel
from typing import List
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates=Jinja2Templates(directory="templates")

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
async def my_template():
    temp = """
<html>
<head></head>
<body>
<p> Hello World</p>
</body>
</html>
"""
    return HTMLResponse(content=temp)

@app.get("/helloworld", response_class=HTMLResponse)
async def hello(request: Request):
    # Jinja2Templates.TemplateResponse
    return templates.TemplateResponse(request=request, name='hello.html')

@app.get("/items/{id}/", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    user_id = id
    return templates.TemplateResponse(request=request, name="hello.html", context={"user_id": user_id})

@app.get('/weuh/{name}')
async def weuh(request: Request, name: str):
    return templates.TemplateResponse("index.html", {"request": request, "name":name})

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=5000, reload=True)