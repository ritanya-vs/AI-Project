import sqlite3

# Database file
DB_FILE = "tickets_database.db"

def initialize_database():
    """
    Creates a 'tickets' table with sample data if not exists.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            Ticket ID INTEGER PRIMARY KEY AUTOINCREMENT,
            priority TEXT,
            assignee TEXT,
            created_on DATE
        )
    """)

    # Insert sample data
    sample_data = [
        ("High", "John", "2024-03-20"),
        ("Medium", "Alice", "2024-03-22"),
        ("Low", "Bob", "2024-03-18"),
        ("High", "Emma", "2024-03-25"),
    ]
    
    cursor.executemany("INSERT INTO tickets (priority, assignee, created_on) VALUES (?, ?, ?)", sample_data)
    
    conn.commit()
    conn.close()

def execute_query(sql_query):
    """
    Executes the given SQL query and returns the results.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute(sql_query)
    results = cursor.fetchall()
    
    conn.close()
    return results

# Run the database initialization if script is executed directly
if __name__ == "__main__":
    initialize_database()
    print("Database initialized with sample tickets.")
