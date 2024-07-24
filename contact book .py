import json

def load_contacts(filename='contacts.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (IOError, json.JSONDecodeError):
        return {}

def save_contacts(contacts, filename='contacts.json'):
    try:
        with open(filename, 'w') as file:
            json.dump(contacts, file, indent=4)
    except IOError as e:
        print(f"An error occurred while saving contacts: {e}")

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }

    save_contacts(contacts)
    print("Contact added successfully!")

def display_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']} , address: {details['address']}")

def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ")
    found_contacts = {name: details for name, details in contacts.items()
                      if search_term in name or search_term in details['phone']}

    if not found_contacts:
        print("No contacts found.")
        return

    for name, details in found_contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")

    if name not in contacts:
        print("Contact not found.")
        return

    phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ")
    email = input(f"Enter new email (current: {contacts[name]['email']}): ")
    address = input(f"Enter new address (current: {contacts[name]['address']}): ")

    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }

    save_contacts(contacts)
    print("Contact updated successfully!")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")

    if name not in contacts:
        print("Contact not found.")
        return

    del contacts[name]
    save_contacts(contacts)
    print("Contact deleted successfully!")

def main():
    contacts = load_contacts()

    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            display_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
