-- TicketBookingSystem database

CREATE DATABASE IF NOT EXISTS TicketBookingSystem;

-- Venue Table
CREATE TABLE IF NOT EXISTS Venue (
    venue_id INT PRIMARY KEY,
    venue_name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL
);

-- Event Table
CREATE TABLE IF NOT EXISTS Event (
    event_id INT PRIMARY KEY,
    event_name VARCHAR(255) NOT NULL,
    event_date DATE NOT NULL,
    event_time TIME NOT NULL,
    venue_id INT,
    total_seats INT NOT NULL,
    available_seats INT NOT NULL,
    ticket_price DECIMAL(10, 2) NOT NULL,
    event_type ENUM('Movie', 'Sports', 'Concert') NOT NULL,
    booking_id INT
);

-- Customer Table
CREATE TABLE IF NOT EXISTS Customer (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    booking_id INT
);

-- Booking Table
CREATE TABLE IF NOT EXISTS Booking (
    booking_id INT PRIMARY KEY,
    customer_id INT,
    event_id INT,
    num_tickets INT NOT NULL,
    total_cost DECIMAL(10, 2) NOT NULL,
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- foreign keys

ALTER TABLE Event ADD FOREIGN KEY (venue_id) REFERENCES Venue(venue_id);

ALTER TABLE Event ADD FOREIGN KEY (booking_id) REFERENCES Booking(booking_id);

ALTER TABLE Customer ADD FOREIGN KEY (booking_id) REFERENCES Booking(booking_id);

ALTER TABLE Booking ADD FOREIGN KEY (customer_id) REFERENCES Customer(customer_id);

ALTER TABLE Booking ADD FOREIGN KEY (event_id) REFERENCES Event(event_id);

-- Inserting records into the Venue table

INSERT INTO Venue (venue_id, venue_name, address) VALUES
(1, 'Venue 1', 'Address 1'),
(2, 'Venue 2', 'Address 2'),
(3, 'Venue 3', 'Address 3'),
(4, 'Venue 4', 'Address 4'),
(5, 'Venue 5', 'Address 5'),
(6, 'Venue 6', 'Address 6'),
(7, 'Venue 7', 'Address 7'),
(8, 'Venue 8', 'Address 8'),
(9, 'Venue 9', 'Address 9'),
(10, 'Venue 10', 'Address 10');

-- Inserting sample records into the Event table
INSERT INTO Event (event_id, event_name, event_date, event_time, venue_id, total_seats, available_seats, ticket_price, event_type, booking_id) VALUES
(1, 'Event 1', '2024-04-10', '12:00:00', 1, 200, 200, 1500.00, 'Concert', NULL),
(2, 'Event 2', '2024-04-11', '14:00:00', 2, 150, 100, 2000.00, 'Movie', NULL),
(3, 'Event 3', '2024-04-12', '15:00:00', 3, 300, 250, 1800.00, 'Sports', NULL),
(4, 'Event 4', '2024-04-13', '18:00:00', 4, 250, 150, 2200.00, 'Concert', NULL),
(5, 'Event 5', '2024-04-14', '20:00:00', 5, 400, 350, 1200.00, 'Concert', NULL),
(6, 'Event 6', '2024-04-15', '19:00:00', 6, 350, 300, 1600.00, 'Sports', NULL),
(7, 'Event 7', '2024-04-16', '17:00:00', 7, 200, 100, 2500.00, 'Movie', NULL),
(8, 'Event 8', '2024-04-17', '16:00:00', 8, 300, 200, 1700.00, 'Concert', NULL),
(9, 'Event 9', '2024-04-18', '21:00:00', 9, 500, 450, 1900.00, 'Sports', NULL),
(10, 'Event 10', '2024-04-19', '13:00:00', 10, 450, 400, 2100.00, 'Movie', NULL);

-- Inserting sample records into the Customer table
INSERT INTO Customer (customer_id, customer_name, email, phone_number, booking_id) VALUES
(1, 'John Doe', 'john@example.com', '1234567890', NULL),
(2, 'Jane Smith', 'jane@example.com', '9876543210', NULL),
(3, 'Alice Johnson', 'alice@example.com', '4567890123', NULL),
(4, 'Bob Brown', 'bob@example.com', '3216549870', NULL),
(5, 'Charlie Davis', 'charlie@example.com', '7891234560', NULL),
(6, 'Emma Wilson', 'emma@example.com', '6549873210', NULL),
(7, 'David Lee', 'david@example.com', '1472583690', NULL),
(8, 'Olivia Clark', 'olivia@example.com', '2583691470', NULL),
(9, 'James Miller', 'james@example.com', '3698521470', NULL),
(10, 'Sophia Martinez', 'sophia@example.com', '8527419630', NULL);

-- Inserting sample records into the Booking table
INSERT INTO Booking (booking_id, customer_id, event_id, num_tickets, total_cost, booking_date) VALUES
(1, 1, 1, 2, 3000.00, '2024-04-03 09:30:00'),
(2, 2, 2, 3, 6000.00, '2024-04-02 10:45:00'),
(3, 3, 3, 1, 1800.00, '2024-04-01 11:20:00'),
(4, 4, 4, 4, 8800.00, '2024-03-05 12:15:00'),
(5, 5, 5, 2, 2400.00, '2024-04-02 13:00:00'),
(6, 6, 6, 3, 4800.00, '2024-04-06 14:30:00'),
(7, 7, 7, 1, 2500.00, '2024-04-07 15:10:00'),
(8, 8, 8, 2, 3400.00, '2024-04-07 16:00:00'),
(9, 9, 9, 4, 7600.00, '2024-04-02 17:45:00'),
(10, 10, 10, 3, 6300.00, '2024-03-01 18:20:00');

-- queries

SELECT * FROM Event;
SELECT * FROM Event WHERE available_seats > 0;
SELECT * FROM Event WHERE event_name LIKE '%cup%';
SELECT * FROM Event WHERE ticket_price BETWEEN 1000 AND 2500;
SELECT * FROM Event WHERE ticket_price BETWEEN 1000 AND 2500;
SELECT * FROM Event WHERE event_date BETWEEN '2024-04-10' AND '2024-04-15';
SELECT * FROM Event WHERE available_seats > 0 AND event_name LIKE '%Concert%'; SELECT * FROM Event WHERE available_seats > 0 AND event_type = 'Concert';
SELECT * FROM Customer LIMIT 5 OFFSET 5;
SELECT * FROM Booking WHERE num_tickets > 4;
SELECT * FROM Customer WHERE phone_number LIKE '%000';
SELECT * FROM Event WHERE total_seats > 15000;
SELECT * FROM Event WHERE event_name NOT LIKE 'x%' AND event_name NOT LIKE 'y%' AND event_name NOT LIKE 'z%'; 


