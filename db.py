import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

try:
    
    conn = psycopg2.connect(
        host=os.getenv("db_host"),
        database=os.getenv("db_database"),
        user=os.getenv("db_user"),
        password=os.getenv("db_password")

        )

    print('connected to the database')


except:
    print("I am unable to connect to the database")

cur = conn.cursor()
# cur.execute("CREATE TABLE IF NOT EXISTS games (id SERIAL PRIMARY KEY, );")
# cur.execute("INSERT INTO mytable (ID) VALUES (1) ")
# conn.commit()



