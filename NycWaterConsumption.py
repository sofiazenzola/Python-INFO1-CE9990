"""
NycWaterConsumption.py
Reads csv from NYC Open Data URL
Puts fields in a list of strings
Outputs the water consumption per capita (gallons per person per day) for a given year
"""

import sys
import csv   
import urllib.request

year=input("Select a year from 1979-2016: ")

url = "https://data.cityofnewyork.us/api/views/ia2d-e54m/rows.csv" \
    "?accessType=DOWNLOAD"
try:
    lines = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print("urllib.error.URLError", error)
    sys.exit(1)

hopLines = []                   

for line in lines:
    try:
        s = line.decode("utf-8")    
    except UnicodeError as unicodeError:
        print(unicodeError)
        sys.exit(1)

    r = csv.reader([s])         #[s] is a list containing one string
    fields = next(r)            #fields is a list of strings
    if fields[0] == year: 
        hopLines.append(fields)

lines.close()
for line in hopLines:
    print("In", line[0], "the water consumputer per capita was", line[3], "gallons per person per day")

sys.exit(0)
