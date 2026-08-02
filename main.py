# Contact Manager CLI — entry point

import json

CONTACTS_FILE = 'contacts.json'

contacts = []

def load_contacts():
    global contacts
    try:
        with open(CONTACTS_FILE, "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []

def save_contacts():
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)


def show_menu():
    print("\n=== Contact Manager ===")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5.Exit")

def add_contact():
    name = input("Enter contact name: ").strip()
    phone = input("Enter contact phone number: ").strip()
    email = input("Enter contact email: ").strip()

    if not name:
        print("Name cannot be empty. Contact not added.")
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    save_contacts()
    print(f"Contact '{name}' added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\n=== Contacts List ===")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']:<15} | {contact['phone']:<15} | {contact['email']}")

def search_contacts():
    if not contacts:
        print("\nNo contacts saved yet.")
        return
    
    search_name = input("\nEnter name to search: ").strip().lower()
    results = [c for c in contacts if search_name in c['name'].lower()]

    if not results:
        print("\nNo matching contact found.")

    print(f"\n=== Search Results ({len(results)}) ===")
    for i, contact in enumerate(results, start=1):
        print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']}")

def delete_contact():
    if not contacts:
        print("\nNo contacts saved yet.")
        return

    view_contacts()
    try:
        choice = int(input("Enter the number of the contact to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if 1 <= choice <= len(contacts):
        removed = contacts.pop(choice - 1)
        save_contacts
        print(f"Deleted contact '{removed['name']}'.")
    else:
        print("Invalid contact number.")

def main():
    print("=" * 40)
    print("     Welcome to Contact Manager CLI")
    print("=" * 40)
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contacts()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 5")

if __name__ == "__main__":
    load_contacts()
    main()