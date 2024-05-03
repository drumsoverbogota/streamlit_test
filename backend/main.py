from fastapi import FastAPI
from pydantic import BaseModel
import time

# Initialize FastAPI app
app = FastAPI()

# Message definition
class Message(BaseModel):
    message: str
    user: str

# Define FastAPI endpoints
@app.get("/")
async def read_root():
    return {"message": "Welcome to the API!"}

@app.post("/chat")
async def chat(data: dict):
    time.sleep(3)
    return {"response": "That is interesting!"}