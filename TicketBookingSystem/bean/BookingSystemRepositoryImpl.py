from TicketBookingSystem.entity.movie import Movie
from TicketBookingSystem.entity.concert import Concert
from TicketBookingSystem.entity.sports import Sports
from TicketBookingSystem.entity.booking import Booking
from TicketBookingSystem.service.IBookingSystemRepository import IBookingSystemRepository

class BookingSystemRepositoryImpl(IBookingSystemRepository):

    def __init__(self, db_conn):
        self.db_conn = db_conn
        self.events = {}
        self.bookings = {}

    def create_event(self, event_name, event_date, event_time, venue_name, total_seats, ticket_price, event_type):

        if event_type.lower() == "movie":
            genre = input("Enter movie genre: ")
            actor_name = input("Enter actor name: ")
            actress_name = input("Enter actress name: ")
            event = Movie(event_name, event_date, event_time, venue_name, total_seats, ticket_price, genre, actor_name, actress_name)
        elif event_type.lower() == "concert":
            artist = input("Enter artist name: ")
            concert_type = input("Enter concert type: ")
            event = Concert(event_name, event_date, event_time, venue_name, total_seats, ticket_price, artist, concert_type)
        elif event_type.lower() == "sports":
            sport_name = input("Enter sport name: ")
            teams_name = input("Enter teams name: ")
            event = Sports(event_name, event_date, event_time, venue_name, total_seats, ticket_price, sport_name, teams_name)
        else:
            print("Invalid event type.")
            return None

        try:
            cursor = self.db_conn.cursor()
            cursor.execute(
                "INSERT INTO Event (event_id, event_name, event_date, event_time, venue_name, total_seats, available_seats, ticket_price, event_type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (event.event_id, event_date, event_time, venue_name, total_seats, total_seats, ticket_price, event_type))
            self.db_conn.commit()
            self.events[event.event_id] = event
            return event
        except:
            print(f"Error creating event: {None}")

    def getEventDetails(self) :
        try:
            cursor = self.db_conn.cursor()
            cursor.execute("SELECT * FROM Event")
            events = cursor.fetchall()
            cursor.close()
            return events
        except:
            print(f"Error fetching event details: {None}")

    def getAvailableNoOfTickets(self) :
        try:
            cursor = self.db_conn.cursor()
            cursor.execute("SELECT SUM(available_seats) FROM Event")
            total_available_tickets = cursor.fetchone()[0]
            cursor.close()
            print(f"total available tickets ={total_available_tickets}")
            return total_available_tickets
        except:
            print(f"Error fetching available tickets: {None}")

    def calculate_booking_cost(self, num_tickets, ticket_price):
        return num_tickets * ticket_price

    def book_tickets(self, event, num_tickets, customer) :
        try:
            cursor = self.db_conn.cursor()
            cursor.execute("SELECT available_seats FROM Event WHERE event_name = %s", (event.event_id))
            available_seats = cursor.fetchone()[0]

            if available_seats >= num_tickets:
                cursor.execute("UPDATE Event SET available_seats = available_seats - %s WHERE event_id = %s",
                               (num_tickets, event.event_id))
                self.db_conn.commit()

                booking = Booking(event, num_tickets, customer)
                self.bookings[booking.booking_id] = booking

                cursor.execute(
                    "INSERT INTO Booking (booking_id, event_id, customer_id, num_tickets, total_cost, booking_date) VALUES (%s, %s, %s, %s, %s, %s)",
                    (booking.booking_id, event.event_id, customer.customer_id, num_tickets, booking.total_cost, booking.booking_date))
                self.db_conn.commit()

                cursor.close()
                print(f"{num_tickets} tickets booked successfully for {event.event_name}, booking id = {booking.booking_id}")
                return booking
            else:
                print("Not enough available seats for booking")
        except:
            ProcessLookupError(f"Error booking tickets: {None}")

    def cancel_booking(self, booking_id):
        try:
            cursor = self.db_conn.cursor()
            cursor.execute("SELECT event_id, num_tickets FROM Booking WHERE booking_id = %s", (booking_id,))
            booking_details = cursor.fetchone()

            if booking_details:
                event_id, num_tickets = booking_details
                cursor.execute("UPDATE Event SET available_seats = available_seats + %s WHERE event_id = %s",
                               (num_tickets, event_id))
                cursor.execute("DELETE FROM Booking WHERE booking_id = %s", (booking_id,))
                self.db_conn.commit()
                cursor.close()
            else:
                print("Booking ID not found")
        except:
            print(f"Error cancelling booking: {None}")

    def get_booking_details(self, booking_id):
        try:
            cursor = self.db_conn.cursor()
            cursor.execute("SELECT * FROM Booking WHERE booking_id = %s", (booking_id,))
            booking_details = cursor.fetchone()
            cursor.close()
            return booking_details
        except:
            print(f"Error fetching booking details: {None}")
