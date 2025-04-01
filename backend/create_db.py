import sqlite3
import pandas as pd

def insert_csv_to_sqlite(csv_file, db_file, table_name):
    try:
        df = pd.read_csv(csv_file)

        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        column_definitions = []
        for column, dtype in df.dtypes.items():
            if pd.api.types.is_integer_dtype(dtype):
                sql_type = "INTEGER"
            elif pd.api.types.is_float_dtype(dtype):
                sql_type = "REAL"
            elif pd.api.types.is_datetime64_any_dtype(dtype):
                sql_type = "TEXT"
            else:
                sql_type = "TEXT"
            column_definitions.append(f"\"{column}\" {sql_type}")

        create_table_sql = f"CREATE TABLE IF NOT EXISTS \"{table_name}\" ({', '.join(column_definitions)})"

        cursor.execute(create_table_sql)

        df.to_sql(table_name, conn, if_exists='append', index=False)

        conn.commit()
        conn.close()

        print(f"Data from '{csv_file}' inserted into '{table_name}' in '{db_file}' successfully.")

    except FileNotFoundError:
        print(f"Error: CSV file '{csv_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

csv_file_path = "customer_support_tickets.csv"
db_file_path = "tickets_database.db"
table_name = "tickets"

insert_csv_to_sqlite(csv_file_path, db_file_path, table_name)

try:
    conn = sqlite3.connect(db_file_path)
    df_from_db = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    print(df_from_db.head())
    conn.close()
except Exception as e:
    print(f"Error reading from the database: {e}")
