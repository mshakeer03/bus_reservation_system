# Online Bus Reservation System

This project is a command-line-based **Online Bus Reservation System** where users can make bus reservations, query their reservations, and manage bookings. The system allows multiple passengers to be booked at once and generates a reservation ticket for each booking. It stores all the booking information in a MySQL database.

## Features
- **Bus Routes**: Displays available bus routes.
- **Make Reservations**: Allows users to reserve seats for one or multiple passengers.
- **Query Reservations**: Users can query existing reservations based on the bus number and journey date.
- **Ticket Generation**: Generates a reservation ticket containing passenger details, seat number, departure time, and fare.
- **Database Integration**: Stores reservation information in a MySQL database.
- **Unique Ticket Number**: Generates a unique 5-digit ticket number for each reservation.
- **Seat Availability**: Checks seat availability before making a reservation.
- **Cancel Reservation**: Allows users to cancel a reservation by providing the ticket number.
- **Fare Calculation**: Calculates the fare based on the passenger's age and the bus route.
- **Data Validation**: Validates user inputs to ensure correct data entry.
- **Error Handling**: Provides error messages for invalid inputs and exceptions.

## Prerequisites
- Python 3.6 or higher
- MySQL 8.0 or higher
- Required Python packages: `mysql-connector-python`, `datetime`

### Python Packages
Install the required Python packages by running the following command:
```bash
pip install -r requirements.txt
```
## MySQL Database Setup
1. Install MySQL on your system and ensure it is running.
2. Log in to MySQL and create a database:
    CREATE DATABASE bus_reservation;
3. Create the necessary table for buses and reservations:
    CREATE TABLE buses (
        bus_no INT PRIMARY KEY,
        route VARCHAR(100),
        fare INT,
        departure_time TIME,
        arrival_time TIME,
    );
    CREATE TABLE reservations (
        id INT AUTO_INCREMENT PRIMARY KEY,
        bus_no INT,
        seat_no INT,
        name VARCHAR(100),
        gender CHAR(1),
        age INT,
        reservation_date DATE,
        fare INT,
        ticket_number INT UNIQUE,
        FOREIGN KEY (bus_no) REFERENCES buses(bus_no)
    );
4. Edit the config.py file to add your MySQL credentials:
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'your_mysql_username'
    MYSQL_PASSWORD = 'your_mysql_password'
    MYSQL_DATABASE = 'bus_reservation'

## Project Structure

├── app.py                      # Main entry point for the reservation system
├── config.py                   # Configuration file for database and bus details
├── reservation                 # Reservation module
│   ├── __init__.py
│   ├── reservation.py          # Reservation logic and ticket generation
│   ├── db_handler.py           # Database handling and SQL queries
├── util                        # Utility functions
│   ├── utils.py                # Utility functions for ticket number generation, etc.
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation

## Usage
1. Clone the repository to your local machine:
    git clone https://github.com/yourusername/bus_reservation_system.git
    cd bus_reservation_system
2. Set up a virtual environment (optional but recommended):
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install the required Python packages:
    pip install -r requirements.txt
4. Ensure that the MySQL database is set up correctly as described in the MySQL Database Setup section.

5. Run the program:
    python main.py
6. Follow the on-screen instructions to make reservations, query reservations, etc.
