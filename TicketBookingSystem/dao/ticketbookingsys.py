from TicketBookingSystem.entity.movie import Movie
from TicketBookingSystem.entity.concert import Concert
from TicketBookingSystem.entity.sports import Sports

class TicketBookingSystem:
    events = []
    @classmethod
    def create_event(cls, event_name, event_date, event_time, venue_name, total_seats, ticket_price, event_type):
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
        cls.events.append(event)
        return event

    @classmethod
    def display_event_details(cls, event):
        event.display_event_details()

    @classmethod
    def book_tickets(cls, event, num_tickets):
        if event.book_tickets(num_tickets):
            print(f"{num_tickets} tickets booked successfully!")
            return event.calculate_total_revenue(num_tickets)
        else:
            print("Failed to book tickets.")
            return 0

    @classmethod
    def cancel_tickets(cls, event, num_tickets):
        if event.cancel_booking(num_tickets):
            print(f"{num_tickets} tickets canceled successfully!")
            return True
        else:
            print("Failed to cancel tickets.")
            return False

    @classmethod
    def main(cls):
        while True:
            print("\n1. Create Event\n2. Display Event Details\n3. Book Tickets\n4. Cancel Tickets\n5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                event_name = input("Enter event name: ")
                event_date = input("Enter event date: ")
                event_time = input("Enter event time: ")
                total_seats = int(input("Enter total seats: "))
                ticket_price = float(input("Enter ticket price: "))
                event_type = input("Enter event type (movie/concert/sports): ")
                venue_name = input("Enter venue name: ")
                cls.create_event(event_name, event_date, event_time, venue_name, total_seats, ticket_price, event_type)
            elif choice == "2":
                if cls.events:
                    for index, event in enumerate(cls.events, start=1):
                        print(f"\nEvent {index}:")
                        cls.display_event_details(event)
                else:
                    print("No events created yet.")
            elif choice == "3":
                if cls.events:
                    event_index = int(input("Enter event index to book tickets: ")) - 1
                    if 0 <= event_index < len(cls.events):
                        event = cls.events[event_index]
                        num_tickets = int(input("Enter number of tickets to book: "))
                        cls.book_tickets(event, num_tickets)
                    else:
                        print("Invalid event index.")
                else:
                    print("No events created yet.")
            elif choice == "4":
                if cls.events:
                    event_index = int(input("Enter event index to cancel tickets: ")) - 1
                    if 0 <= event_index < len(cls.events):
                        event = cls.events[event_index]
                        num_tickets = int(input("Enter number of tickets to cancel: "))
                        cls.cancel_tickets(event, num_tickets)
                    else:
                        print("Invalid event index.")
                else:
                    print("No events created yet.")
            elif choice == "5":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")


