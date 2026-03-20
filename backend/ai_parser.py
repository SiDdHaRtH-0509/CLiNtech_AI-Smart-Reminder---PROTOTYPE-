import openai
import json
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def parse_command(user_input):
    return {
        "task": user_input,
        "trigger_type": "time",
        "time": "7 PM",
        "location": "Home",
        "confidence": 0.95
    }

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    try:
        output = response.choices[0].message.content
        return json.loads(output)
    except:
        return {
            "task": user_input,
            "trigger_type": "time",
            "time": "unknown",
            "location": "unknown",
            "confidence": 0.5
        }