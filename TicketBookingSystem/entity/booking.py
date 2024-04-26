class Booking:
    def __init__(self, event):
        self.event = event
        self.num_tickets = 0
        self.total_cost = 0

    def calculate_booking_cost(self, num_tickets):
        self.num_tickets = num_tickets
        self.total_cost = self.num_tickets * self.event.get_ticket_price()

    def book_tickets(self, num_tickets):
        if self.event.book_tickets(num_tickets):
            self.num_tickets += num_tickets
            self.total_cost += num_tickets * self.event.get_ticket_price()
            print(f"{num_tickets} tickets booked successfully!")
            return True
        else:
            print("Failed to book tickets.")
            return False

    def cancel_booking(self, num_tickets):
        if self.event.cancel_booking(num_tickets):
            self.num_tickets -= num_tickets
            self.total_cost -= num_tickets * self.event.get_ticket_price()
            print(f"{num_tickets} tickets canceled successfully!")
            return True
        else:
            print("Failed to cancel booking.")
            return False

    def get_available_no_of_tickets(self):
        return self.event.get_available_seats()

    def get_event_details(self):
        return self.event.display_event_details()
