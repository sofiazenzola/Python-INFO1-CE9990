"""
dictionary.py
(This is last week's (July 20th) homework assignment that I'm turning in late"
This program reads a dictionary about info from test restaurants in nyc
-It loops through the dictionary to get a list of 'filtering options' (ex. overall_rating, cuisine, etc)"
-Calls a GUI that reads that list in a drop down menu
-When "Outdoor_Dinning" is select and hit the button, it filters through the dictionary...
..to ouput list of restaurants where there is outdoor dinning"
-This version (because of time constraints) only works if "Outdoor_Dinning" is selected
(Will continue to work on this as a personal project)
"""

import sys
import tkinter


mydic={'Overall_Rating': {0: 3.0, 1: 3.0, 2: 4.0, 3: 3.0, 4: 4.0, 5: 3.0, 6: 5.0, 7: 3.0, 8: 3.0, 9: 5.0, 10: 5.0},
    'Cuisine': {0: 'American', 1: 'American', 2: 'Bagels', 3: 'Italian', 4: 'Latin American', 5: 'Mexican', 6: 'American (New)', 7: 'American (New)', 8: 'Mexican', 9: 'Mediterranean', 10: 'Southern & Soul'},
    'Neighborhood': {0: 'Alphabet City', 1: 'Alphabet City', 2: 'Alphabet City', 3: 'Alphabet City', 4: 'Alphabet City', 5: 'Alphabet City', 6: 'Alphabet City', 7: 'Alphabet City/Chelsea', 8: 'Battery Park', 9: 'Brooklyn - Park Slope', 10: 'Brooklyn - Red Hook'},
    'Name': {0: 'Sidewalk Cafe', 1: '7A Cafe', 2: 'Tompkins Square Bagels', 3: 'Gnocco', 4: 'Yuca Bar and Restaurant', 5: "Benny's Burritos", 6: 'Tuome', 7: 'Westville', 8: 'El Vez', 9: 'Miriam', 10: 'Hometown BBQ'},
    'Notes': {0: 'Burgers are good, good drinks', 1: 'Late night food', 2: "Best neighborhood bagel place out there - variety, cost, value. The Kaitlyn + bacon. French toast bagel + Strawberry cream cheese. Yes. A million options - can't go wrong.", 3: "Get the gnocco, go with people that like sharing because you're going to want to try it all.", 4: 'Good brunch - mellow and food was great', 5: 'Fine food, great margaritas', 6: '**Faint** : magnificent - go hungry and bring friends. Devilled eggs to start, the scallop crudo melts in your mouth, lobster roll was tiny but amazing. Pig out for two is a must - that crispy pork belly is perfection. The lamb and  red snapper too did not disappoint, falls apart in your mouth. and then get whatever dim sum they pass around, its worth it.', 7: "Always fresh and tasty, solid pick if there's not the typical long wait", 8: "Good tacos and guac! Not a reason to go down to Battery Park, but if you're there, it's a good dinner. Good looking cocktails as well.", 9: 'LOVE. THIS. PLACE. 6 small plates for $32 and it was all delicious. Right down the street from Barclays. Not at all touristy, hidden neighborhood gem.', 10: '**Transport to Texas** the hype is real. Get ready for the best kind of meat sweats. Brisket and ribs were all we could do. But go with a group and get it all.'},
    'Price_Point': {0: '$$', 1: '$$', 2: '$', 3: '$$$', 4: '$$$', 5: '$$', 6: '$$$', 7: '$$$', 8: '$$$$', 9: '$$', 10: '$$$'},
    'Outdoor_Dinning': {0: 'N', 1: 'N', 2: 'N', 3: 'Y', 4: 'N', 5: 'Y', 6: 'N', 7: 'N', 8: 'N', 9: 'N', 10: 'N'}
}

def buttonPress():   #Called when the button is pressed.
    answerText.delete("1.0", tkinter.END)
    
    try:
        optionAnswer = str(optionName.get())
    except ValueError:
        answerText.insert("1.0", "Couldn't find " + optionName.get())
        return
    
    if optionAnswer=='Outdoor_Dinning':
        for i, key in enumerate(mydic[optionAnswer]): 
            if mydic[optionAnswer][i]=='Y':
                a='Name:', mydic['Name'][i], 'Cuisine:', mydic['Cuisine'][i],'Price_Point:',mydic['Price_Point'][i],'Overall_Rating:',mydic['Overall_Rating'][i],'Neighborhood:',mydic['Neighborhood'][i],'Notes:',mydic['Notes'][i],'Outdoor_Dinning:',mydic['Outdoor_Dinning'][i]
                a=str(a)
                answerText.insert("1.0", a + "\n" + "\n")
     


        
root = tkinter.Tk()
root.title("Restaurant List")
root.geometry("750x300")

dropdownLabel = tkinter.Label(root, text = "Choose an option", width = 15)
dropdownLabel.grid(row = 0, column = 1)

optionNames=[]
not_option=['Notes','Name'] ##Eliminate the options that cannot used as a filter 
for key in mydic:
    if any(x in key for x in not_option):
        continue
    else:
        optionNames.append(key)
        
optionName = tkinter.StringVar(root)   
optionName.set(optionNames[0])         
optionMenu = tkinter.OptionMenu(root, optionName, *optionNames)
optionMenu.grid(row = 1, column = 1)

answerText = tkinter.Text(root, width = 100,
    height = 40, borderwidth = 2, relief = "groove")
answerText.grid(row = 2, column = 0, columnspan = 3)



button = tkinter.Button(root, text = "Go", command = buttonPress)
button.grid(row = 1, column = 2)



root.mainloop() 
