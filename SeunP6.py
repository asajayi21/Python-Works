#SeunP6.py
#Programmer: A. Seun Ajayi
#Email: aajayi@cnm.edu
#Purpose: A program that calculates the distance between two geographic points

import math

def main():
    #Calls to header function
    header()

    calContinue = True

#Ends calculation if user enters no
    while calContinue:
        point1 = tuple(get_location())
        point2 = tuple(get_location())

        Caldistance = distance(point1, point2)

        print(f"The distance between points {point1} and {point2} is {Caldistance:.2f}\n")
        
        #Checks to do another
        choice = input("Do you want to do another calculation? (yes/no): ").lower()
        if choice == "no":
            calContinue = False
   
    print("\nThank you, goodbye!")

#Prints out message
def header():
    print("Welcome, the purpose of this program is to calculate the distance between two geographic points.\n")

#Gets location 
def get_location():
    result = []
    
    lat = float(input("Enter the latitude in decimal degrees: "))
    long = float(input("Enter the longitude in decimal degrees: "))

    #append values to list
    result.append(lat)
    result.append(long)

    return result

#Calculates distance
def distance(point1, point2):
    try:
        a = math.sin((point2[0]-point1[0])/2) * math.sin((point2[0]-point1[0])/2) + math.cos(point1[0]) * math.cos(point2[0]) * math.sin((point2[1]-point1[1])/2) * math.sin((point2[1]-point1[1])/2)
    
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

        d = 6371.0 * c
    except:
        print("Error return -1.")
        return -1

    return d


main()

