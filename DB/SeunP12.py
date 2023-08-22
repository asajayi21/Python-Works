#SeunP12.py
#Programmer: A. Seun Ajayi
#Email: aajayi@cnm.edu
#Purpose: POINTS IN A DATABASE

from tkinter import END
import tkinter as tk
import pyodbc
import GeoPoint

pointList = []
pointResult = []

#Define Functions
def loadPoints():
    #Connection to MS SQL DB
    my_sql_conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost\SQLEXPRESS;Database=master;Trusted_Connection=yes;')

    curs = my_sql_conn.cursor()
    #query to get values from table
    select_sql = 'SELECT * FROM [FlashCardDB].[dbo].[PointDB]'

    curs.execute(select_sql)
    records = curs.fetchall()
    for row in records:
        newPoint = GeoPoint.GeoPoint(float(row[0]),float(row[1]),row[2])
        pointList.append(newPoint)

def close_win():
   mainWindow.destroy()

def calcPoints():
    #Call function to load points
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

#Define window
mainWindow = tk.Tk()
mainWindow.title("GeoPoint Calculator")
mainWindow.geometry('475x225')
mainWindow.resizable(1,0)

#Define Frames
result_frame = tk.Frame(mainWindow, width=275,height = 75)
exit_frame = tk.Frame(mainWindow, bg='#E6E6E6', width=275,height = 75)

#Pack Frames
result_frame.pack()
exit_frame.pack()

#Create Widgets
lat_lbl = tk.Label(result_frame, text='Enter Latitude')
lat_lbl.grid(row=0,column=0,padx=2,pady=5)
lat_value = tk.Entry(result_frame, width = 15)
lat_value.grid(row=0,column=1,padx=5,pady=5)

lon_lbl = tk.Label(result_frame, text='Enter Longitude')
lon_lbl.grid(row=1,column=0,padx=2,pady=5)
lon_value = tk.Entry(result_frame, width = 15)
lon_value.grid(row=1,column=1,padx=2,pady=5)

result_lbl = tk.Entry(result_frame, width = 55)
result_lbl.grid(row=2,column=0, padx=2, pady=5,columnspan=2, ipadx=10)

cal_btn = tk.Button(exit_frame, text='Calculate', command=calcPoints)
cal_btn.grid(row=0,column=2,columnspan=2, padx=5,pady=5,ipadx=10)
exit_btn = tk.Button(exit_frame, text='Exit', command=close_win)
exit_btn.grid(row=0,column=0, columnspan=2, padx=5, pady=5, ipadx=10)

#Run window
mainWindow.mainloop()






