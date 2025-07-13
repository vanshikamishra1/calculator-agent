import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_deepseek_response(prompt: str) -> str:
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {os.getenv('DEEPSEEK_API_KEY')}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    res = requests.post(url, headers=headers, json=data)
    if res.status_code != 200:
        return f"API Error: {res.status_code} - {res.json()}"

    return res.json()["choices"][0]["message"]["content"]
