import os

api_key = os.environ["GEMINI_API_KEY"]

print("First 4 chars:", api_key[:4])
print("Length:", len(api_key))
