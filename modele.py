from flask import Flask

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="quizoo"
)

mycursor = mydb.cursor()

mycursor.execute