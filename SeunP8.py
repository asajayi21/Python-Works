#SeunP8.py
#Programmer: A. Seun Ajayi
#Email: aajayi@cnm.edu
#Purpose: demonstrate error handling

import math

#create class
class GeoPoint:
    def __init__(self):
        self.lat = 0.0
        self.lon = 0.0
        self.description =""

#create methods to class
    def SetPoint(self, lat, lon):
        self.lat = lat
        self.lon = lon
    
    def GetPoint(self):
        return (self.lat, self.lon,)

#Calculates distance    
    def Distance(self, lat, lon):
        a = math.sin((lat-self.lat)/2) * math.sin((lat-self.lat)/2) + math.cos(self.lat) * math.cos(lat) * math.sin((lon-self.lon)/2) * math.sin((lon-self.lon)/2)
    
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

        d = 6371.0 * c

        return d

    def SetDescription(self, description):
        self.description = description
    
    def GetDescription(self):
        return self.description
    
def main():

    #initialize the object of the class
    point1 = GeoPoint()
    point2 = GeoPoint()

    #Sets values to the class objects
    point1.SetPoint(36.1,-86.8)
    point1.SetDescription("Nashville")
    
    point2.SetPoint(35,-106)
    point2.SetDescription("Albuquerque")

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
        except KeyboardInterrupt:
            print("\nYou must enter a number!")
        except Exception as e:
            print ("Something went wrong:", e)
        #If no error execute code
        else:
            distanceToOne = point1.Distance(userLat, userLon)
            distanceToTwo = point2.Distance(userLat, userLon)

            #logical test, which distance is closer
            if distanceToOne < distanceToTwo:
                print(f"You are closest to {point1.GetDescription()} which is located at {point1.GetPoint()}.")
            else:
                print(f"You are closest to {point2.GetDescription()} which is located at {point2.GetPoint()}.")
        #Runs code regardless of error or not
        finally:    
            #Checks to do another
            choice = input("Do you want to do another calculation? (y/n): ").lower()
            if choice == "n":
                calContinue = False
   
    print("\nThank you, goodbye!")


main()
