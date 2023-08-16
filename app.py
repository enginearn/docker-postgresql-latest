import psycopg

DB_NAME = "test"
USER = "postgres"
PASSWORD = "postgres"
HOST = "db"
PORT = "5432"

def database_exists(dbname, user, password, host, port):
    try:
        conn = psycopg.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        conn.close()
        return True
    except psycopg.OperationalError:
        return False

def create_database(dbname, user, password, host, port):
    conn = psycopg.connect(dbname="postgres", user=user, password=password, host=host, port=port)
    conn.autocommit = True # autocommit is required
    cur = conn.cursor()
    cur.execute(f"CREATE DATABASE {dbname};")
    conn.close()

if not database_exists(DB_NAME, USER, PASSWORD, HOST, PORT):
    create_database(DB_NAME, USER, PASSWORD, HOST, PORT)

with psycopg.connect(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST, port=PORT) as conn:
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS test (
                id serial PRIMARY KEY,
                num integer,
                data text)
            """)
        cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "ghi'jkl"))
        cur.execute("SELECT * FROM test")
        for record in cur:
            print(record)
