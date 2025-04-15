from decouple import config
import requests
import json

def query_openrouter(prompt):
    headers = {
        "Authorization": f"Bearer {config('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:8000",
        "X-Title": "My Django App",
    }

    payload = {
        "model": "openai/gpt-4o",  # or any supported model
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 800
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions",
                             headers=headers, data=json.dumps(payload))

    return response.json()
