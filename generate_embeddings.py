import os
import json
from dotenv import load_dotenv
from google import genai
from database import db

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

cursor = db.cursor()

cursor.execute("SELECT id, content FROM document_chunks WHERE embedding IS NULL")

chunks = cursor.fetchall()

for chunk_id, content in chunks:

    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=content
    )

    embedding = result.embeddings[0].values

    embedding_json = json.dumps(embedding)

    cursor.execute(
        "UPDATE document_chunks SET embedding = %s WHERE id = %s",
        (embedding_json, chunk_id)
    )

db.commit()

print("Embeddings generated successfully")

cursor.close()
db.close()