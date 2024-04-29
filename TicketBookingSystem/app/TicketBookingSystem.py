
from TicketBookingSystem.bean.BookingSystemRepositoryImpl import BookingSystemRepositoryImpl
from TicketBookingSystem.entity.customer import Customer
from TicketBookingSystem.exception.exceptions import EventNotFoundException
from TicketBookingSystem.exception.exceptions import InvalidBookingIDException

class TicketBookingSystem:
    def __init__(self, db_conn):
        self.booking_system_repository = BookingSystemRepositoryImpl(db_conn)

    def display_menu(self):
        print("===== Ticket Booking System =====")
        print("1. Create Event")
        print("2. View Event Details")
        print("3. Book Tickets")
        print("4. Cancel Booking")
        print("5. View Available Seats")
        print("6. Exit")

    def create_event(self):
        event_name = input("Enter event name: ")
        event_date = input("Enter event date (YYYY-MM-DD): ")
        event_time = input("Enter event time (HH:MM:SS): ")
        venue_name = input("Enter venue name: ")
        total_seats = int(input("Enter total seats: "))
        ticket_price = float(input("Enter ticket price: "))
        event_type = input("Enter event type (Movie/Sports/Concert): ")
        self.booking_system_repository.create_event(event_name, event_date, event_time, venue_name, total_seats, ticket_price, event_type)

    def view_event_details(self):
        event_details = self.booking_system_repository.getEventDetails()
        if event_details:
            for event in event_details:
                print(event)
        else:
            print("no events found")

    def book_tickets(self):
        self.view_event_details()
        event_id = int(input("Enter event ID to book tickets: "))
        try:
            event = self.booking_system_repository.events[event_id]
        except Exception as e:
            raise EventNotFoundException(f"event id not found : {e}")

        num_tickets = int(input("Enter number of tickets to book: "))

        # Create customer
        customer_name = input("Enter customer name: ")
        email = input("Enter email: ")
        phone_number = input("Enter phone number: ")
        customer = Customer(customer_name, email, phone_number)

        # Book tickets
        self.booking_system_repository.book_tickets(event, num_tickets, customer)

    def cancel_booking(self):
        booking_id = int(input("Enter booking ID to cancel: "))
        self.booking_system_repository.cancel_booking(booking_id)

    def view_available_seats(self):
        available_seats = self.booking_system_repository.getAvailableNoOfTickets()
        print(f"Total available seats: {available_seats}")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.create_event()
            elif choice == "2":
                self.view_event_details()
            elif choice == "3":
                self.book_tickets()
            elif choice == "4":
                self.cancel_booking()
            elif choice == "5":
                self.view_available_seats()
            elif choice == "6":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a valid option.")



