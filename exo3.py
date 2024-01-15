'''
Consider a binary file containing a certain number of records for a simple phone agenda 
management application. Each record is in the following format: <name, phone> 
Provide a Python program that allows:
• Building a binary file with n records <name, phone>.
• Listing the contents of a binary file with records <name, phone>.
• Direct access to a record of type <name, phone>
'''

import pickle
def build_agenda_file(filename, n):
  with open(filename, 'wb') as file:
    for _ in range(n):
      name = input("Enter name: ")
      phone = input("Enter phone number: ")
      record = (name, phone)
      pickle.dump(record, file)

def list_agenda_contents(filename):
  with open(filename, 'rb') as file:
    while True:
      try:
        record = pickle.load(file)
        print(record)
      except EOFError: # End Of File Error
        break
      except Exception as e:
        print("An Error Occurred")

def find_record_by_name(file_path, target):
  with open(file_path, 'rb') as file:
    while True:
      try:
        name, number = pickle.load(file)
        if name == target:
          print(f"The Number of Your Target is: {number}")
          break
      except EOFError:
        print("The Name You Provided is Not Listed")
        break

build_agenda_file("agenda.pickle", 5)

list_agenda_contents("agenda.pickle")

find_record_by_name("agenda.pickle", "james")