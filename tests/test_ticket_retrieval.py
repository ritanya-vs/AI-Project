import sys
import os

# Add the 'backend' directory to the system path to access the query_translator module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "backend")))

from query_translator import generate_sql_filter, execute_query

def test_ticket_retrieval():
    # Example extracted data that would be passed to the query generation function
    extracted_data = {
        "priority": "high",
        "assignee": "John",
        "time_range": "last week"
    }

    # Generate the SQL query based on the extracted data
    sql_query = generate_sql_filter(extracted_data)
    print("Generated SQL Query:", sql_query)

    # Specify the correct path to the tickets_database.db file in the backend directory
    db_path = os.path.join(os.path.dirname(__file__), '..', 'backend', 'tickets_database.db')

    # Execute the query and retrieve results, passing the correct db_path
    results = execute_query(sql_query, db_path=db_path)
    
    # Print the results (you can modify this based on what the expected results should be)
    print("Query Results:", results)

    # Perform assertions if needed, for example, check that there are results
    assert len(results) > 0, "No tickets found for the given criteria"
    print(f"Retrieved {len(results)} tickets successfully!")

# Run the test
test_ticket_retrieval()
