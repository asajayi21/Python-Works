#CreateDB.py
#Programmer: A. Seun Ajayi
#Email: aajayi@cnm.edu
#Purpose: create database with values

import pyodbc

try:
    #Connection to MS SQL DB
    my_sql_conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost\SQLEXPRESS;Database=master;Trusted_Connection=yes;')

    curs = my_sql_conn.cursor()
    #query to create table
    create_sql = 'CREATE TABLE [FlashCardDB].[dbo].[PointDB] (Latitude DECIMAL(5,2), Longitude DECIMAL(5,2), Description varchar(255))'

    curs.execute(create_sql)
    #query to insert value to table
    insert_sql = 'INSERT INTO [FlashCardDB].[dbo].[PointDB] VALUES (?,?,?)'

    #opens file and insert value to table
    with open("pointfile.csv") as file:
            for line in file:
                vals = line.rstrip().split(",")
                curs.execute(insert_sql,vals)

    my_sql_conn.commit()

    #query to check values is inserted in table
    select_sql = 'SELECT * FROM [FlashCardDB].[dbo].[PointDB]'
    curs.execute(select_sql)
    records = curs.fetchall()
    #prints records
    for row in records:
        print(f"Lat: {row[0]} Lon: {row[1]} Desc: {row[2]}")
except pyodbc.Error as e:
     print(f"Error occured {e}")
finally:
    if my_sql_conn:
        my_sql_conn.close()
        print("Connection is closed!")
