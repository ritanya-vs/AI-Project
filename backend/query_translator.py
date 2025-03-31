import sqlite3
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
    if extracted_data.get("priority"):
        conditions.append(f"priority = '{extracted_data['priority'].capitalize()}'")

    # Handle assignee
    if extracted_data.get("assignee"):
        conditions.append(f"assignee = '{extracted_data['assignee']}'")

    # Handle time range
    if extracted_data.get("time_range") and extracted_data["time_range"] in TIME_MAPPINGS:
        conditions.append(TIME_MAPPINGS[extracted_data["time_range"]]())

    # Combine conditions with AND
    where_clause = " AND ".join(conditions) if conditions else "1=1"  # Default to all records

    # Full SQL Query
    sql_query = f"SELECT * FROM tickets WHERE {where_clause};"
    
    return sql_query

def execute_query(sql_query, db_path="tickets.db"):
    """
    Executes the given SQL query on the database and returns the results.
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(sql_query)
        results = cursor.fetchall()
        conn.close()
        return results
    except Exception as e:
        print("Database query execution failed:", str(e))
        return []

# Example usage
if __name__ == "__main__":
    extracted_info = {
        "priority": "high",
        "assignee": "John",
        "time_range": "last week"
    }

    sql_query = generate_sql_filter(extracted_info)
    print("Generated SQL Query:", sql_query)
    results = execute_query(sql_query)
    print("Query Results:", results)