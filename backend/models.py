from pydantic import BaseModel

class Reminder(BaseModel):
    task: str
    trigger_type: str
    time: str
    location: str