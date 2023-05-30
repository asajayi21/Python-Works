#SeunP2.py
#Programmer: A. Seun Ajayi
#Email: aajayi@cnm.edu
#Purpose: provides user capability to view contact info

def main():
    #Program Menu
    print("Welcome to state info finder.")
    print("This program will tell you the information for a state you input.\n")
    #Get input from user
    stateName = input("Please enter the name of a state: ")

    #Call function to get state information
    solutionReturn(stateName)        
    
    print("\nThank you for using state info finder.\n")


def solutionReturn(stateName):
    #Initialize the lists              
    States = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware',
    'Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana',
    'Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska',
    'Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio',
    'Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas',
    'Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']

    Capitals = ['Montgomery','Juneau','Phoenix','Little Rock','Sacramento','Denver','Hartford','Dover',
    'Tallahassee','Atlanta','Honolulu','Boise','Springfield','Indianapolis','Des Moines','Topeka','Frankfort',
    'Baton Rouge','Augusta','Annapolis','Boston','Lansing','St. Paul','Jackson','Jefferson City','Helena','Lincoln',
    'Carson City','Concord','Trenton','Santa Fe','Albany','Raleigh','Bismarck','Columbus','Oklahoma City','Salem',
    'Harrisburg','Providence','Columbia','Pierre','Nashville','Austin','Salt Lake City','Montpelier','Richmond','Olympia',
    'Charleston','Madison','Cheyenne']
    
    NumCongressional = ['9','3','11','6','54','10','7','3','30','16','4','4','19','11','6','6','8','8','4','10',
    '11','15','10','6','10','4','5','6','4','14','5','28','16','3','17','7','8','19','4','9','3','11','40','6','3',
    '13','12','4','10','3']
    
    StateHoods = ['22','49','48','25','31','38','5','1','27','4','50','43','21','19','29','34','15','18','23','7',
    '6','26','32','20','24','41','37','36','9','3','47','11','12','39','18','46','33','2','13','8','40','16','28',
    '45','14','10','42','35','30','44']
    
    #Print out information about the state
    print(f"\nThe capital of {stateName} is {Capitals[States.index(stateName)]} it has {NumCongressional[States.index(stateName)]} congressional districts and it is state number " +
    f"{StateHoods[States.index(stateName)]} in the union.")

main()