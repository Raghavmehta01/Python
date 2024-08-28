athletes = [
    {"name": "Nathan Hales", "country": "Great Britain", "medal_type": "Gold", "gender": "Male", "event": "Men's Trap", "year": 2024, "metric": "Hits out of 125"},
    {"name": "Amber Rutter", "country": "Great Britain", "medal_type": "Silver", "gender": "Female", "event": "Women's Skeet", "year": 2024, "metric": "Hits out of 60"},
    {"name": "Amber Hill", "country": "Great Britain", "medal_type": "Gold", "gender": "Female", "event": "Women's Skeet", "year": 2020, "metric": "Hits out of 60"},
    {"name": "Matt Coward-Holley", "country": "Great Britain", "medal_type": "Bronze", "gender": "Male", "event": "Men's Skeet", "year": 2020, "metric": "Hits out of 60"},
    {"name": "Sarah Hayward", "country": "Great Britain", "medal_type": "Silver", "gender": "Female", "event": "Women's Trap", "year": 2016, "metric": "Hits out of 75"},
    {"name": "Peter Wilson", "country": "Great Britain", "medal_type": "Gold", "gender": "Male", "event": "Men's Double Trap", "year": 2016, "metric": "Hits out of 150"},
    {"name": "Peter Wilson", "country": "Great Britain", "medal_type": "Gold", "gender": "Male", "event": "Men's Double Trap", "year": 2012, "metric": "Hits out of 150"},
    {"name": "Vincent Hancock", "country": "Great Britain", "medal_type": "Silver", "gender": "Male", "event": "Men's Skeet", "year": 2012, "metric": "Hits out of 125"},
    {"name": "Richard Faulds", "country": "Great Britain", "medal_type": "Gold", "gender": "Male", "event": "Men's Trap", "year": 2008, "metric": "Hits out of 125"},
    {"name": "Peter Wilson", "country": "Great Britain", "medal_type": "Silver", "gender": "Male", "event": "Men's Double Trap", "year": 2008, "metric": "Hits out of 150"},
    {"name": "Richard Faulds", "country": "Great Britain", "medal_type": "Gold", "gender": "Male", "event": "Men's Trap", "year": 2004, "metric": "Hits out of 125"},
    {"name": "Ian Peel", "country": "Great Britain", "medal_type": "Bronze", "gender": "Male", "event": "Men's Double Trap", "year": 2004, "metric": "Hits out of 150"}
]
medals = 12

def add_details(name, country,medal_type, gender, event, year, metric):
    global medals
    athletes.append({
        "name": name.lower(),
        "country": country,
        "medal_type": medal_type,
        "gender": gender,
        "event": event,
        "year": year,
        "metric": metric
    })
    medals += 1

def view_details():
    if not athletes:
        print("No Information")
        return

    print("\nChoose an option:")
    print("1. View all records")
    print("2. View specific athlete record")
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            print(f"\n{'Name':<20} {'Country':<15} {'Medal':<10} {'Gender':<10} {'Event':<20} {'Year':<5} {'Metric':<20}")
            print("-" * 100)
            print()  
            
            for athlete in athletes:
                print(f"{athlete['name']:<20} {athlete['country']:<15} {athlete['medal_type']:<10} {athlete['gender']:<10} {athlete['event']:<20} {athlete['year']:<5} {athlete['metric']:<20}")
            print()
        case 2:
            athname = input("Enter the athlete's name: ").lower()
            
            found = False
            for athlete in athletes:
                if athlete["name"].lower() == athname:
                    print("Name:", athlete["name"].title())
                    print("Country:", athlete["country"])
                    print("Medal:", athlete["medal_type"])
                    print("Gender:", athlete["gender"])
                    print("Event:", athlete["event"])
                    print("Year:", athlete["year"])
                    print("Metric:", athlete["metric"])
                    print()
                    found = True
            if not found:
                print("No information found for the given athlete.")
        case _:
            print("Invalid choice")

def medal_count():
    return medals

def ath_performance(athname):
    athname = athname.lower()
    for athlete in athletes:
        if athlete["name"].lower() == athname:
            return athlete["metric"]
    return "Athlete not found"


def event_details(event_name):
    event_name = event_name.lower()
    event_athletes = []
    for athlete in athletes:
        if athlete["event"].lower() == event_name:
            event_athletes.append(athlete)
    if not event_athletes:
        return "No athletes found for this event"
    return event_athletes

def menu():
    while True:
        print("\nMenu:")
        print("1. View Athlete Details")
        print("2. Add Athlete Details")
        print("3. View Medal Count")
        print("4. View Athlete Performance")
        print("5. View Event Details")
        print("6. Exit")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                view_details()
            case "2":
                name = input("Enter athlete's name: ")
                country = input("Enter country: ")
                medal_type = input("Enter medal type (Gold/Silver/Bronze): ")
                gender = input("Enter gender: ")
                event = input("Enter event: ")
                year = int(input("Enter Olympic year: "))
                metric = input("Enter performance metric : ")
                add_details(name, country, medal_type, gender, event, year, metric)
                print("Athlete added successfully.")
            case "3":
                print(f"Total medals: {medal_count()}")
            case "4":
                athname = input("Enter athlete's name: ")
                print(f"Performance of {athname}: {ath_performance(athname)}")
            case "5":
                event_name = input("Enter event name: ")
                result = event_details(event_name)
                if result == "No athletes found for this event":
                    print(result)
                else:
                    for athlete in result:
                        print(f"Name: {athlete['name']}, Country: {athlete['country']}, Medal: {athlete['medal_type']}, Year: {athlete['year']}, Metric: {athlete['metric']}")
            case "6":
                print("Exited")
                break
            case _:
                print("Invalid choice")


while True:
    menu()
