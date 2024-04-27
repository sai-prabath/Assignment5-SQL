from datetime import datetime
class Booking:
    booking_id_counter = 0

    def __init__(self, event, num_tickets, customers):
        Booking.booking_id_counter += 1
        self.booking_id = Booking.booking_id_counter
        self.event = event
        self.num_tickets = num_tickets
        self.customers = customers
        self.total_cost = event.ticket_price * num_tickets
        self.booking_date = datetime.now()

    def display_booking_details(self):
        print(f"Booking ID: {self.booking_id}")
        print("Event Details:")
        self.event.display_event_details()
        print(f"Number of Tickets: {self.num_tickets}")
        print(f"Total Cost: {self.total_cost}")
        print(f"Booking Date: {self.booking_date}")
        self.customers.display_customer_details()
