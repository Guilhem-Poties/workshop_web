# -*- coding: utf-8 -*-
from flask import Flask,request,render_template,jsonify,abort
from flask_cors import CORS
from flask_restful import Api, Resource 

#from flaskmysqldb import MySQL
import model

############# si modele.py est dans une autre dossier de routeur.py
# import sys
# sys.path.append('../lol/modele')
############
#lié notre fichier actuel : routeur.cpp avec modele.cpp
#import modele
#importer une foncion qui est dans le fichier modele
#from modele import fonction1, fonction2
 
app = Flask(__name__)
api = Api(app)
CORS(app)

todos = {}

# class ToDoSimple(Resource):
#     def get(self, todo_id):
#         return {todo_id: todos[todo_id]}
#     def put(self, todo_id):
#         todos [todo_id] = request.form["data"]
#         return {todo_id: todos[todo_id]}

# api.add_resource(ToDoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
 
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'flask'
 
#mysql = MySQL(app)

#les absences, c'est pour un dictionnaire qui pour un entier donne le nom et le nombre d'absences
# structure absences : { 1:{'nom':'toto', 'abs':3}, 2:{'nom':'bob', 'abs':3} }
infos_utilisateur={}
liste_themes={}
progression_globale=0
liste_question={}

@app.route("/")
def saisie():
    return render_template('index.html')

@app.route("/index", methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        email = request.form['email']
        date_naissance = request.form['date_de_naissance']
        mdp = request.form['mdp']
        model.insert_user(nom, prenom, email, date_naissance, mdp)
        return "User inserted successfully!"


# @app.route('/login', methods = ['POST', 'GET'])
# def login():
#     if request.method == 'GET':
#         return "Login via the login Form"
     
#     if request.method == 'POST':
#         name = request.form['name']
#         age = request.form['age']
#         cursor = mysql.connection.cursor()
#         cursor.execute(''' INSERT INTO info_table VALUES(%s,%s)''',(name,age))
#         mysql.connection.commit()
#         cursor.close()
#         return f"Done!!"
