from fastapi import FastAPI
from core.router import route

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Smart Assistant API running"}

@app.post("/chat")
def chat(user_input: str):
    response = route(user_input)
    return {"response": response}