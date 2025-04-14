import sqlite3
import os

# Get the absolute path of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Combine with 'tickets.db' to get the full path to the database
db_path = os.path.join(script_dir, 'tickets.db')

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Query all records from the tickets table
cursor.execute("SELECT * FROM tickets;")
tickets = cursor.fetchall()

print("Tickets in the database:", tickets)

# Close the connection
conn.close()
