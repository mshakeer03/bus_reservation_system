import mysql.connector
from config import DATABASE_CONFIG

# Function to establish a database connection
def get_db_connection():
    conn = mysql.connector.connect(**DATABASE_CONFIG)
    return conn

# Function to insert a reservation into the MySQL database
def insert_reservation(bus_no, seat_no, name, gender, age, reservation_date, fare):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO reservations (bus_no, seat_no, name, gender, age, reservation_date, fare)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (bus_no, seat_no, name, gender, age, reservation_date, fare))
    conn.commit()
    cursor.close()
    conn.close()

# Function to query reservations for a specific bus on a specific date
def query_reservations(bus_no, reservation_date):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        SELECT seat_no, name, gender, age, fare FROM reservations
        WHERE bus_no = %s AND reservation_date = %s
    """
    cursor.execute(query, (bus_no, reservation_date))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

# Function to check if a seat is available
def is_seat_available(bus_no, reservation_date, seat_no):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        SELECT seat_no FROM reservations
        WHERE bus_no = %s AND reservation_date = %s AND seat_no = %s
    """
    cursor.execute(query, (bus_no, reservation_date, seat_no))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result is None
