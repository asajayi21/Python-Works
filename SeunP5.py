#SeunP5.py
#Programmer: A. Seun Ajayi
#Email: aajayi@cnm.edu
#Purpose: To play the game rock, paper, scissors

import random

#Create the list
computerScore = userScore = 0
choices=['rock','paper','scissors']

print("Welcome to the rock, paper, scissors game.")

gameContinue = True

#Ends game if user enters no
while gameContinue:

    #Breaks loop if any player won twice 
    while computerScore < 2 and userScore < 2:
        userInput = input("\nPlease select \"rock\", \"paper\", or \"scissors\" : ").lower()
        compChoice = random.randint(0,2)

        #Check for winner and increment their score
        if choices[compChoice] == userInput:
            print("It's a Tie!")
        elif choices[compChoice] == "rock" and userInput == "paper":
            userScore +=1
            print(f"You won! - {userInput} covers {choices[compChoice]}")
            print(f"You selected: {userInput}; the computer selected: {choices[compChoice]}")
            print(f"You won that round; The game's score is: {userScore} - {computerScore}.\n")
        elif choices[compChoice] == "rock" and userInput == "scissors":
            computerScore +=1
            print(f"You lost! - {choices[compChoice]} knocks {userInput}")
            print(f"You selected: {userInput}; the computer selected: {choices[compChoice]}")
            print(f"You lost that round; The game's score is: {userScore} - {computerScore}.\n")
        elif choices[compChoice] == "paper" and userInput == "rock":
            computerScore +=1
            print(f"You lost! - {choices[compChoice]} covers {userInput}")
            print(f"You selected: {userInput}; the computer selected: {choices[compChoice]}")
            print(f"You lost that round; The game's score is: {userScore} - {computerScore}.\n")
        elif choices[compChoice] == "paper" and userInput == "scissors":
            userScore +=1
            print(f"You won! - {userInput} cuts {choices[compChoice]}")
            print(f"You selected: {userInput}; the computer selected: {choices[compChoice]}")
            print(f"You won that round; The game's score is: {userScore} - {computerScore}.\n")
        elif choices[compChoice] == "scissors" and userInput == "rock":
            userScore +=1
            print(f"You won! - {userInput} knocks {choices[compChoice]}")
            print(f"You selected: {userInput}; the computer selected: {choices[compChoice]}")
            print(f"You won that round; The game's score is: {userScore} - {computerScore}.\n")
        else:
            computerScore +=1
            print(f"You lost! - {choices[compChoice]} cuts {userInput}")
            print(f"You selected: {userInput}; the computer selected: {choices[compChoice]}")
            print(f"You lost that round; The game's score is: {userScore} - {computerScore}.\n")
    
    #Breaks loop when player enters no
    choice = input("Do you want to play another round of rock, paper, scissors? (yes/no): ").lower()
    if choice == "no":
        gameContinue = False
    else:
        computerScore = userScore = 0

print("Thank you for playing rock, paper, and scissors.")