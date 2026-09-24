import sqlite3


connection = sqlite3.connect("expense_tracker.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        amount REAL NOT NULL,
        type TEXT NOT NULL,
        category TEXT,
        date TEXT
    )
""")

connection.commit()
connection.close()

print("Database and transactions table created!")