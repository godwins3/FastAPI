from fastapi import FastAPI

app = FastAPI() # initialize fastapi app

# create our first endpoint
@app.get('/')
async def home():

    return {'Message': 'Hello FastAPI'}