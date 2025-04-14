from query_translator import generate_sql_filter, execute_query

def retrieve_tickets(extracted_data):

    valid_keys = {"priority", "assignee", "time_range", "type"}
    extracted_data = {k: v for k, v in extracted_data.items() if k in valid_keys and v}

    sql_query = generate_sql_filter(extracted_data)

    tickets = execute_query(sql_query)
    
    return tickets

if __name__ == "__main__":
    extracted_data = {
        "priority": "high",
        "assignee": "John",
        "time_range": "last week",
        "type": None  
    }

    tickets = retrieve_tickets(extracted_data)
    print("Filtered Tickets:", tickets)
