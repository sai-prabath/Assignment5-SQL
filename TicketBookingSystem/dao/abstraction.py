from abc import ABC, abstractmethod

# Abstract
class Event(ABC):
    def __init__(self, event_name, event_date, event_time, venue_name, total_seats, ticket_price, event_type):
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.venue_name = venue_name
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.ticket_price = ticket_price
        self.event_type = event_type

    @abstractmethod
    def display_event_details(self):
        pass

    @abstractmethod
    def calculate_total_revenue(self, num_tickets):
        pass

    @abstractmethod
    def book_tickets(self, num_tickets):
        pass

    @abstractmethod
    def cancel_booking(self, num_tickets):
        pass


class BookingSystem(ABC):
    events = []

    @abstractmethod
    def create_event(self, event_name, event_date, event_time, total_seats, ticket_price, event_type, venue_name):
        pass

    @abstractmethod
    def book_tickets(self, event, num_tickets):
        pass

    @abstractmethod
    def cancel_tickets(self, event, num_tickets):
        pass

    @abstractmethod
    def get_available_seats(self, event):
        pass

# Concrete

class Movie(Event):
    def __init__(self, event_name, event_date, event_time, venue_name, total_seats, ticket_price, genre, actor_name, actress_name):
        super().__init__(event_name, event_date, event_time, venue_name, total_seats, ticket_price, event_type="Movie")
        self.genre = genre
        self.actor_name = actor_name
        self.actress_name = actress_name

    def display_event_details(self):
        print(f"Event Name: {self.event_name}")
        print(f"Event Date: {self.event_date}")
        print(f"Event Time: {self.event_time}")
        print(f"Venue: {self.venue_name}")
        print(f"Total Seats: {self.total_seats}")
        print(f"Available Seats: {self.available_seats}")
        print(f"Ticket Price: {self.ticket_price}")
        print(f"Event Type: {self.event_type}")
        print(f"Genre: {self.genre}")
        print(f"Actor: {self.actor_name}")
        print(f"Actress: {self.actress_name}")

    def calculate_total_revenue(self, num_tickets):
        return num_tickets * self.ticket_price

    def book_tickets(self, num_tickets):
        if self.available_seats >= num_tickets:
            self.available_seats -= num_tickets
            return True
        else:
            return False

    def cancel_booking(self, num_tickets):
        self.available_seats += num_tickets
        return True


class Concert(Event):
    def __init__(self, event_name, event_date, event_time, venue_name, total_seats, ticket_price, artist, concert_type):
        super().__init__(event_name, event_date, event_time, venue_name, total_seats, ticket_price, event_type="Concert")
        self.artist = artist
        self.concert_type = concert_type

    def display_event_details(self):
        print(f"Event Name: {self.event_name}")
        print(f"Event Date: {self.event_date}")
        print(f"Event Time: {self.event_time}")
        print(f"Venue: {self.venue_name}")
        print(f"Total Seats: {self.total_seats}")
        print(f"Available Seats: {self.available_seats}")
        print(f"Ticket Price: {self.ticket_price}")
        print(f"Event Type: {self.event_type}")
        print(f"Artist: {self.artist}")
        print(f"Concert Type: {self.concert_type}")

    def calculate_total_revenue(self, num_tickets):
        return num_tickets * self.ticket_price

    def book_tickets(self, num_tickets):
        if self.available_seats >= num_tickets:
            self.available_seats -= num_tickets
            return True
        else:
            return False

    def cancel_booking(self, num_tickets):
        self.available_seats += num_tickets
        return True


class Sport(Event):
    def __init__(self, event_name, event_date, event_time, venue_name, total_seats, ticket_price, sport_name, teams_name):
        super().__init__(event_name, event_date, event_time, venue_name, total_seats, ticket_price, event_type="Sports")
        self.sport_name = sport_name
        self.teams_name = teams_name

    def display_event_details(self):
        print(f"Event Name: {self.event_name}")
        print(f"Event Date: {self.event_date}")
        print(f"Event Time: {self.event_time}")
        print(f"Venue: {self.venue_name}")
        print(f"Total Seats: {self.total_seats}")
        print(f"Available Seats: {self.available_seats}")
        print(f"Ticket Price: {self.ticket_price}")
        print(f"Event Type: {self.event_type}")
        print(f"Sport: {self.sport_name}")
        print(f"Teams: {self.teams_name}")

    def calculate_total_revenue(self, num_tickets):
        return num_tickets * self.ticket_price

    def book_tickets(self, num_tickets):
        if self.available_seats >= num_tickets:
            self.available_seats -= num_tickets
            return True
        else:
            return False

    def cancel_booking(self, num_tickets):
        self.available_seats += num_tickets
        return True


class TicketBookingSystem(BookingSystem):
    def create_event(self, event_name, event_date, event_time, total_seats, ticket_price, event_type, venue_name):
        if event_type == "Movie":
            genre = input("Enter genre: ")
            actor_name = input("Enter actor name: ")
            actress_name = input("Enter actress name: ")
            event = Movie(event_name, event_date, event_time, venue_name, total_seats, ticket_price, genre, actor_name, actress_name)
        elif event_type == "Concert":
            artist = input("Enter artist name: ")
            concert_type = input("Enter concert type: ")
            event = Concert(event_name, event_date, event_time, venue_name, total_seats, ticket_price, artist, concert_type)
        elif event_type == "Sports":
            sport_name = input("Enter sport name: ")
            teams_name = input("Enter teams playing: ")
            event = Sport(event_name, event_date, event_time, venue_name, total_seats, ticket_price, sport_name, teams_name)
        else:
            print("Invalid event type!")
            return None

        self.events.append(event)
        return event

    def book_tickets(self, event, num_tickets):
        if event.book_tickets(num_tickets):
            print(f"{num_tickets} tickets booked successfully!")
            return event.calculate_total_revenue(num_tickets)
        else:
            print("Failed to book tickets.")
            return 0

    def cancel_tickets(self, event, num_tickets):
        if event.cancel_booking(num_tickets):
            print(f"{num_tickets} tickets canceled successfully!")
            return True
        else:
            print("Failed to cancel tickets.")
            return False

    def get_available_seats(self, event):
        return event.available_seats
