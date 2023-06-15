#SeunP4.py
#Programmer: Seun Ajayi
#Email: aajayi@cnm.edu
#Purpose: provides user capability to translate a phrase from Spanish to English

#Create the dictionary
commonPhrase = {"Hola":"Hello","Como estas?":"How are you?","Bien":"Good","Gracias":"Thank you"}

#Print out the keys
print(commonPhrase.keys())

#Ask for input from user
word = input("Please enter a phrase to translate: ")

#Checks phrase is in dictionary or prints not able to translate
if word in commonPhrase: 
    print("Your sentence in english: {}".format(commonPhrase.get(word,"n/a")))
else:
    print("Unable to translate.")
