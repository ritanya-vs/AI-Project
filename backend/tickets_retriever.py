from query_translator import generate_sql_filter, execute_query

def retrieve_tickets(extracted_data):
    """
    Retrieves tickets from the database based on the extracted data.
    """
    # Generate the SQL query from the extracted data
    sql_query = generate_sql_filter(extracted_data)

    # Execute the query and retrieve results
    tickets = execute_query(sql_query)
    
    return tickets

# Example usage
if __name__ == "__main__":
    extracted_data = {
        "priority": "high",
        "assignee": "John",
        "time_range": "last week"
    }

    tickets = retrieve_tickets(extracted_data)
    print("Filtered Tickets:", tickets)
