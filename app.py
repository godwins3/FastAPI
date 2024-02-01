from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
async def home():
    return {'Message': 'Hello FastAPI'}

@app.get('/hello/{name}/{age}')
async def Hello(name: str, age: int):

    return {f'My name is {name} and am {age} years old'}

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=5000, reload=True)