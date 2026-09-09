import os
import json
import numpy as np
from database import db
from dotenv import load_dotenv
from google import genai

load_dotenv()

# Gemini
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
cursor = db.cursor(dictionary=True)

# 1. User question
question = "I'm planning a vacation. How much annual leave can I take, and who do I need to inform?"

# 2. Create question embedding
result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=question
)

question_embedding = np.array(result.embeddings[0].values)

# 3. Get stored chunks
cursor.execute(
    "SELECT id, content, embedding FROM document_chunks"
)

chunks = cursor.fetchall()

# 4. Compare question with every chunk
best_chunk = None
best_similarity = -1
results = []

for chunk in chunks:

    chunk_embedding = np.array(
        json.loads(chunk["embedding"])
    )

    similarity = np.dot(question_embedding, chunk_embedding) / (
        np.linalg.norm(question_embedding) *
        np.linalg.norm(chunk_embedding)
    )

    results.append({
        "content": chunk["content"],
        "similarity": similarity
    })
results.sort(
    key=lambda x: x["similarity"],
    reverse=True
)    
prompt = f"""
Answer the user's question using only the information provided below.

Information:
{results}

Question:
{question}
"""

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)

print("Answer:")
print(response.text)