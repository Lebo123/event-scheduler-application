import datetime

class Event:
    def __init__(self, title, date_time, description=""):
        self.title = title
        self.date_time = date_time
        self.description = description

def display_menu():
    print("\nEvent Scheduler Menu:")
    print("1. Add Event")
    print("2. View Events")
    print("3. Search Events")
    print("4. Edit Event")
    print("5. Delete Event")
    print("6. Exit")

def add_event(events):
    title = input("Enter event title: ")
    description = input("Enter event description (optional): ")
    date_str = input("Enter event date and time (YYYY-MM-DD HH:MM): ")

    try:
        date_time = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M')
        event = Event(title, date_time, description)
        events.append(event)
        print("Event added successfully.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD HH:MM.")

def view_events(events):
    if not events:
        print("No events found.")
        return

    print("\nList of Events:")
    for index, event in enumerate(events, 1):
        print(f"{index}. {event.title} - {event.date_time.strftime('%Y-%m-%d %H:%M')}")
        if event.description:
            print(f"   Description: {event.description}")

def search_events(events):
    if not events:
        print("No events found.")
        return

    search_query = input("Enter search keyword or date (YYYY-MM-DD): ").lower()

    matching_events = []
    for event in events:
        if (
            search_query in event.title.lower() or
            search_query in event.description.lower() or
            (event.date_time.strftime('%Y-%m-%d') == search_query)
        ):
            matching_events.append(event)

    if matching_events:
        print("\nMatching Events:")
        view_events(matching_events)
    else:
        print("No matching events found.")

def edit_event(events):
    view_events(events)

    if not events:
        return

    try:
        index = int(input("Enter the number of the event to edit: ")) - 1
        if 0 <= index < len(events):
            edited_event = events[index]
            print(f"Editing Event: {edited_event.title}")

            edited_event.title = input("Enter new event title (press Enter to keep the current title): ") or edited_event.title
            edited_event.description = input("Enter new event description (press Enter to keep the current description): ") or edited_event.description
            date_str = input("Enter new event date and time (YYYY-MM-DD HH:MM) (press Enter to keep the current date and time): ") or edited_event.date_time.strftime('%Y-%m-%d %H:%M')

            try:
                edited_event.date_time = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M')
                print("Event edited successfully.")
            except ValueError:
                print("Invalid date format. Event date and time remain unchanged.")
        else:
            print("Invalid event number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def delete_event(events):
    view_events(events)

    if not events:
        return

    try:
        index = int(input("Enter the number of the event to delete: ")) - 1
        if 0 <= index < len(events):
            deleted_event = events.pop(index)
            print(f"Event '{deleted_event.title}' deleted successfully.")
        else:
            print("Invalid event number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    events = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_event(events)
        elif choice == '2':
            view_events(events)
        elif choice == '3':
            search_events(events)
        elif choice == '4':
            edit_event(events)
        elif choice == '5':
            delete_event(events)
        elif choice == '6':
            print("Exiting Event Scheduler. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()