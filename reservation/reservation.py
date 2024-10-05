import random
from reservation.db_handler import insert_reservation
from reservation.db_handler import query_reservations_sp_sd
from reservation.db_handler import is_preffered_seat_available
from reservation.db_handler import is_number_passengers_exceeds_free_seats
from reservation.db_handler import delete_reservation
from reservation.db_handler import is_ticket_number_unique
from config import BUS_INFO
from datetime import datetime

# Generate a unique 5-digit ticket number
def generate_unique_ticket_number():
    while True:
        ticket_number = random.randint(10000, 99999)  # Generate 5-digit number
        if is_ticket_number_unique(ticket_number):  # Check if the ticket number is unique
            return ticket_number

# Make Reservation Logic
def make_reservation(bus_no, date, num_passengers, route, fare, depart_time, arrival_time):
    reservations = []  # List to store reservation details for all passengers

    for i in range(num_passengers):
        print(f"\nBooking details for Passenger {i + 1}:")

        # Seat number input and validation
        seat_no = int(input("Enter preferred seat number (1-40): "))
        while is_reservation_full(bus_no, date):
            print(f"Bus {bus_no} on {date} is full. Please choose a different date.")
            date = input("Enter date of journey (e.g., 16-Jan-2024): ")
        while is_number_passengers_exceeds_free_seats(bus_no, date, num_passengers):
            print(f"Number of passengers exceeds the free seats available. Please try again.")
            num_passengers = int(input("Enter the number of passengers: "))
        while seat_no < 1 or seat_no > 40:
            print("Invalid seat number, choose seat number between 1 and 40!")
            seat_no = int(input("Enter preferred seat number (1-40): "))
        while not is_preffered_seat_available(bus_no, date, seat_no):
            print(f"Seat {seat_no} already taken. Please choose a different seat.")
            seat_no = int(input("Enter preferred seat number (1-40): "))

        # Collect passenger details
        name = input("Enter passenger name: ")
        gender = input("Enter gender (M/F): ").upper()
        while gender not in ['M', 'F']:
            print("Invalid gender. Please enter M or F.")
            gender = input("Enter gender (M/F): ").upper()

        age = int(input("Enter passenger age: "))

        # Generate a unique ticket number for this reservation
        ticket_number = generate_unique_ticket_number()

        # Insert reservation into MySQL database, including the ticket_number
        insert_reservation(bus_no, seat_no, name, gender, age, date, fare, ticket_number)

        # Add reservation to the list
        reservations.append({
            'ticket_number': ticket_number,  # Add the ticket number to the reservation
            'seat_no': seat_no,
            'name': name,
            'gender': gender,
            'age': age,
            'fare': fare
        })

        print("-" * 80)
        print(f"Reservation successful for Passenger {i + 1}! Seat number is {seat_no}.")

    # Print the ticket for all passengers after the loop finishes
    print_reservation_ticket(ticket_number, bus_no, date, reservations, depart_time, arrival_time, route)

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

# Reservation Cancellation Logic
def cancel_reservation(bus_no, date, seat_no):
    print("-" * 80)
    print(f"Canceling reservation for seat {seat_no} on Bus {bus_no} on {date}.")
    delete_reservation(bus_no, date, seat_no)
    print(f"Reservation canceled successfully!")
    print("-" * 80)

# Print Ticket (Modified to handle multiple passengers)
def print_reservation_ticket(ticket_number, bus_no, date, reservations, depart_time, arrive_time, route):
    print("-" * 80)
    print(f"\nReservation Ticket:")
    print(f"Bus No: {bus_no}\tRoute: {route}\tDate of Journey: {date}\n")
    print(f"Seat\tName\tGender\tAge\tDeparture Time\tArrival Time\tFare\tTicket No")
    print("-" * 80)

    total_fare = 0

    for reservation in reservations:
        ticket_number = reservation['ticket_number']
        seat_no = reservation['seat_no']
        name = reservation['name']
        gender = reservation['gender']
        age = reservation['age']
        fare = reservation['fare']
        total_fare += fare

        print(f"{seat_no}\t{name}\t{gender}\t{age}\t{depart_time}\t\t{arrive_time}\t\t{fare}\t{ticket_number}")

    print("-" * 80)
    print(f"Total Amount: {total_fare:.2f}")
    print("-" * 80)
