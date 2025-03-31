import sqlite3
from datetime import datetime, timedelta

# Connect to SQLite database (or create if it doesn't exist)
conn = sqlite3.connect("tickets.db")
cursor = conn.cursor()

# Create 'tickets' table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    priority TEXT,
    assignee TEXT,
    created_on DATE
);
""")

# Insert sample data
sample_data = [
    ("High", "John", (datetime.today() - timedelta(days=1)).date()),  # Yesterday
    ("Medium", "Alice", (datetime.today() - timedelta(days=7)).date()),  # Last week
    ("Low", "Bob", (datetime.today() - timedelta(days=30)).date()),  # Last month
]

cursor.executemany("INSERT INTO tickets (priority, assignee, created_on) VALUES (?, ?, ?);", sample_data)

# Commit changes and close connection
conn.commit()
conn.close()

print("Database 'tickets.db' created successfully with sample data!")
