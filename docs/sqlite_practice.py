import sqlite3

conn = sqlite3.connect("test.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

cursor.execute(
    "INSERT INTO users (name, age) VALUES (?, ?)",
    ("Arushi", 21)
)

cursor.execute("SELECT * FROM users")

rows = cursor.fetchall()

print(rows)

conn.commit()

print("User added successfully")

conn.close()
