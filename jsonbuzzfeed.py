"""
jsonbuzzfeed.py
Using Buzzfeed's API (https://newsapi.org/buzzfeed-api) download latest articles
Convert it to json format to create a dictionary
show latest article title and it's url
"""

import sys
import urllib.request
import json

url = "https://newsapi.org/v1/articles?source=buzzfeed&sortBy=latest&apiKey=8c72b8c8a1a54c519ef021745f0b0afc"


try:
    infile = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print("urllib.error.URLError", error)
    sys.exit(1)

sequenceOfBytes = infile.read()         #Read the entire input file.
infile.close()

try:
    s = sequenceOfBytes.decode("utf-8") #s is a string.
except UnicodeError as unicodeError:
    print(unicodeError)
    sys.exit(1)


try:
    dictionary = json.loads(s)          #dictionary is a dictionary.
except json.JSONDecodeError as jSONDecodeError:
    print(jSONDecodeError)
    sys.exit(1)



articles = dictionary["articles"]               
                  
print("Latest article = {}".format(dictionary["articles"][0]['title']))
print()
print("Link = {}".format(dictionary["articles"][0]['url']))
                                                             

sys.exit(0)
