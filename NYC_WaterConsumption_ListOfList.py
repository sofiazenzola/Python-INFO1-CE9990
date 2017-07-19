"""
nycwaterconsumption-ListOfList.py
Reads csv from NYC Open Data URL
Puts fields in a list of list
Sorts list by descending water consumption per capita (gallons per person per day)
Outputs ranking of year NYC consumed the most water per capita
"""

import sys
import csv   
import urllib.request

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

    r = csv.reader([s])         
    fields = next(r)            
    hopLines.append(fields)
lines.close()

hopLines= sorted(hopLines, key=lambda field: field[3], reverse=True)   # sort by per capita

index=0
for line in hopLines:
    if index==0:
        ##print("Rank",line[0],line[3], sep="-")
        print("Rank - {:4} - ".format(line[0]),line[3], sep="")
        index+=1
    else:
        ##print(index,line[0],line[3], sep="-")
        print("{:4} - {:4} - {:4}".format(index,line[0],line[3]))            
        index+=1

sys.exit(0)
