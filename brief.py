import os

api_key = os.environ.get("GEMINI_API_KEY")

print("Key exists:", api_key is not None)

if api_key:
    print("First 5 chars:", api_key[:5])
    print("Length:", len(api_key))
else:
    print("No key found")
