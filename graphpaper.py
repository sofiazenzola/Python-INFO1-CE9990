"""
graphpaper.py
Let the user input four numbers to design a sheet of graph paper.
Output the graph paper 


"""

import sys
rows= input("How many rows of boxes?")
try:
    rows=int(rows)
except ValueError:
        print("That is not a valid input.It must be a whole number. Default is 3")
        rows = 3

columns= input("How many columns of boxes?")
try:
    columns=int(columns)
except ValueError:
        print("That is not a valid input.It must be a whole number. Default is 4")
        columns = 4
        
rowspace= input("How many rows of spaces in each box (e.g., 1)?")
try:
    rowspace=int(rowspace)
except ValueError:
        print("That is not a valid input.It must be a whole number. Default is 1")
        rowspace = 1

columnspace= input("How many columns of spaces in each box (e.g., 3)?")
try:
    columnspace=int(columnspace)
except ValueError:
        print("That is not a valid input.It must be a whole number. Default is 4")
        columnspace = 4

z=1
while z<=rows:
    w=1
    while w<=columns:
        print("+", columnspace*"-", end = "", sep = "")
        w+=1
    z+=1
    print()
    x=1
    while x<=rowspace:
        y=1
        while y<=columns:
            print("|", columnspace*" ", end = "", sep = "")
            y+=1
        print()
        x+=1

sys.exit(0)
