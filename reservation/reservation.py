from reservation.db_handler import insert_reservation, query_reservations_sp_sd, is_seat_available
from config import BUS_INFO
from datetime import datetime

# Make Reservation Logic
def make_reservation(bus_no, date, route, fare, depart_time, arrival_time):
    seat_no = int(input("Enter preferred seat number (1-40): "))
    while seat_no < 1 or seat_no > 40:
        print("Invalid seat number, choose seat number between 1 and 40!")
        seat_no = int(input("Enter preferred seat number (1-40): "))
    while not is_seat_available(bus_no, date, seat_no):
        print(f"Seat {seat_no} already taken. Please choose a different seat.")
        seat_no = int(input("Enter preferred seat number (1-40): "))
    while is_reservation_full(bus_no, date):
        print(f"Bus {bus_no} on {date} is full. Please choose a different date.")
        date = input("Enter date of journey (e.g., 16-Jan-2024): ")
    name = input("Enter passenger name: ")
    gender = input("Enter gender (M/F): ").upper()
    while gender not in ['M', 'F']:
        print("Invalid gender. Please enter M or F.")
        gender = input("Enter gender (M/F): ").upper()

    age = int(input("Enter passenger age: "))

    # Insert reservation into MySQL database
    insert_reservation(bus_no, seat_no, name, gender, age, date, fare)

    print("-" * 50)
    print(f"Reservation successful! Your seat number is {seat_no}.")
    print_reservation_ticket(bus_no, date, seat_no, name, gender, age, depart_time, arrival_time, route, fare)

# Query Reservation Logic
def query_reservations(bus_no, date):
    print(f"\nBus No: {bus_no}\tDate of Journey: {date}")
    print(f"Route: {BUS_INFO[bus_no]['route']}")
    print("-" * 50)
    print("Seat No\tName\tAge\tGender\tFare")
    print("-" * 50)

    reservations = query_reservations_sp_sd(bus_no, date)

    for res in reservations:
        seat_no, name, gender, age, fare = res
        print(f"{seat_no}\t{name}\t{age}\t{gender}\t{fare}")

    print("-" * 50)
    print(f"Total Reservations: {len(reservations)}")
    print

# Is reservation full
def is_reservation_full(bus_no, date):
    reservations = query_reservations_sp_sd(bus_no, date)
    return len(reservations) == 40

# Print Ticket
def print_reservation_ticket(bus_no, date, seat_no, name, gender, age, depart_time, arrive_time, route, fare):
    print("\nReservation Ticket")
    print(f"Bus No: {bus_no}\tRoute: {route}\tDate of Journey: {date}\n")
    print(f"Seat\tName\tGender\tAge\tDeparture Time\tArrival Time\tFare")
    print(f"{seat_no}\t{name}\t{gender}\t{age}\t{depart_time}\t\t{arrive_time}\t\t{fare}")
    print("-" * 50)
