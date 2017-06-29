"""
control.py
Ask the user for input if it is cloudy outside
Outputs some advice for the weather


"""

import sys

while True:
    answer= input("Is it cloudy outside?")

    if answer.lower()=="yes":
        print("You may need this ☂")

    elif answer.lower()=="no":
        print("Enjoy the sun ☀")
    else:
        print("Please type only "\"yes"\" or "\"no""\.")


sys.exit(0)
