import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("tickets_predicted.db")
cursor = conn.cursor()

'''
# Delete rows except the first 200 based on Ticket_ID
cursor.execute("""
DELETE FROM tickets WHERE Ticket_ID > 200
""")
print("Deleted all rows except the first 200.")
'''
'''
# Step 1: Add the new column 'Ticket_Type' if not exists
cursor.execute("ALTER TABLE tickets ADD COLUMN Ticket_Type TEXT")
print("Added 'Ticket_Type' column successfully.")

# Step 2: Define ticket types (200 values in order)
ticket_types = [
    "Technical issue", "Technical issue", "Technical issue", "Billing inquiry", "Billing inquiry",
    "Cancellation request", "Product inquiry", "Refund request", "Technical issue", "Refund request",
    "Cancellation request", "Product inquiry", "Technical issue", "Technical issue", "Billing inquiry",
    "Billing inquiry", "Product inquiry", "Product inquiry", "Product inquiry", "Refund request",
    "Refund request", "Cancellation request", "Cancellation request", "Technical issue", "Product inquiry",
    "Product inquiry", "Billing inquiry", "Cancellation request", "Technical issue", "Cancellation request",
    "Billing inquiry", "Technical issue", "Billing inquiry", "Refund request", "Refund request",
    "Cancellation request", "Refund request", "Product inquiry", "Technical issue", "Product inquiry",
    "Product inquiry", "Billing inquiry", "Product inquiry", "Technical issue", "Refund request",
    "Product inquiry", "Refund request", "Technical issue", "Cancellation request", "Technical issue",
    "Refund request", "Refund request", "Refund request", "Cancellation request", "Technical issue",
    "Cancellation request", "Technical issue", "Refund request", "Technical issue", "Product inquiry",
    "Cancellation request", "Product inquiry", "Billing inquiry", "Billing inquiry", "Technical issue",
    "Technical issue", "Billing inquiry", "Cancellation request", "Technical issue", "Refund request",
    "Cancellation request", "Refund request", "Billing inquiry", "Cancellation request", "Billing inquiry",
    "Product inquiry", "Cancellation request", "Billing inquiry", "Billing inquiry", "Technical issue",
    "Technical issue", "Cancellation request", "Refund request", "Technical issue", "Technical issue",
    "Product inquiry", "Technical issue", "Technical issue", "Billing inquiry", "Product inquiry",
    "Refund request", "Product inquiry", "Technical issue", "Refund request", "Product inquiry",
    "Product inquiry", "Cancellation request", "Product inquiry", "Billing inquiry", "Technical issue",
    "Cancellation request", "Billing inquiry", "Refund request", "Refund request", "Refund request",
    "Product inquiry", "Cancellation request", "Technical issue", "Technical issue", "Product inquiry",
    "Cancellation request", "Refund request", "Product inquiry", "Cancellation request", "Cancellation request",
    "Technical issue", "Cancellation request", "Billing inquiry", "Refund request", "Billing inquiry",
    "Billing inquiry", "Product inquiry", "Refund request", "Product inquiry", "Technical issue",
    "Refund request", "Billing inquiry", "Refund request", "Cancellation request", "Cancellation request",
    "Billing inquiry", "Product inquiry", "Cancellation request", "Refund request", "Cancellation request",
    "Product inquiry", "Cancellation request", "Technical issue", "Product inquiry", "Cancellation request",
    "Cancellation request", "Technical issue", "Billing inquiry", "Cancellation request", "Refund request",
    "Cancellation request", "Cancellation request", "Billing inquiry", "Refund request", "Technical issue",
    "Refund request", "Refund request", "Product inquiry", "Technical issue", "Technical issue",
    "Cancellation request", "Product inquiry", "Technical issue", "Product inquiry", "Billing inquiry",
    "Refund request", "Refund request", "Refund request", "Cancellation request", "Billing inquiry",
    "Product inquiry", "Refund request", "Technical issue", "Billing inquiry", "Product inquiry",
    "Billing inquiry", "Refund request", "Cancellation request", "Refund request", "Technical issue",
    "Technical issue", "Technical issue", "Cancellation request", "Billing inquiry", "Billing inquiry",
    "Refund request", "Cancellation request", "Product inquiry", "Billing inquiry", "Refund request",
    "Technical issue", "Product inquiry", "Cancellation request", "Refund request", "Technical issue",
    "Refund request", "Product inquiry", "Product inquiry", "Cancellation request", "Billing inquiry",
    "Refund request", "Refund request", "Refund request", "Cancellation request", "Product inquiry"
]

# Step 3: Update the table with Ticket_Type values
cursor.execute("SELECT Ticket_ID FROM tickets ORDER BY Ticket_ID LIMIT 200")
ticket_ids = [row[0] for row in cursor.fetchall()]  # Fetch first 200 Ticket_IDs

for ticket_id, ticket_type in zip(ticket_ids, ticket_types):
    cursor.execute("UPDATE tickets SET Ticket_Type=? WHERE Ticket_ID=?", (ticket_type, ticket_id))
'''

'''
# Add the "Assignee" column if it doesn't exist
cursor.execute("""
    ALTER TABLE tickets ADD COLUMN Assignee TEXT
""")

# Mapping of Ticket_Type to Assignee
assignee_mapping = {
    "Technical issue": "John",
    "Billing inquiry": "Sam",
    "Cancellation request": "Mary",
    "Product inquiry": "Nancy",
    "Refund request": "Bob"
}

# Update the Assignee column based on Ticket_Type
for ticket_type, assignee in assignee_mapping.items():
    cursor.execute("""
        UPDATE tickets SET Assignee = ? WHERE Ticket_Type = ?
    """, (assignee, ticket_type))
'''


# Commit and close connection
conn.commit()
conn.close()

