"""
twelvedaysofchristmas.py

Loop through the items in a list to ouput a repetative song
"""

import sys

def ordinal(n):
    lastDigit = n % 10
    last2Digits = n % 100
    
    if 11 <= last2Digits and last2Digits <= 13:
        ordinal = "th"
    elif lastDigit == 1:
        ordinal = "st"
    elif lastDigit == 2:
        ordinal="nd"
    elif lastDigit == 3:
        ordinal="rd"
    else:
        ordinal="th"
    return ordinal        
    



gift = [
    "Partridge in a Pear Tree.",  # 0
    "Turtle Doves", # 1
    "French Hens",     # 2
    "Calling Birds",     # 3
    "Gold Rings",     # 4
    "Geese a-Laying",      # 5
    "Swans a-Swimming",   # 6
    "Maids a-Milking",    # 7
    "Ladies Dancing",  # 8
    "Lords a-Leaping",   # 9
    "Pipers Piping",   #10
    "Drummers Drumming"    #11
]
n = len(gift)
lyric= " "
listgifts= " "

for d in range(n):
    day=d+1
    lyricprep="On the " + str(day) + ordinal(day) + " day of Christmas my true love sent to me "
    if day==1:
        lyric = lyricprep + "a " + gift[d] 
        listgifts= "and a " + gift[d] 
    else:
        listgifts = str(day)+" "+ gift[d] + ", " + listgifts
        lyric = lyricprep + str(listgifts)   

    print(lyric)
    print()

sys.exit(0)
