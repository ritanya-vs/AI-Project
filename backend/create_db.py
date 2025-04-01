import sqlite3
from datetime import datetime, timedelta

def create_test_database(db_path="tickets.db"):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Create tickets table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                priority TEXT,
                assignee TEXT,
                created_on TEXT
            );
        ''')

        # Insert sample tickets for testing
        cursor.executemany('''
            INSERT INTO tickets (priority, assignee, created_on)
            VALUES (?, ?, ?);
        ''', [
            ('High', 'John', (datetime.today() - timedelta(days=3)).date()),  # Last week
            ('Medium', 'Jane', (datetime.today() - timedelta(days=5)).date()),  # Last week
            ('Low', 'John', (datetime.today() - timedelta(days=10)).date()),  # Older than last week
        ])
        
        conn.commit()
        conn.close()
        print("Database and sample data created successfully.")
    except Exception as e:
        print("Failed to create database or insert data:", str(e))

# Call the function to create the database and sample data
create_test_database()
