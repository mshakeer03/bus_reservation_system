from file_handler import open_bus_file, is_preffered_seat_available
from config import BUS_INFO

# Make Reservation Logic
def make_reservation(bus_no, date):
    filename = open_bus_file(bus_no, date)

    seat_no = int(input("Enter preferred seat number (1-40): "))
    while seat_no < 1 or seat_no > 40 or not is_preffered_seat_available(bus_no, date, seat_no):
        print("Invalid seat number or seat already taken. Please try again.")
        seat_no = int(input("Enter preferred seat number (1-40): "))

    name = input("Enter passenger name: ")
    gender = input("Enter gender (M/F): ").upper()
    while gender not in ['M', 'F']:
        print("Invalid gender. Please enter M or F.")
        gender = input("Enter gender (M/F): ").upper()

    age = int(input("Enter passenger age: "))
    fare = BUS_INFO[bus_no]['fare']

    with open(filename, 'a') as f:
        f.write(f"{seat_no}\t{name}\t{gender}\t{age}\t{BUS_INFO[bus_no]['depart']}\t{BUS_INFO[bus_no]['arrive']}\t{fare}\n")

    print(f"Reservation successful! Your seat number is {seat_no}.")
    print_reservation_ticket(bus_no, date, seat_no, name, gender, age, BUS_INFO[bus_no]['depart'], BUS_INFO[bus_no]['arrive'], fare)

# Query Reservation Logic
def query_reservation(bus_no, date):
    filename = open_bus_file(bus_no, date)

    with open(filename, 'r') as f:
        lines = f.readlines()[1:]  # Skip the header
        for line in lines:
            print(line.strip())

# Print Ticket
def print_reservation_ticket(bus_no, date, seat_no, name, gender, age, depart_time, arrive_time, fare):
    print("\nReservation Ticket")
    print(f"Bus No: {bus_no}\tDate of Journey: {date}")
    print(f"{seat_no}\t{name}\t{gender}\t{age}\tDepart: {depart_time}\tArrive: {arrive_time}\tFare: {fare}")
