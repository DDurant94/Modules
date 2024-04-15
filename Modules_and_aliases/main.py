'''
3. Mastering Python Modules and Aliases
Objective:
The aim of this assignment is to enhance your proficiency in using Python modules, both standard and custom, 
with a specific focus on importing with aliases. This will develop your skills in organizing code, simplifying 
access to module components, and effectively managing namespace in Python programs.

Task 1: Custom Module with Aliases

Problem Statement: Create a custom module named text_utils.py with functions for string manipulation 
(e.g., reversing a string, capitalizing). In your main script, import this module using an alias and utilize its functions.
Code Example:
```python
# text_utils.py
def reverse_string(s):
# function to reverse a string
def capitalize_string(s):
    # function to capitalize a string

# main.py
# Import text_utils using an alias and utilize its functions

```
Expected Outcome: Your main script should be able to use the functions from text_utils.py via an alias, 
demonstrating an understanding of custom module creation and aliasing.
'''
import text_utils as tu

def main():
  print("Welcome to Python Modules and Aliases")
  while True:
    print("Main menu:\n1. Reverse text\n2. Capitalize text\n3. Capitalize All Words\n4. Exit")
    choice = input("Choose a menu option: ")
    if choice == "1":
      string = input("Enter a text that you want reversed: ")
      tu.reverse_string(string)
    elif choice == "2":
      string = input("Enter a text that you want capitalized: ")
      tu.capitalize_string(string)
    elif choice == "3":
      string = input("Enter a text that you want capitalized: ")
      tu.capitalize_all(string)
    elif choice == "4":
      print("Goodbye!")
      break
    else:
      print("Invalid choice")

main()