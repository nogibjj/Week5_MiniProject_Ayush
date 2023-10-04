"""
Transforms and Loads data into the local SQLite3 database
Example:
,general name,count_products
"""
import sqlite3
import csv
import os

#load the csv file and insert into a new sqlite3 database
def load(dataset="/workspaces/Week5_MiniProject_Ayush/diabetes.csv"):
    """"Transforms and Loads data into the local SQLite3 database"""

    #prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=''), delimiter=',')
    conn = sqlite3.connect('diabetesDB.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS diabetesDB")
    c.execute("CREATE TABLE diabetesDB ("
          "Pregnancies,Glucose,BloodPressure,SkinThickness,"
          "Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome)")

    #insert
    c.executemany("INSERT INTO diabetesDB VALUES (?,?, ?, ?, ?, ?, ?, ?, ?)", payload)
    conn.commit()
    conn.close()
    return "diabetesDB.db"

load()

