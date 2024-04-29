from abc import ABC, abstractmethod
class IBookingSystemRepository(ABC):
    @abstractmethod
    def create_event(self, event_name, event_date, event_time, venue_name, total_seats, ticket_price, event_type):
        pass

    @abstractmethod
    def getEventDetails(self) :
        pass

    @abstractmethod
    def getAvailableNoOfTickets(self) :
        pass

    @abstractmethod
    def calculate_booking_cost(self, num_tickets, ticket_price):
        pass

    @abstractmethod
    def book_tickets(self, event, num_tickets, customer):
        pass

    @abstractmethod
    def cancel_booking(self, booking_id: int) :
        pass

    @abstractmethod
    def get_booking_details(self, booking_id: int) :
        pass

