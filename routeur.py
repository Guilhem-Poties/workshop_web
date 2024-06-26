# -*- coding: utf-8 -*-
from flask import Flask,request,render_template,jsonify,abort
from flask_cors import CORS
# from flask_restful import Api, Resource 

#from flaskmysqldb import MySQL
import model
from model import recupere_question

############# si modele.py est dans une autre dossier de routeur.py
# import sys
# sys.path.append('../lol/modele')
############
#lié notre fichier actuel : routeur.cpp avec modele.cpp
#import modele
#importer une foncion qui est dans le fichier modele
#from modele import fonction1, fonction2
 
app = Flask(__name__)

CORS(app)

#todos = {}

# class ToDoSimple(Resource):
#     def get(self, todo_id):
#         return {todo_id: todos[todo_id]}
#     def put(self, todo_id):
#         todos [todo_id] = request.form["data"]
#         return {todo_id: todos[todo_id]}

# api.add_resource(ToDoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)


#les absences, c'est pour un dictionnaire qui pour un entier donne le nom et le nombre d'absences
# structure absences : { 1:{'nom':'toto', 'abs':3}, 2:{'nom':'bob', 'abs':3} }
# infos_utilisateur={}
# liste_themes={}
# progression_globale=0
# liste_question={}

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/index", methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        print("GET request received")
        return render_template('index.html')
    
    if request.method == 'POST':
        print("POST request received")
        try:
            nom = request.form['nom']
            prenom = request.form['prenom']
            email = request.form['email']
            date_naissance = request.form['date_de_naissance']
            mdp = request.form['mdp']
            print("Received data: {nom}, {prenom}, {email}, {date_naissance}, {mdp}")
            model.insert_user(nom, prenom, email, date_naissance, mdp)
            cursor.execute(sql_insert_query, record_to_insert)
            connection.commit()
            print("User inserted successfully!")
            return "User inserted successfully!"
        except Exception as e:
            print(f"Error: {e}")
            return "An error occurred"
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

@app.route("/connexion", methods=['POST', 'GET'])
def index():

@app.route("/question", methods=['POST', 'GET'])
def index():

# @app.route('/login', methods = ['POST', 'GET'])
# def login():
#     if request.method == 'GET':
#         return "Login via the login Form"

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
     
#     if request.method == 'POST':
#         name = request.form['name']
#         age = request.form['age']
#         cursor = mysql.connection.cursor()
#         cursor.execute(''' INSERT INTO info_table VALUES(%s,%s)''',(name,age))
#         mysql.connection.commit()
#         cursor.close()
#         return f"Done!!"
