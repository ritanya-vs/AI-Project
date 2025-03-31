from datetime import datetime, timedelta

# Mapping extracted time ranges to SQL-compatible date filters
TIME_MAPPINGS = {
    "today": lambda: f"DATE(created_on) = '{datetime.today().date()}'",
    "yesterday": lambda: f"DATE(created_on) = '{(datetime.today() - timedelta(days=1)).date()}'",
    "last week": lambda: f"created_on >= '{(datetime.today() - timedelta(days=7)).date()}'",
    "last month": lambda: f"created_on >= '{(datetime.today() - timedelta(days=30)).date()}'",
}

def generate_sql_filter(extracted_data):
    """
    Converts extracted attributes into an SQL WHERE clause.
    """
    conditions = []

    # Handle priority
    if extracted_data["priority"]:
        conditions.append(f"priority = '{extracted_data['priority'].capitalize()}'")

    # Handle assignee
    if extracted_data["assignee"]:
        conditions.append(f"assignee = '{extracted_data['assignee']}'")

    # Handle time range
    if extracted_data["time_range"] and extracted_data["time_range"] in TIME_MAPPINGS:
        conditions.append(TIME_MAPPINGS[extracted_data["time_range"]]())

    # Combine conditions with AND
    where_clause = " AND ".join(conditions) if conditions else "1=1"  # Default to all records

    # Full SQL Query
    sql_query = f"SELECT * FROM tickets WHERE {where_clause};"
    
    return sql_query

# Example usage
if __name__ == "__main__":
    extracted_info = {
        "priority": "high",
        "assignee": "John",
        "time_range": "last week"
    }

    sql_query = generate_sql_filter(extracted_info)
    print("Generated SQL Query:", sql_query)
