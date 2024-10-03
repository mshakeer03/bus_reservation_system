CREATE DATABASE IF NOT EXISTS bus_reservation_system;

USE bus_reservation_system;

-- Table for buses
CREATE TABLE buses (
    bus_no INT PRIMARY KEY,
    route VARCHAR(100),
    fare INT,
    depart_time TIME,
    arrive_time TIME
);

-- Table for reservations
CREATE TABLE reservations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    bus_no INT,
    seat_no INT,
    name VARCHAR(100),
    gender CHAR(1),
    age INT,
    reservation_date DATE,
    fare INT,
    FOREIGN KEY (bus_no) REFERENCES buses(bus_no)
);

-- Insert bus data
INSERT INTO buses (bus_no, route, fare, depart_time, arrive_time)
VALUES
    (1, 'DEL to JAI', 600, '08:30:00', '13:30:00'),
    (2, 'DEL to NAI', 700, '09:00:00', '15:15:00'),
    (3, 'DEL to CHA', 500, '08:30:00', '12:00:00');
