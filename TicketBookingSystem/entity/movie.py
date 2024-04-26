from TicketBookingSystem.entity.event import Event

class Movie (Event):
    def __init__(self, event_name, event_date, event_time, venue_name, total_seats, ticket_price, genre, actor_name, actress_name):
        super().__init__(event_name, event_date, event_time, venue_name, total_seats, ticket_price, "Movie")
        self.genre = genre
        self.actor_name = actor_name
        self.actress_name = actress_name

    def display_event_details(self):
        super().display_event_details()
        print(f"Genre: {self.genre}")
        print(f"Actor Name: {self.actor_name}")
        print(f"Actress Name: {self.actress_name}")
