"""
ReadsURL.py
Loop through the lines of a text from a url
Add lines to a list
sort the list of lines in order of increasing length
"""

import sys
import urllib.request

url = "http://oit2.scps.nyu.edu/~meretzkm/INFO1-CE9264/src/christmas/christmas.html"

try:
    lines = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print("urllib.error.URLError", error)
    sys.exit(1)

listOfLines = []    #Start with an empty list.

for line in lines:
    try:
        s = line.decode("utf-8") #Convert sequence of bytes to string of characters.
    except UnicodeError as unicodeError:
        print(unicodeError)
        sys.exit(1)
    listOfLines.append(s)
lines.close()
listOfLines.sort(key = len)

for list in listOfLines:
    print(list)


sys.exit(0)
