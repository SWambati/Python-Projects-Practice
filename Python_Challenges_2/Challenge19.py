#this program allows users to enter and search for contact information stored in a dictionary

def contact_book():
    contacts ={}

    print("Hello! Welcome to your contact book.")

    while True:
        print("Contact Book Menu: ")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. View Contact List")
        print("6. Exit")

        option = input("Select an option between 1 and 6: ")

        if option == "1":
            name = input("Enter the contact name: ").strip()
            phone_number = input("Enter the contact's phone number: ").strip()
            contacts[name] = phone_number
            print(f"Your new contact, {name}, has been added to the contact book successfully.")

        elif option == "2":
            name = input("Enter the contact name to search: ").strip()
            if name in contacts:
                print(f"{name}: {contacts[name]}")
            else:
                print(f"There is no contact named {name} in the contact list.")
        
        elif option == "3":
            name = input("Enter the contact name to update: ").strip()
            if name in contacts:
                new_phone_number = input(f"Enter the new phone number for {name}: ").strip()
                contacts[name] = new_phone_number
                print(f"New phone number for {name} has been updated successfully.")
            else:
                print(f"There is no contact with the name {name} in the contact list")
        elif option == "4":
            name = input("Enter the contact name to delete: ").strip()
            if name in contacts:
                del contacts[name]
                print(f"The contact {name} has been deleted successfully")
            else:
                print(f"There is no contact with the name {name} in your contact list")
        
        elif option == "5":
            if contacts:
                print("Contact List:")

                for name, phone_number in contacts.items():
                    print(f"{name} : {phone_number}")
            
            else:
                print("You do not have any contacts in your contact list yet")

        elif option == "6":
            print("You have close the contact book")
            break

        else:
            print("Please enter a valid option between 1 and 6")


contact_book()




