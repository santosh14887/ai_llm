import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

result = client.models.embed_content(
    model="gemini-embedding-001",
    contents="Employees receive 20 days of annual leave."
)

print(result.embeddings[0].values)