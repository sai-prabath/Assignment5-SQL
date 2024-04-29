from abc import ABC, abstractmethod
import IEventServiceProvider

class IBookingSystemServiceProvider(IEventServiceProvider):
    @abstractmethod
    def calculate_booking_cost(self, event, num_tickets):
        pass

    @abstractmethod
    def book_tickets(self, event, num_tickets):
        pass

    @abstractmethod
    def cancel_booking(self, event, num_tickets):
        pass

    @abstractmethod
    def get_booking_details(self, booking):
        pass
