import sqlite3

conn = sqlite3.connect("reminders.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS reminders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT,
    trigger_type TEXT,
    time TEXT,
    location TEXT
)
""")

def save_reminder(data):
    c.execute(
        "INSERT INTO reminders (task, trigger_type, time, location) VALUES (?, ?, ?, ?)",
        (data["task"], data["trigger_type"], data["time"], data["location"])
    )
    conn.commit()