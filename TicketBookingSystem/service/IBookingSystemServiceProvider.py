from abc import ABC, abstractmethod
import IEventServiceProvider

class IBookingSystemServiceProvider(IEventServiceProvider):
    @abstractmethod
    def calculate_booking_cost(self, num_tickets: int):
        pass

    @abstractmethod
    def book_tickets(self, event_name: str, num_tickets: int, customers: list):
        pass

    @abstractmethod
    def cancel_booking(self, booking_id: int):
        pass

    @abstractmethod
    def get_booking_details(self, booking_id: int):
        pass
