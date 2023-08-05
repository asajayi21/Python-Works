#SeunP11.py
#Programmer: A. Seun Ajayi
#Email: aajayi@cnm.edu
#Purpose: demonstrate how to use a GUI

from tkinter import END
import tkinter as tk
import GeoPoint


pointList = []
pointResult = []

#Define window
mainWindow = tk.Tk()
mainWindow.title("GeoPoint Calculator")
mainWindow.geometry('300x225')
mainWindow.resizable(1,0)

#Define Functions
def loadPoints():
    with open(get_file.get()) as file:
        for line in file:
            lat,lon,desc = line.rstrip().split(",")
            newPoint = GeoPoint.GeoPoint(float(lat),float(lon),desc)
            #assigns point to point list
            pointList.append(newPoint)

def close_win():
   mainWindow.destroy()

def calcPoints():
    loadPoints()

    pointUser = GeoPoint.GeoPoint(float(lat_value.get()), float(lon_value.get()))

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

    #Display result
    result_lbl.delete(0,END)
    result_lbl.insert(0,pointList[location])

#Define Frames
input_frame = tk.Frame(mainWindow, width=275,height = 75)
result_frame = tk.Frame(mainWindow, width=275,height = 75)
exit_frame = tk.Frame(mainWindow, bg='#E6E6E6', width=275,height = 75)

#Pack Frames
input_frame.pack()
result_frame.pack()
exit_frame.pack()

#Create Widgets
file_lbl = tk.Label(input_frame, text='Enter Filename')
file_lbl.grid(row=0,column=0,padx=2,pady=5)
get_file = tk.Entry(input_frame, width = 25)
get_file.grid(row=0,column=1,padx=5,pady=5)

lat_lbl = tk.Label(result_frame, text='Enter Latitude')
lat_lbl.grid(row=0,column=0,padx=2,pady=5)
lat_value = tk.Entry(result_frame, width = 15)
lat_value.grid(row=0,column=1,padx=5,pady=5)

lon_lbl = tk.Label(result_frame, text='Enter Longitude')
lon_lbl.grid(row=1,column=0,padx=2,pady=5)
lon_value = tk.Entry(result_frame, width = 15)
lon_value.grid(row=1,column=1,padx=2,pady=5)

result_lbl = tk.Entry(result_frame, width = 25)
result_lbl.grid(row=2,column=0, padx=2, pady=5,columnspan=4, ipadx=10)

cal_btn = tk.Button(exit_frame, text='Calculate', command=calcPoints)
cal_btn.grid(row=0,column=2,columnspan=2, padx=5,pady=5,ipadx=10)
exit_btn = tk.Button(exit_frame, text='Exit', command=close_win)
exit_btn.grid(row=0,column=0, columnspan=2, padx=5, pady=5, ipadx=10)

#Run window
mainWindow.mainloop()