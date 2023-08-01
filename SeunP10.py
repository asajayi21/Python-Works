#SeunP10.py
#Programmer: A. Seun Ajayi
#Email: aajayi@cnm.edu
#Purpose: get point from a file

import GeoPoint

def main():

    pointList = []
    pointResult = []
    
    resultPoint = GeoPoint.GeoPoint() 

    #reads from csv file
    with open("pointfile.csv") as file:
        for line in file:
            lat,lon,desc = line.rstrip().split(",")
            newPoint = GeoPoint.GeoPoint(float(lat),float(lon),desc)
            #assigns point to point list
            pointList.append(newPoint)

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
            location = 0
            
            #iterate each point and set value to closest
            for dPoint in pointList:
                pointResult.append(dPoint.Distance(pointUser))
            
            #assigns the first element as minimum
            minPoint = pointResult[0]

            #If element is min set to value and index
            for i in range(len(pointResult)):
                if pointResult[i] < minPoint:
                    minPoint = pointResult[i]
                    location = i

            #remove all elements in sequence
            pointResult.clear()
            print(pointList[location])

        finally:    
            #Checks to do another
            choice = input("Do you want to do another calculation? (y/n): ").lower()
            if choice == "n":
                calContinue = False
    
    print("\nThank you, goodbye!")

if __name__ == "__main__":
    main()
        