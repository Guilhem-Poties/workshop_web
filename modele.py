from flask import Flask

import mysql.connector

mydb = mysql.connector.connect(
    port=8889,
    host="localhost",
    user="root",
    password="root",
    database="quizoo"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM question")
allQuestions = mycursor.fetchall()
print(allQuestions)