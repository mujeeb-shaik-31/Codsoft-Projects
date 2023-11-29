contacts = {}  # Dictionary to store contacts

def add_contact():
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")
    contacts[name] = number
    print(f"Added {name} with number {number} to contacts.")

def search_contact():
    name = input("Enter contact name to search: ")
    if name in contacts:
        print(f"{name}'s number is {contacts[name]}.")
    else:
        print(f"{name} is not in contacts.")

def display_contacts():
    if contacts:
        print("Contacts:")
        for name, number in contacts.items():
            print(f"{name}: {number}")
    else:
        print("No contacts available.")

def delete_contact():
    name = input("Enter contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"{name} has been deleted from contacts.")
    else:
        print(f"{name} is not in contacts.")

# User interaction loop
while True:
    print("\n*** Contact Book Menu ***")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Display Contacts")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        search_contact()
    elif choice == '3':
        display_contacts()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")