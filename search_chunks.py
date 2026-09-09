from database import db
import json


cursor = db.cursor(dictionary=True)

cursor.execute("SELECT id, content, embedding FROM document_chunks")

chunks = cursor.fetchall()

for chunk in chunks:
    print("ID:", chunk["id"])
    print("Content:", chunk["content"])

    embedding = json.loads(chunk["embedding"])

    print("Embedding length:", len(embedding))
    print("--------------------")