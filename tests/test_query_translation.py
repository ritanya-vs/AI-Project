import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "backend")))
from query_translator import generate_sql_filter  # Assuming the function you're testing is in query_translator.py

def test_query_translation():
    extracted_data = {
        "priority": "high",
        "assignee": "John",
        "time_range": "last week"
    }
    # Construct the expected SQL query manually based on the logic you want to validate
    expected_sql = "SELECT * FROM tickets WHERE priority = 'High' AND assignee = 'John' AND created_on >= '2025-03-25';"
    
    # Use assert to compare the generated SQL query with the expected SQL query
    assert generate_sql_filter(extracted_data) == expected_sql, f"Expected {expected_sql}, but got {generate_sql_filter(extracted_data)}"

# Run the test
if __name__ == "__main__":
    test_query_translation()
    print("Test passed!")
