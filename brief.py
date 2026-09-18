from google import genai
import os

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Give me a 3 sentence summary of today's global financial markets."
)

print(response.text)
