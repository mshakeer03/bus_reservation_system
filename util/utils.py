import random
from reservation.db_handler import is_ticket_number_unique

# Generate a unique ticket number
def generate_unique_ticket_number():
    while True:
        ticket_number = random.randint(10000, 99999)  # Generate unique number
        if is_ticket_number_unique(ticket_number):  # Check if the ticket number is unique
            return ticket_number
