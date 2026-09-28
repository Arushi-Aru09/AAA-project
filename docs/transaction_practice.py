import sqlite3

conn = sqlite3.connect("test.db")

try:
    conn.execute("BEGIN")

    conn.execute(
        "INSERT INTO users(name, age) VALUES (?, ?)",
        ("Ravi", 25)
    )

    conn.commit()
    print("Transaction successful")

except Exception as e:
    conn.rollback()
    print("Transaction failed")

conn.close()