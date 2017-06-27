"""
Homework #1 
Sofia Zenzola 
inout.py

Prompt the user for their first name.
Then tell them how many characters are in their name 
"""

import sys
while True:
    try:
        name = input("What is your name? ")
    except EOFError:
        print("I'll assume your name is Bob.")
        name = 'Bob'

    if name=="":
        print("You didn't type anything. I'll assume your name is Bob.")
        name = 'Bob'

    length = len(name)
    print(name,"is", length, "characters long!")
sys.exit(0)
