from TicketBookingSystem.service.IEventServiceProvider import IEventServiceProvider
from TicketBookingSystem.entity.movie import Movie
from TicketBookingSystem.entity.concert import Concert
from TicketBookingSystem.entity.sports import Sports
from TicketBookingSystem.entity.event import Event

class EventServiceProviderImpl(IEventServiceProvider):
    def __init__(self):
        self.events = []

    def create_event(self, event_name, event_date, event_time, venue_name, total_seats, ticket_price, event_type ):
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
        self.events.append(event)
        return event

    def get_event_details(self, event):
        event.display_event_details()

    def get_available_no_of_tickets(self, event):
        return event.get_available_seats()
