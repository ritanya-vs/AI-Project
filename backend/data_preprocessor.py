import sqlite3
import pandas as pd

def load_tickets(db_path="tickets_database.db"):
    """
    Loads ticket data from SQLite database.
    """
    conn = sqlite3.connect(db_path)
    query = "SELECT 'Ticket Subject', 'Ticket Description', 'Ticket Priority' FROM tickets"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def prepare_dataset(df):
    """
    Converts data into input-output pairs for fine-tuning BART.
    """
    dataset = []
    for _, row in df.iterrows():
        input_text = f"Subject: {row["'Ticket Subject'"]} | Description: {row["'Ticket Description'"]}"
        output_text = f"Priority: {row["'Ticket Priority'"]}"
        dataset.append({"input": input_text, "output": output_text})
    return dataset

if __name__ == "__main__":
    df = load_tickets()
    dataset = prepare_dataset(df)
    print(dataset[:5])  # Print first few samples
