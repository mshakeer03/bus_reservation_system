import os

# Function to create or open a reservation file for a bus on a given date
def open_bus_file(bus_no, date):
    filename = f"{date.replace('-', '')}B{str(bus_no).zfill(2)}.txt"
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write("Sno\tName\tGender\tAge\tDepartTime\tArrivTime\tFare\n")
    return filename

# Function to check seat availability
def is_preffered_seat_available(bus_no, date, seat_no):
    filename = open_bus_file(bus_no, date)
    with open(filename, 'r') as f:
        lines = f.readlines()[1:]
        taken_seats = [int(line.split('\t')[0]) for line in lines]
    return seat_no not in taken_seats
