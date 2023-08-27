import pickle
from collections import UserDict

class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

class AddressBook(UserDict):
    def add_contact(self, contact):
        self.data[contact.name] = contact.phone_number

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.data, file)

    def load_from_file(self, filename):
        with open(filename, 'rb') as file:
            self.data = pickle.load(file)

    def search_contacts(self, search):
        result = []
        for name, phone_number in self.data.items():
            if (search.lower() in name.lower() or search in phone_number):
                result.append((name, phone_number))
        return result

def main():
    address_book = AddressBook()

    try:
        address_book.load_from_file('address_book.bin')
    except FileNotFoundError:
        pass

    while True:
        print("1. Add contact.")
        print("2. Search contacts.")
        print("3. Exit.")
        choice = input("Select the option: ")

        if choice == '1':
            name = input("Enter the name: ")
            phone_number = input("Enter the phone number : ")
            contact = Contact(name, phone_number)
            address_book.add_contact(contact)
            address_book.save_to_file('address_book.bin')
        elif choice == '2':
            search = input("Enter the 'name/phone': ")
            result = address_book.search_contacts(search)
            if result:
                print("Result:")
                for name, phone_number in result:
                    print(f"Name: {name}, Phone number: {phone_number}")
            else:
                print("Sorry! No matches found.")
        elif choice == '3' or choice == 'exit':
            break
        else:
            print("Oops! Please choose the correct option.")

if __name__ == "__main__":
    main()
