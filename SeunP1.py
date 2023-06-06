#SeunP1.py
#Programmer: Seun Ajayi
#Purpose: provides user capability to calculate the surface area and volume of a square pyramid.

import math

#Function to get the input values and to display the results.
def main():
    #Gets the input
    base = float(input("Enter the length of the base (in feet): "))
    height = float(input("Enter the the pyramid height (in feet): "))

    #Calls function to get the Slant Height
    s = findArea(base,height)
    vol = findVolume(base,height)

    #Calculates the Surface Area
    surface_area = base**2 + (s*4)

    #Display result
    print(f"The height is {height:4.3f} \nThe base is {base:4.3f}")
    print(f"The total surface area is {surface_area:.3f}  \nThe volume of the pyramid is {vol:.3f} ")

#Function to find the Area of one pyramid side
def findArea(a, h):
    #Calculates and returns the result
    s = math.sqrt(h**2+ (a/2)**2)
    return s * a/2

#Function to find the volume.
def findVolume(a, h):
    #Calculates and returns the result
    return (a**2) * (h/3)

main()

