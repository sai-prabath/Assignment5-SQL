from TicketBookingSystem.service.IBookingSystemServiceProvider import IBookingSystemServiceProvider
import EventServiceProviderImpl

class BookingSystemServiceProviderImpl(EventServiceProviderImpl, IBookingSystemServiceProvider):
    def __init__(self):
        super().__init__()

    def calculate_booking_cost(self, event, num_tickets):
        return event.get_ticket_price() * num_tickets

    def book_tickets(self, event, num_tickets):
        if event.book_tickets(num_tickets):
            print(f"{num_tickets} tickets booked successfully!")
            return event.calculate_total_revenue(num_tickets)
        else:
            print("Failed to book tickets.")
            return 0

    def cancel_booking(self, event, num_tickets):
        if event.cancel_booking(num_tickets):
            print(f"{num_tickets} tickets canceled successfully!")
            return True
        else:
            print("Failed to cancel tickets.")
            return False

    def get_booking_details(self, booking):
        booking.display_booking_details()
