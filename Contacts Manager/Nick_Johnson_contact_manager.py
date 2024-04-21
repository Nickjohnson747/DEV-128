"""
Assignment: Contact Manager
Class: DEV 128
Date: 01/10/24
Author: Nick Johnson
Description: Program to help user manage contacts information
    Supports
        listing all contacts,
        viewing/adding/deleting a contact,
        printing a given field for all contacts.
    Program uses dictionary of dictionaries to hold the contacts information.
"""


def list(contacts: dict[str, dict[str, str]]) -> None:
    """
    Prints the name of all contacts in the dictionary

    Parameters:
        contacts (dict[str, dict[str,str]]): dictonary of contacts to search through
    """

    i = 1
    for key in contacts.keys():
        print("\t" + str(i) + ". " + key)
        i += 1


def view(contacts: dict[str, dict[str, str]], name: str) -> None:
    """
    Prints the information for a given contact

    Parameters:
        contacts (dict[str, dict[str,str]]): Dictonary of contacts to search through
        name (str): Name of contact to display
    """

    try:
        if name in contacts:
            print("Viewing contact for", name)

        for key, value in sorted(contacts[name].items()):
            print("\t" + key + ": " + value)
    except KeyError:
        print("No contact found for that name")


def add(contacts: dict[str, dict[str, str]]) -> None:
    """
    Adds a contact to the dictionary

    Parameters:
        contacts (dict[str, dict[str,str]]): Dictonary of contacts to search through
    """

    name: str = input("Enter the name for the new contact: ").title()
    address: str = input("Enter the address for the new contact: ").title()
    mobile: str = input("Enter the mobile number for the new contact: ")
    company: str = input("Enter the company for the new contact: ")

    contacts[name] = {"address": address, "mobile": mobile, "company": company}
    print("Contact added")


def delete(contacts: dict[str, dict[str, str]], name: str) -> None:
    """
    Deletes the given contact from the contact dictioanry

    Parameters:
        contacts (dict[str, dict[str,str]]): Dictonary of contacts to search through
        name (str): Name of contact to delete
    """

    try:
        del contacts[name]
        print("Contact for " + name + " deleted")
    except KeyError:
        print("No contact found for that name")


def view_field(contacts: dict[str, dict[str, str]], field: str) -> None:
    """
    Checks dictonary to see if the given field exists

    Parameters:
        contacts (dict[str, dict[str,str]]): dictonary of contacts to search through
        field (str): field to search for and display
    """

    # Feels inefficient to do this in 2 loops; is there a way to do it in one? Does it improve runtime if I do it in 1 loop?
    i = 0
    for contact, _ in contacts.items():
        if field in contacts[contact]:
            break
        i += 1
        if i == len(contacts.keys()):
            print("No contact found with that field")
            return

    for key, _ in sorted(contacts.items()):
        if field in contacts[key]:
            print("{:15}: ".format(key), contacts[key][field])
        elif field not in contacts[key]:
            print("{:15}: ".format(key), "**No data**")


def main():
    contacts = {
        "Joel": {
            "address": "1500 Anystreet, San Francisco, 94110",
            "company": "A startup",
            "mobile": "555-555-1111",
        },
        "Anne": {
            "address": "1000 Somestreet, Fresno, CA 93704",
            "state": "California",
            "landline": "125-555-2222",
            "company": "Some Great Company",
        },
        "Sally": {
            "state": "Illinois",
            "landline": "217-555-1222",
            "company": "Illinois Technologies",
            "mobile": "217-333-2353",
        },
        "Ben": {
            "address": "1400 Another Street, Fresno CA 93704",
            "state": "California",
            "mobile": "125-555-4444",
        },
    }

    print("Welcome to contacts manager program")
    print("COMMAND MENU")
    print("\tlist - Display all contacts")
    print("\tview - View a contact")
    print("\tadd - Add a contact")
    print("\tdel - Delete a contact")
    print("\tlist - Display all contacts")
    print("\tfield - View field for all contacts")
    print("\texit - Exit the program")

    command: str = ""
    while command != "exit".lower():
        command = ""
        command = input("Please enter the command: ").lower()
        if command == "list":
            if len(contacts.keys()) > 0:
                list(contacts)
            else:
                print("No contacts to show")

        elif command == "view":
            name: str = input("Please enter the name: ").title()
            view(contacts, name)

        elif command == "add":
            add(contacts)

        elif command == "del":
            name: str = input("Enter the name: ").title()
            delete(contacts, name)

        elif command == "field":
            field: str = input(
                "Please enter the name of the field you want to view: "
            ).lower()

            view_field(contacts, field)

        elif command == "exit":
            break

        else:
            print("Invalid command")

    print("Good bye")


if __name__ == "__main__":
    main()
