import sqlite3

db_path = "finance_tracker.db"
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    category TEXT NOT NULL,
    amount REAL NOT NULL,
    description TEXT
)
""")

connection.commit()
connection.close()

print("✅ Database initialized successfully!")
