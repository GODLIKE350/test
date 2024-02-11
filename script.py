import os
import csv

class Phonebook:
    def __init__(self, filename):
        # Initialize the Phonebook with a filename for the CSV file
        self.filename = filename
        self.entries = []
        # Load entries from the CSV file when the Phonebook is created
        self.load_entries()

    def load_entries(self):
        # Load entries from the CSV file into the Phonebook
        if os.path.exists(self.filename):
            with open(self.filename, 'r', newline='') as file:
                reader = csv.DictReader(file)
                # Convert the reader object to a list and store it in self.entries
                self.entries = list(reader)

    def save_entries(self):
        # Save the current entries to the CSV file
        with open(self.filename, 'w', newline='') as file:
            # Define the fieldnames for the CSV file
            fieldnames = ['Last Name', 'First Name', 'Middle Name', 'Organization', 'Work Phone', 'Personal Phone']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            # Write the header to the CSV file
            writer.writeheader()
            # Write the entries to the CSV file
            writer.writerows(self.entries)

    def add_entry(self, entry):
        # Add a new entry to the Phonebook and save the changes
        self.entries.append(entry)
        self.save_entries()

    def edit_entry(self, index, entry):
        # Edit an existing entry in the Phonebook at the given index
        if 0 <= index < len(self.entries):
            self.entries[index] = entry
            self.save_entries()

    def search_entries(self, search_term):
        # Search for entries that contain the search term in any of their fields
        return [entry for entry in self.entries if any(search_term.lower() in value.lower() for value in entry.values())]

    def display_entries(self, page_number, entries_per_page):
        # Display entries for a given page number and number of entries per page
        start_index = (page_number - 1) * entries_per_page
        end_index = start_index + entries_per_page
        # Print each entry on the current page
        for entry in self.entries[start_index:end_index]:
            print(entry)

def main():
    # Create a new Phonebook instance with the filename 'phonebook.csv'
    phonebook = Phonebook('phonebook.csv')
    while True:
        # Display the menu options
        print("\n1. Display entries")
        print("2. Add entry")
        print("3. Edit entry")
        print("4. Search entries")
        print("5. Exit")
        choice = input("Enter your choice: ")

        # Handle the user's choice
        if choice == '1':
            # Display entries for a given page
            page_number = int(input("Enter page number: "))
            entries_per_page = int(input("Enter entries per page: "))
            phonebook.display_entries(page_number, entries_per_page)
        elif choice == '2':
            # Add a new entry to the Phonebook
            entry = {
                'Last Name': input("Enter last name: "),
                'First Name': input("Enter first name: "),
                'Middle Name': input("Enter middle name: "),
                'Organization': input("Enter organization: "),
                'Work Phone': input("Enter work phone: "),
                'Personal Phone': input("Enter personal phone: ")
            }
            phonebook.add_entry(entry)
        elif choice == '3':
            # Edit an existing entry in the Phonebook
            index = int(input("Enter index of the entry to edit: "))
            entry = {
                'Last Name': input("Enter last name: "),
                'First Name': input("Enter first name: "),
                'Middle Name': input("Enter middle name: "),
                'Organization': input("Enter organization: "),
                'Work Phone': input("Enter work phone: "),
                'Personal Phone': input("Enter personal phone: ")
            }
            phonebook.edit_entry(index, entry)
        elif choice == '4':
            # Search for entries in the Phonebook
            search_term = input("Enter search term: ")
            results = phonebook.search_entries(search_term)
            for result in results:
                print(result)
        elif choice == '5':
            # Exit the program
            break
        else:
            # Handle invalid choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


