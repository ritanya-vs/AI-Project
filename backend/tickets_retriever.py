from query_translator import generate_sql_filter, execute_query 
from nlu import classify_intent

def retrieve_tickets(extracted_data):
    """
    Retrieves tickets from the database based on the extracted data.
    """
    # Classify priority using BART
    extracted_data["Ticket Priority"] = classify_intent(extracted_data["Ticket Subject"])

    # Generate SQL query
    sql_query = generate_sql_filter(extracted_data)

    # Execute and return results
    return execute_query(sql_query)


# Example usage
if __name__ == "__main__":
    extracted_data = {
        "priority": "high",
        "assignee": "John",
        "time_range": "last week"
    }

    tickets = retrieve_tickets(extracted_data)
    print("Filtered Tickets:", tickets)
