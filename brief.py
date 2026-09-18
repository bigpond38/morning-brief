import os

api_key = os.environ["GEMINI_API_KEY"]

print(type(api_key))
print("Length:", len(api_key))
print("Start:", api_key[:4])
print("End:", api_key[-4:])
