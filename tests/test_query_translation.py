from query_translator import generate_sql_filter

def test_generate_sql_filter():
    extracted_data = {
        "priority": "high",
        "assignee": "John",
        "time_range": "last week"
    }
    expected_sql = "SELECT * FROM tickets WHERE priority = 'High' AND assignee = 'John' AND created_on >= '2024-03-24';"
    assert generate_sql_filter(extracted_data) == expected_sql
