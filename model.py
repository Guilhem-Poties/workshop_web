from flask import Flask, request

import mysql.connector
#moi
from flask_mysqldb import MySQL

############# si routeur.py est dans une autre dossier de modele.py
# import sys
# sys.path.append('../lol/routeur')
############
#lié notre fichier actuel : modele.cpp avec routeur.cpp
import routeur
#importer une foncion qui est dans le fichier routeur
from routeur import fonction1, fonction2

mydb = mysql.connector.connect(
    port=8889,
    host="localhost",
    user="root",
    password="root",
    database="quizoo"
)

@app.route("/index", methods = ['POST', 'GET'])
def index():
    # mycursor = mydb.cursor()
    # mycursor.execute("SELECT * FROM question")
    # allQuestions = mycursor.fetchall()
    # print(allQuestions)

    if request.method == 'GET':
        return render_template('session.html')
        # return "Login via the login Form"
     
    
    if request.method == 'POST':
            name = request.form['nom']
            age = request.form['prenom']
            name = request.form['email']
            age = request.form['date_de_naissance']
            name = request.form['mot_de_passe']
            cursor = mysql.connection.cursor()
            cursor.execute(''' INSERT INTO USER VALUES(id,nom, prenom, mail, date_naissance, mdp)''',(name,prenom, email, date_de_naissance, mot_de_passe))
            mysql.connection.commit()
            cursor.close()
            return f"Done!!"


##### INFOS SUR UN SITE 
# mysql = MySQL(app)
 
# #Creating a connection cursor
# cursor = mysql.connection.cursor()
 
# #Executing SQL Statements
# cursor.execute(''' CREATE TABLE table_name(field1, field2...) ''')
# cursor.execute(''' INSERT INTO table_name VALUES(v1,v2...) ''')
# cursor.execute(''' DELETE FROM table_name WHERE condition ''')
 
# #Saving the Actions performed on the DB
# mysql.connection.commit()
 
# #Closing the cursor
# cursor.close()
