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

This Python-based Online Bus Reservation System application is designed with modularity and scalability in mind, leveraging core Python features such as object-oriented programming, structured error handling, and database connectivity. The project is structured into multiple modules, each handling different responsibilities such as database interactions, user inputs, and business logic, ensuring separation of concerns and easy maintainability. The system supports features such as booking multiple passengers, ticket cancellation, and querying reservations.

### 1. Application Architecture:

The application follows a modular architecture where each module has a dedicated function. The main driver program (app.py) manages the overall user interface (CLI-based) and routes the user’s actions (e.g., reservation, query, cancellation) to the respective modules.

    **Reservation Module:** Handles all booking-related functionalities like seat selection, passenger details collection, and ticket generation.
    **Database Handler Module:** Manages interaction with the MySQL database to store and retrieve reservation details.
    **Utility Module:** Contains helper functions like ticket number generation and date validation.
This clear division of tasks makes the application more readable, maintainable, and testable.

### 2. Features of Python:

    **Object-Oriented Design:** The application uses classes and functions to encapsulate business logic, helping in better code organization and reuse.
    **Subprocess Handling:** The application supports parallel tasks, like database updates, without blocking the main workflow.
    **Exception Handling:** Structured error handling is used to deal with invalid inputs (e.g., invalid seat number, date, etc.).
    **File and Database Operations:** The system can dynamically read from and write to MySQL databases and generate logs or output tickets in text format.

### 3. Database Connectivity:

    **MySQL** is used as the backend to store reservations. A dedicated module (db_handler.py) handles database connections, queries, and data manipulations using the mysql-connector-python library.
    The **reservations table** contains fields such as bus number, seat number, passenger details (name, gender, age), date of reservation, and a unique ticket number, ensuring that all reservations are recorded and managed efficiently.
    Database connectivity is abstracted into utility functions to ensure all interactions with MySQL are consistent and efficient.

### 4. Libraries Used:

    **MySQL Connector (mysql-connector-python):** Handles all MySQL database operations, including insertions, deletions, and queries.
    **Datetime:** Used for date validation and management, ensuring users can only select valid future dates for reservations.
    **Random:** Generates unique ticket numbers for each reservation.
    **OS:** Manages file operations for log generation and storage.

### 5. Key Features:

	**Reservation for Multiple Passengers:** Users can book tickets for multiple passengers in a single transaction, and a consolidated ticket with all passengers' details is generated.
    **Cancellation:** The system allows users to cancel a reservation by specifying the bus number, seat number, and date of reservation.
    **Database Integrity:** MySQL constraints (e.g., unique ticket numbers) ensure data integrity and consistency in the database.
The entire system is designed to be extensible, meaning more features (such as seat preferences, dynamic pricing, etc.) can be added without disturbing the existing structure.

## Folder Structure
```
├── app.py                      # Main entry point for the reservation system
├── config.py                   # Configuration file for database and bus details
├── reservation                 # Reservation module
│   ├── __init__.py
│   ├── reservation.py          # Reservation logic and ticket generation
│   ├── db_handler.py           # Database handling and SQL queries
│   ├── validation.py           # Date validation and return in proper format
├── util                        # Utility functions
│   ├── utils.py                # Utility functions for ticket number generation, etc.
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

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
