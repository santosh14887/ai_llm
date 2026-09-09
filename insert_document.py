from database import db

cursor = db.cursor()

sql = """
INSERT INTO documents (title, content)
VALUES (%s, %s)
"""

title = "Employee Handbook"
content = "Employees receive 20 days of annual leave every year."

cursor.execute(sql, (title, content))

db.commit()

print("Document inserted successfully")

cursor.close()
db.close()