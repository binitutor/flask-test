import time
from postgres_db import PostgresDb

postgresdb = PostgresDb()
db = postgresdb.get_db()
def get_db():
    return db

def get_conn():
    count = 0
    while(1):
        try:
            return db.connect()
        except:
            count += 1
            if count > 10:
                print("Failed to get database connection!")
                raise ValueError("Failed to get database connection")
            time.sleep(count)