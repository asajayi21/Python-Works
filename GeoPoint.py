#GeoPoint.py
#Programmer: A. Seun Ajayi
#Email: aajayi@cnm.edu
#Purpose: create a GeoPoint class

import math

#create class
class GeoPoint:
    def __init__(self,lat=0, lon=0,description='TBD'):
        self.lat = lat
        self.lon = lon
        self.description = description

    #string method to print object 
    def __str__(self):
        return f"You are closest to {self.description} which is located at ({self.lat:.2f},{self.lon:.2f})"

    def GetPoint(self):
        return self.lat, self.lon

    #tuple variable to set the lat and lon
    def SetPoint(self, Pcoordinate):
        self.lat, self.lon = Pcoordinate
    
    #property to call the setter and getter methods
    Pcoordinate = property(GetPoint, SetPoint)

    def SetDescription(self, descP):
        self.description = descP
    
    def GetDescription(self):
        return self.description

    #property to set and get the description method
    descP = property(GetDescription,SetDescription)

    #Calculates distance    
    def Distance(self, toPoint):
        userPoint = toPoint.Pcoordinate

        a = math.sin((self.lat-userPoint[0])/2) * math.sin((self.lat-userPoint[0])/2) \
        + math.cos(self.lat) * math.cos(userPoint[0]) * (math.sin((self.lon-userPoint[1])/2) * math.sin((self.lon-userPoint[1])/2))
    
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

        d = 6371.0 * c

        return d
