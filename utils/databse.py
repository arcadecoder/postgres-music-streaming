import psycopg2
import pandas as pd

def run_query(query):
    """
    Connect to mysql database for IAS
    and execute query
    """
    try:
        conn = psycopg2.connect(
            host="127.0.0.1",
            user="arcade",
            dbname="test",
            port=5432
        )
        data = pd.read_sql_query(query, conn)
        conn.close()
        return data
    except Exception as e:
        print(f"Error, {e}")

df = run_query(""" SELECT relname FROM pg_class WHERE relkind='r'
                  AND relname !~ '^(pg_|sql_)'; 
                  """)

print(df)
