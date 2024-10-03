from reservation.db_handler import insert_reservation, query_reservations, is_seat_available
from config import BUS_INFO
from datetime import datetime

# Make Reservation Logic
def make_reservation(bus_no, date):
    seat_no = int(input("Enter preferred seat number (1-40): "))
    while seat_no < 1 or seat_no > 40 or not is_seat_available(bus_no, date, seat_no):
        print("Invalid seat number or seat already taken. Please try again.")
        seat_no = int(input("Enter preferred seat number (1-40): "))

    name = input("Enter passenger name: ")
    gender = input("Enter gender (M/F): ").upper()
    while gender not in ['M', 'F']:
        print("Invalid gender. Please enter M or F.")
        gender = input("Enter gender (M/F): ").upper()

    age = int(input("Enter passenger age: "))
    fare = BUS_INFO[bus_no]['fare']

    # Insert reservation into MySQL database
    insert_reservation(bus_no, seat_no, name, gender, age, date, fare)

    print(f"Reservation successful! Your seat number is {seat_no}.")
    print_reservation_ticket(bus_no, date, seat_no, name, gender, age, BUS_INFO[bus_no]['depart'], BUS_INFO[bus_no]['arrive'], fare)

# Query Reservation Logic
def query_reservations(bus_no, date):
    print(f"\nBus No: {bus_no}\tDate of Journey: {date}")
    print(f"Route: {BUS_INFO[bus_no]['route']}")
    print("-" * 50)
    print("Sno\tName\tAge\tGender\tFare")
    print("-" * 50)

    reservations = query_reservations(bus_no, date)

    for res in reservations:
        seat_no, name, gender, age, fare = res
        print(f"{seat_no}\t{name}\t{age}\t{gender}\t{fare}")

    print("-" * 50)
    print(f"Total Reservations: {len(reservations)}")

# Print Ticket
def print_reservation_ticket(bus_no, date, seat_no, name, gender, age, depart_time, arrive_time, fare):
    print("\nReservation Ticket")
    print(f"Bus No: {bus_no}\tDate of Journey: {date}")
    print(f"{seat_no}\t{name}\t{gender}\t{age}\tDepart: {depart_time}\tArrive: {arrive_time}\tFare: {fare}")
