'''
2. Exploring Python Modules and Data Structures Assignment
Objective:
The aim of this assignment is to deepen your understanding of Python modules, 
both built-in and custom, and to enhance your skills in working with various Python data structures like lists, 
dictionaries, and sets. This assignment focuses on practical applications of these concepts in real-world scenarios.

Task 1: Contact List Manager

Problem Statement: Create a Python script using a custom module to manage a contact list. The script should allow adding, 
removing, and displaying contacts stored in a list.
Code Example:
```python
# contacts_manager.py
# Define functions to add, remove, and display contacts
# main.py
# Implement the logic to interact with the contact manager

```
Expected Outcome: Your script should be able to add new contacts, remove existing contacts, 
and display all contacts. Each contact can be a dictionary with a name and phone number.

Task 2: Date Extractor

Problem Statement: Write a Python program that uses the datetime module to extract and 
display the current month and year. Additionally, allow the user to input a date string and parse it 
into a datetime object.
Code Example:
```python
# main.py
from datetime import datetime
# Implement code to display the current month and year
# Implement code to parse a user-input date string into a datetime object
```
Expected Outcome: The program should accurately display the current month and year and 
successfully convert a user-input date string (e.g., "2023-03-15") into a datetime object, handling any invalid inputs gracefully.
'''

# Question two: Task one


import contacts_manager as cm


def import_file(file_import):
  try:
    with open(file_import, "r") as file:
      extraction = file.readlines()
      contacts = {}
      for line in extraction:
        getting_info = line.split("/")
        contacts[getting_info[0]] = {"Phone Number": getting_info[1]}
      return contacts
  except FileNotFoundError:
    print("Error: File can not be found")

def export_file(file_import, contacts):
  try:
    with open(file_import, "w") as file:
      for person, info in contacts.items():
        file.write(f"{person}/{info["Phone Number"]}")
      print("File Updated")
  except FileNotFoundError:
    print("Error: File can not be found")
    

def main():
  print("Welcome to the contact Manager System")
  while True:
    contact_book = import_file('Data_structures\\contact_book.txt')
    print("Main Menu:\n1. Add Contact\n2. Delete Contact\n3. View Contact\n4. Exit")
    menu_choice = input("Choose one of the menu options: ")
    if menu_choice == "1":
      name = input("Name to add to contact book: ").title()
      phone_number = input(f"What is the phone number associated with {name}'s contact [1-999-999-9999]: ")
      cm.add_contact(contact_book,name,phone_number)
    elif menu_choice == "2":
      name = input("Name to remove to contact book: ").title()
      cm.remove_contact(contact_book,name)
    elif menu_choice == "3":
      cm.view_contacts(contact_book)
    elif menu_choice == "4":
      print("Thank for using the Contact Manger System!")
      break
    else:
      print("Sorry invalid choice!")
    export_file('Data_structures\\contact_book.txt',contact_book)

main()

# Task two

from datetime import datetime as dt, timedelta

def month_year():
  now = dt.now()
  current_month = now.month
  current_year = now.year
  print(f"The current month is {current_month}\nThe current year is {current_year}")

def input_date(date):
    try:
        user_date = dt.strptime(date, "%Y-%m-%d")
        print(f"Date Picked: {user_date}")
    except ValueError:
        print("Invalid date format. Please enter a valid date")

def main():
  print("Welcome Date Extractor!")
  while True:
    month_year()
    print("Main Menu:\n1. Choose Date\n2. Exit")
    user_choice = input("Choose a menu option: ")
    if user_choice == "1":
      users_date = input("Enter a date (YYYY-MM-DD): ")
      input_date(users_date)
    elif user_choice == "2":
      print("Goodbye")
      break
    else:
      print("Invalid Choice")

main()