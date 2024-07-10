import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, request

# SQL QUERIES
CREATE_ROOMS_TABLE = (
    '''
    CREATE TABLE IF NOT EXISTS rooms (id SERIAL PRIMARY KEY, name TEXT);
    '''
)
CREATE_TEMPS_TABLE = (
    '''
    CREATE TABLE IF NOT EXISTS temperatures (room_id INTEGER, temperature REAL,
        date TIMESTAMP, FOREIGN KEY(room_id) REFERENCES rooms(id) ON DELETE CASCADE);
    '''
)
INSERT_ROOM_RETURN_ID = (
    '''
    INSERT INTO rooms (name) VALUES (%s) RETURNING id;
    '''
)
INSERT_ROOM_RETURN_ID = (
    '''
    INSERT INTO temperatures (room_id, temperature, date) VALUES (%s, %s, %s);
    '''
)

# output how many days worth of temperature data is collected.
GLOBAL_NUMBER_OF_DAYS = (
    '''
    SELECT COUNT(DISTINCT DATE(date)) AS days FROM temperatures;
    '''
)
GLOBAL_AVG = (
    '''
    SELECT AVG(temperature) AS average FROM temperatures;
    '''
)

# GET
GET_TEST_TABLE = (
    '''
    SELECT * FROM test;
    '''
)

# TEST
CREATE_TEST_TABLE = (
    '''
    CREATE TABLE IF NOT EXISTS test (id SERIAL PRIMARY KEY, name TEXT);
    '''
)
INSERT_TEST_TABLE = (
    '''
    INSERT INTO test (name) VALUES (%s);
    '''
)

app = Flask(__name__)
load_dotenv()
db_url = os.getenv('DB_URL')
conn = psycopg2.connect(db_url)


@app.get("/")
def home():
    return "Welcome to BiniTutor File Processor!" 

@app.post("/api/room")
def create_room():
    data = request.get_json()
    name = data['name']
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(CREATE_ROOMS_TABLE)
    #         cursor.execute(INSERT_ROOM_RETURN_ID, (name,))
    #         room_id = cursor.fetchone()[0]
    # return {"id": room_id, "message": f"Room {name} created."}, 201
    return {"message": f"Room {name} created."}, 201


@app.post("/api/test")
def create_test():
    data = request.get_json()
    name = data['name']
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(CREATE_TEST_TABLE)
            cursor.execute(INSERT_TEST_TABLE, (name,))
    return {"message": "test table created."}, 201

@app.get("/api/test")
def get_rooms():
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(GET_TEST_TABLE)
            rooms = cursor.fetchall()
    return rooms, 201
