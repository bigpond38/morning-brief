import os
import requests

api_key = os.environ["GEMINI_API_KEY"]

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"

payload = {
    "contents": [
        {
            "parts": [
                {
                    "text": "Say hello to Harry."
                }
            ]
        }
    ]
}

response = requests.post(url, json=payload)

print("Status:", response.status_code)
print(response.text)
