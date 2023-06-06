#SeunP3.py
#Programmer: Seun Ajayi
#Purpose: provides user capability to find fruit in a string

#Define variables
Fruits = ["apple","watermelon","lemon","orange","grapes","strawberry","blueberries"]
fCount = 0
lFruit = []

#Gets input from user
getSentence = input("Please enter a sentence with a fruit in it: ")

#Gets the count of fruit in sentence
for fruit in Fruits:
    fCount += getSentence.lower().count(fruit)
    #If fruit in sentence append to sequence
    if fruit in getSentence.lower():
        lFruit.append(fruit)

#Displays result and list of fruit in sentence
print(f"I found {fCount} fruits in your sentence.")
print(f"Your fruits are: {lFruit}")

#Checks if sequence has value
# Then locate the index of fruit in sentence
# Sets value to variable
# Use variable to one instance of fruit in sentence
if len(lFruit)>0:
    fLen = len(lFruit[0])
    location = getSentence.lower().find(lFruit[0])
    rSentence = getSentence[location:location+fLen]
    newSentence = getSentence.replace(rSentence,"Brussel Sprouts",1)

else:
    newSentence = getSentence

#Display new sentence
print(f"Your sentence with some brussel sprouts: \"{newSentence}\"")
