'''
1. Python Modules and Data Handling Assignment
Objective:
The aim of this assignment is to assess your understanding and ability to implement Python modules, 
both built-in and custom, and to apply data handling techniques using Python's data structures and error handling. 
This assignment will help solidify your grasp on creating and using modules, 
as well as manipulating and processing data effectively in Python.

Task 1: Your Mood Today

Problem Statement: Create a Python program using a custom module that asks the user how they are 
feeling today and responds with a custom message based on the mood entered.
Code Example:
```python
# mood_responses.py
def mood_response(mood):
# Implement your response logic here
# main.py
import mood_responses
mood = input("How are you feeling today? ")
print(mood_responses.mood_response(mood))

```
Expected Outcome: The program should be able to take a user's mood as input (e.g., happy, sad, excited) and 
return a corresponding custom message
'''
import mood_responses

def main():
  print("Welcome to Mood Response System")
  name = input("What is your name? ").capitalize()
  try:
    while True:
      mood = input("How are you feeling today? [Type 'End' to exit] ").lower()
      if mood == "end":
        print("Have a great day!")
        break
      elif mood:
        print(f"\n{name}, {mood_responses.mood_response(mood)}")
  except ModuleNotFoundError as m:
    print(f"Error: {m}")
    
main()