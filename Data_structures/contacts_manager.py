# Question two: Task one
import re
name_match = r"[A-Za-z]{2,15}\s[A-Za-z]{2,15}"
phone_match = r"(\d{1}-\d{3}-\d{3}-\d{4})"
def add_contact(contacts,name,phone_number):
  contact_info = validating(name,phone_number)
  if contact_info:
    if name not in contacts:
      contacts[name] ={"Phone Number": phone_number}
    else:
      return f"{name} is already in contacts"
  else:
    return f"Can't Validate contact info"

def remove_contact(contacts,name):
  if name in contacts:
    contacts.pop(name)
    print(f"{name} has been removed")
  else:
    return "Name not found"

def view_contacts(contacts):
  for person, info in contacts.items():
     print(f"{person}\nPhone Number: {info["Phone Number"]}\n")

def validating(name,phone):
  validate_name = re.match(name_match,name)
  validate_phone = re.match(phone_match,phone)
  if validate_name:
    if validate_phone:
      return True
  else:
    return False