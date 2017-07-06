"""
forloop.py
Input a string and will output how many spaces, vowels, consonants,
and other characters there are in the string. Ys are not counted as a vowel
"""

string=input("type in your sentence: ")

spacecount=0
vowelcount=0
consonantscount=0
othercount=0

for x in string:
    if x.lower() == " ":
        spacecount+=1
    elif x.lower() in "aeiou":
        vowelcount+=1
    elif x.lower() in "bcdfghjklmnpqrstvwxz":
        consonantscount+=1
    else:
        othercount+=1
    
print("There are", spacecount, "spaces", vowelcount, "vowels", consonantscount, "consonants and", othercount, "other characters", sep=' ') 
