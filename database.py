import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ai_app"
)

print("Database connected successfully")