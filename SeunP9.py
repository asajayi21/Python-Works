#SeunP9.py
#Programmer: A. Seun Ajayi
#Email: aajayi@cnm.edu
#Purpose: create a better class

import math
import GeoPoint

def main():
    #Constructor to set point
    point1 = GeoPoint.GeoPoint(36.16,-86.77,"Nashville")

    point2 = GeoPoint.GeoPoint()
    
    point2.Pcoordinate = 35.07,-106.64
    point2.descP = "Albuquerque"

    calContinue = True

#Gets input and calls class method to calculate distance
    while calContinue:
        #Trys to get input values
        try:
            userLat = float(input("Enter you Latitude: "))
            userLon = float(input("Enter you Longitude: "))
            userDesc = input("Enter the Description: ")
        #catches the errors
        except TypeError:
            print("Wrong type of input!")
        except Exception as e:
            print ("Something went wrong:", e)
        #If no error execute code
        else:
            pointUser = GeoPoint.GeoPoint(userLat, userLon,userDesc)
            distanceToOne = point1.Distance(pointUser)
            distanceToTwo = point2.Distance(pointUser)

            #logical test, which distance is closer
            if distanceToOne < distanceToTwo:
                print(point1)
            else:
                print(point2)
        #Runs code regardless of error or not
        finally:    
            #Checks to do another
            choice = input("Do you want to do another calculation? (y/n): ").lower()
            if choice == "n":
                calContinue = False
   
    print("\nThank you, goodbye!")

if __name__ == "__main__":
    main()