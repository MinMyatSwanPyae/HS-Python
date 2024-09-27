import random

# Data structures to hold user and item data
users: dict = {}
items: dict = {}

def main() -> None:
    while True:
        print("\nWelcome to the Lost and Found System!")
        start_command = input("Type 'Start' to begin or 'Exit' to quit: ").strip().lower()

        if start_command == "start":
            user_type = input("Are you a student or staff? Enter 'student' or 'staff': ")\
                .strip().lower()

            if user_type == "student":
                handle_student()
            elif user_type == "staff":
                handle_staff()
            else:
                print("Invalid user type input. Please enter 'student' or 'staff'.")
        elif start_command == "exit":
            print("Exiting the system. Thank you for using the Lost and Found System!")
            break
        else:
            print("Invalid command. Type 'Start' to begin or 'Exit' to quit.")

def handle_student() -> None:
    while True:
        choice = input("Do you want to 'login' or 'signup'? ").lower().strip()
        if choice in ["signup", "login"]:
            if choice == "signup":
                signup()
            elif choice == "login":
                email = input("Enter your email: ")
                if email in users:
                    student_menu(email)
                else:
                    print("User not found, please sign up.")
                    signup()
            break
        print("Invalid choice. Please type 'login' or 'signup'.")

def signup() -> None:
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = int(input("Enter your phone number as an integer: "))
    major = input("Enter your major: ")
    degree = input("Are you a Bachelor or Master? ")
    year = input("Enter your academic year: ")
    
    users[email] = {
        "name": name,
        "email": email,
        "phone": phone,
        "major": major,
        "degree": degree,
        "year": year,
        "points": 0,
        "reported": [],
        "claimed": []
    }
    print("Account created successfully!")
    student_menu(email)

def student_menu(email: str) -> None:
    while True:
        print("\nChoose an option:")
        print("a) Report a found item")
        print("b) Check for a lost item")
        print("c) View items you reported")
        print("d) View items you claimed")
        print("e) View your point wallet")
        print("f) Exit to main menu")
        
        choice = input("Enter your choice (a, b, c, d, e, f): ").lower().strip()
        if choice in ['a', 'b', 'c', 'd', 'e', 'f']:
            if choice == 'a':
                report_item(email)
            elif choice == 'b':
                check_lost_item()
            elif choice == 'c':
                view_reported_items(email)
            elif choice == 'd':
                view_claimed_items(email)
            elif choice == 'e':
                view_points(email)
            elif choice == 'f':
                break
        else:
            print("Invalid choice. Please enter one of the following: a, b, c, d, e, f.")

def report_item(email: str) -> None:
    date = input("Enter the date you found the item (YYYY-MM-DD): ")
    item_name = input("Enter the name of the item: ")
    locations = [
        "Welcome.Space", "Mission.Space", "Startup.Space(0.7)", "Personal.Space(6.1)",
        "Personal.Space(6.2)", "Personal.Space(6.3)", "Personal.Space(6.4)", 
        "Startup.Space(08)", "Bar.Space", "Lab.Space", "Crew.Space", "Open.Space", 
        "Venture.Space", "Growth.Space", "Interactive.Space", "Head.Space", 
        "Meeting.Space", "Cyber.Space", "Data.Space"
    ]
    print("Choose the location where you found the item:")
    while True:
        for idx, location in enumerate(locations):
            print(f"{idx+1}) {location}")
        try:
            location_index = int(input("Enter the number of the location: ")) - 1
            location = locations[location_index]
            break
        except (IndexError, ValueError):
            print("Invalid selection. Please enter a number from the list above.")

    note = input("Add a note (optional): ")
    
    unique_id = generate_unique_id()
    items[unique_id] = {
        "date": date,
        "name": item_name,
        "location": location,
        "reporter": email,
        "note": note,
        "status": "unclaimed",
        "claimer": None,
        "claim_date": None
    }
    users[email]["reported"].append(unique_id)
    print("Thank you for your information. Your report has been saved.")
    print(f"Item ID: {unique_id}")

def generate_unique_id() -> int:
    return random.randint(100000, 999999)

def check_lost_item() -> None:
    while True:
        method = input("Search by 'date' or 'location'? ").strip().lower()
        if method in ["date", "location"]:
            break
        print("Invalid method. Please enter 'date' or 'location'.")

    if method == "date":
        date = input("Enter the date (YYYY-MM-DD): ")
        found_items = {id: item for id, item in items.items() if item['date'] == date}
    elif method == "location":
        print("Choose the location to check for your lost item:")
        locations = [
            "Welcome.Space", "Mission.Space", "Startup.Space(0.7)", "Personal.Space(6.1)",
            "Personal.Space(6.2)", "Personal.Space(6.3)", "Personal.Space(6.4)", 
            "Startup.Space(08)", "Bar.Space", "Lab.Space", "Crew.Space", "Open.Space", 
            "Venture.Space", "Growth.Space", "Interactive.Space", "Head.Space", 
            "Meeting.Space", "Cyber.Space", "Data.Space"
        ]
        for idx, location in enumerate(locations):
            print(f"{idx+1}) {location}")
        location_index = int(input("Enter the number of the location: ")) - 1
        location = locations[location_index]
        found_items = {id: item for id, item in items.items() if item['location'] == location}

    display_items(found_items)
    print("Enter the Unique ID of the item you believe is yours, or type 'unknown' if you don't know:")
    user_input = input().strip()
    if user_input.lower() == 'unknown':
        print("Please contact our support for further assistance.")
        return
    try:
        item_id = int(user_input)
        if item_id in found_items:
            confirm = input("Are you sure this is your item? (yes/no): ").strip().lower()
            if confirm == "yes":
                claim_item(item_id)
            else:
                print("Item not claimed.")
        else:
            print("No item found with that ID.")
    except ValueError:
        print("Invalid input. Please enter a valid numeric ID or type 'unknown'.")

def claim_item(item_id: int) -> None:
    claimer_email = input("Enter your email to claim this item: ")
    if claimer_email in users and claimer_email != items[item_id]['reporter']:
        claim_date = input("Enter the date you are claiming this item (YYYY-MM-DD): ")
        items[item_id]['status'] = 'claimed'
        items[item_id]['claimer'] = claimer_email
        items[item_id]['claim_date'] = claim_date
        users[items[item_id]['reporter']]['points'] += 25
        users[claimer_email]['claimed'].append(item_id)
        print("Congratulations for finding your lost item!")
    else:
        print("You cannot claim your own reported item.")

def display_items(items_dict: dict) -> None:
    print("\nFound Items:")
    for id, item in items_dict.items():
        print(f"Unique ID: {id}, Name: {item['name']}, Date: {item['date']}, \
Location: {item['location']}, Reporter: {item['reporter']}")

def view_reported_items(email: str) -> None:
    print("\nItems you have reported:")
    for item_id in users[email]["reported"]:
        item = items[item_id]
        status = item['status']
        claimed_by = item['claimer'] if status == 'claimed' else "Not claimed"
        print(f"Unique ID: {item_id}, Name: {item['name']}, Date: {item['date']}, \
Location: {item['location']}, Status: {status}, Claimed by: {claimed_by}")

def view_claimed_items(email: str) -> None:
    print("\nItems you have claimed:")
    for item_id in users[email]["claimed"]:
        item = items[item_id]
        print(f"Unique ID: {item_id}, Name: {item['name']}, Claimed Date: \
{item['claim_date']}, Location: {item['location']}, Reported by: {item['reporter']}")

def view_points(email: str) -> None:
    print(f"\nYour current points: {users[email]['points']}")

def handle_staff() -> None:
    key = input("Enter the staff key: ")
    if key == "123456":
        staff_menu()
    else:
        print("Invalid key.")

def staff_menu() -> None:
    while True:
        print("\nStaff Options:")
        print("a) View all registered students' profiles")
        print("b) View all reported items")
        print("c) Exit to main menu")

        choice = input("Enter your choice (a, b, c): ").lower().strip()
        if choice == 'a':
            view_all_student_profiles()
        elif choice == 'b':
            display_all_items()
        elif choice == 'c':
            break
        else:
            print("Invalid choice. Please enter one of the following: a, b, c.")

        if input("\nWould you like to perform another action? (yes/no): ")\
                .lower().strip() != "yes":
            break

def view_all_student_profiles() -> None:
    if not users:
        print("No registered users found.")
        return
    for email, user in users.items():
        print(f"Email: {email}, Name: {user['name']}, Items Reported: \
{len(user['reported'])}, Items Claimed: {len(user['claimed'])}, Points: {user['points']}")

def display_all_items() -> None:
    if not items:
        print("No items have been reported.")
        return
    for item_id, item in items.items():
        status_info = f"Claimed by {item['claimer']} on {item['claim_date']}"\
            if item['status'] == 'claimed' else "Not claimed"
        print(f"Unique ID: {item_id}, Item Name: {item['name']}, Reporter: \
{item['reporter']}, Location: {item['location']}, Status: {status_info}, Note: {item['note']}")

if __name__ == "__main__":
    main()
