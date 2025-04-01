import sqlite3

conn = sqlite3.connect('tickets.db')
cursor = conn.cursor()

# Check database integrity
cursor.execute('PRAGMA integrity_check;')
result = cursor.fetchone()
if result[0] != 'ok':
    print("Database is corrupt!")
else:
    print("Database integrity is OK.")
