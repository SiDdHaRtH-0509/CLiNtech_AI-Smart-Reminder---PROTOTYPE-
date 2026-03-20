import time
from datetime import datetime

reminders = []

def add_reminder(data):
    reminders.append(data)

def check_reminders():
    triggered = []
    now = datetime.now().strftime("%H:%M")

    for r in reminders:
        if r["trigger_type"] == "time" and r["time"] in now:
            triggered.append(r)

    return triggered