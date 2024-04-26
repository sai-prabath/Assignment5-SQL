from TicketBookingSystem.entity.event import Event

class Sports(Event):
    def __init__(self, event_name, event_date, event_time, venue_name, total_seats, ticket_price, sport_name, teams_name):
        super().__init__(event_name, event_date, event_time, venue_name, total_seats, ticket_price, "Sports")
        self.sport_name = sport_name
        self.teams_name = teams_name

    def display_event_details(self):
        super().display_event_details()
        print(f"Sport Name: {self.sport_name}")
        print(f"Teams Name: {self.teams_name}")