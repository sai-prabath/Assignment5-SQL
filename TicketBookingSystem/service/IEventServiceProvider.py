from abc import ABC, abstractmethod

class IEventServiceProvider(ABC):
    @abstractmethod
    def create_event(self, event_name, event_date, event_time, venue_name, total_seats, ticket_price, event_type):
        pass

    @abstractmethod
    def get_event_details(self, event):
        pass

    @abstractmethod
    def get_available_no_of_tickets(self, event):
        pass
