from distutils.util import execute
import mysql.connector
import pandas as pd
import os
import glob
#to convert the file name which is in form of tuples to string
def convertTuple(tup):
        # initialize an empty string
    str = ''
    for item in tup:
        str = str + item
    return str

connection = mysql.connector.connect(
user='root', password='12345', host='localhost',port='3306')
cursor = connection.cursor()
cursor.execute("CREATE DATABASE AudPrjct")
#the location of the csv files
path = r'/mnt/c/Users/Ashrith/Desktop/ToolV2/src/dev-src/dev-microservices/Order-To-Cash-Microservice/Data/Structure and table header data'
#fecting only the files with .csv to it
csv_files = glob.glob(os.path.join(path, "*.csv"))

for f in csv_files:
    #reading of csv files
    df = pd.read_csv(f)
    
    text=open(f,"r",encoding='utf-8')
    text = ' '.join([i for i in text])   
    text = text.replace(",", " ") #creating a string that will go as input wo Create table command
    comma="),"
    Ftxt=text.replace(")",comma)
    
    #the next two lines are the issue
    #It cant provide a proper syntax of mysql
    #Have to find a way to pass the strinf text to the below commad 
    
        

    str=convertTuple(f.split("Structure and table header data/")[-1])
    str=str.replace(".csv","")
    str=str.replace(" ","_")
    sql = "CREATE TABLE IF NOT EXISTS " + str  +""" (%s"""%(Ftxt)+""")"""
    cursor.execute(sql)
    print(sql)

connection.commit()
students = cursor.fetchall()
connection.close()

