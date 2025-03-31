from ticket_retriever import retrieve_tickets
from query_translator import initialize_database

def test_retrieve_tickets():
    initialize_database()  # Ensure the database is set up
    extracted_data = {
        "priority": "high",
        "assignee": "John",
        "time_range": "last week"
    }
    tickets = retrieve_tickets(extracted_data)
    assert len(tickets) > 0  # Assuming there are matching tickets in the sample data
