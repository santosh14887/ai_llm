from database import db
cursor = db.cursor()

chunks = [
    "Employees receive 20 days of annual leave every year.",
    "Employees must inform their manager before taking leave.",
    "Employees should maintain regular attendance during working hours."
]

sql = """
INSERT INTO document_chunks (document_id, content)
VALUES (%s, %s)
"""

for chunk in chunks:
    cursor.execute(sql, (1, chunk))

db.commit()

print("Chunks inserted successfully")

cursor.close()
db.close()