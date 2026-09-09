import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

question = "How many days of annual leave do employees receive?"

result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=question
)

question_embedding = result.embeddings[0].values

print("Question:", question)
print("Embedding length:", len(question_embedding))
print("First 5 values:", question_embedding[:5])