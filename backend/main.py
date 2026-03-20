from fastapi import FastAPI
from pydantic import BaseModel
from ai_parser import parse_command
from reminder_engine import add_reminder, check_reminders
from db import save_reminder
from suggestions import get_suggestions

app = FastAPI()

class UserInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "CLiNtech Backend Running"}

@app.post("/parse")
def parse(input: UserInput):
    parsed = parse_command(input.text)
    return parsed

@app.post("/add_reminder")
def add(parsed: dict):
    add_reminder(parsed)
    save_reminder(parsed)
    return {"status": "Reminder added"}

@app.get("/check_reminders")
def check():
    return check_reminders()

@app.get("/suggestions")
def suggestions():
    return get_suggestions()