import mysql.connector
from config import DATABASE_CONFIG

# Function to establish a database connection
def get_db_connection():
    conn = mysql.connector.connect(**DATABASE_CONFIG)
    return conn

# Insert reservation with ticket_number into MySQL database
def insert_reservation(bus_no, seat_no, name, gender, age, reservation_date, fare, ticket_number):
    connection = mysql.connector.connect(**DATABASE_CONFIG)
    cursor = connection.cursor()

    query = """
        INSERT INTO reservations (bus_no, seat_no, name, gender, age, reservation_date, fare, ticket_number)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (bus_no, seat_no, name, gender, age, reservation_date, fare, ticket_number))

    connection.commit()
    cursor.close()
    connection.close()

# Check if the generated ticket number is unique
def is_ticket_number_unique(ticket_number):
    connection = mysql.connector.connect(**DATABASE_CONFIG)
    cursor = connection.cursor()

    query = "SELECT COUNT(*) FROM reservations WHERE ticket_number = %s"
    cursor.execute(query, (ticket_number,))
    result = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return result == 0  # True if the ticket number is unique

# Function to query reservations for a specific bus on a specific date
def query_reservations_sp_sd(bus_no, reservation_date):
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
def is_preffered_seat_available(bus_no, reservation_date, seat_no):
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

# Function to check if the number of passengers exceeds the free seats available
def is_number_passengers_exceeds_free_seats(bus_no, reservation_date, num_passengers):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        SELECT COUNT(*) FROM reservations
        WHERE bus_no = %s AND reservation_date = %s
    """
    cursor.execute(query, (bus_no, reservation_date))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result[0] + num_passengers > 40

# Function to cancel a reservation
def delete_reservation(bus_no, reservation_date, seat_no):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        DELETE FROM reservations
        WHERE bus_no = %s AND reservation_date = %s AND seat_no = %s
    """
    cursor.execute(query, (bus_no, reservation_date, seat_no))
    conn.commit()
    cursor.close()
    conn.close()
