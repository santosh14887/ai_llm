import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai
load_dotenv()
conversation = []
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
app = FastAPI()
class MessageRequest(BaseModel):
    message: str
    name: str

@app.get("/")
def home():
    return {"name" : "santosh"}
@app.get("/users")
def getUser():
    return {
        "users": [
            "Santosh",
            "Rahul",
            "Amit"
        ]
    }
@app.get("/getSpecificUser")
def getSpecificUser(name: str):
    return {"message", f"name is {name}"}
@app.get("/doSquare")
def doSquare(num: int):
    return {
        "number" : num,
        "result" : num*num
        }
@app.post("/messages")
def postMethod(data : MessageRequest):
    return {
    "received": data
    }
@app.post("/chat")
def chat(data: MessageRequest):
    conversation.append({
            "role": "user",
            "message": data.message
        })
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=str(conversation)
    )
    conversation.append({
        "role": "assistant",
        "message": response.text
    })

    return {
        "answer": response.text,
        "history": conversation
    }