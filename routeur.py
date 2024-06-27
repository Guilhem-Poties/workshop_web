# -*- coding: utf-8 -*-
from flask import Flask,request,render_template,jsonify,abort
from flask_cors import CORS
# from flask_restful import Api, Resource 

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

CORS(app)


# infos_utilisateur={}
# liste_themes={}
# progression_globale=0
# liste_question={}

# @app.route("/")
# def index():
#     return render_template('index.html')


@app.route("/question")
def question():
    return render_template("question.html")

# @app.route("/connexion", methods=['POST', 'GET'])
# def session():
#     ##session
@app.route("/", methods=['GET'])
def connexion_get():
    return render_template('connexion.html')

@app.route("/inscription", methods=['POST'])
def inscription():
    try:
        nom = request.form['nom']
        prenom = request.form['prenom']
        email = request.form['email']
        date_naissance = request.form['date_de_naissance']
        mdp = request.form['mdp']

        if model.verif_email(email):
            return "Error: email already taken"

        print(f"Received data: {nom}, {prenom}, {email}, {date_naissance}, {mdp}")
        model.insert_user(nom, prenom, email, date_naissance, mdp)
        print("User inserted successfully!")
        return "User inserted successfully!"

    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred"

@app.route("/connexion", methods=['POST'])
def connexion():
    try:
        email = request.form['email']
        mdp = request.form['mdp']

        if not model.verif_connexion(email, mdp):
            return "Error: user not found. Try again or register"

        print("User connected successfully!")
        return theme()

    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred"
   

@app.route("/index", methods=['POST', 'GET'])
def theme():
    themes = model.recuperer_themes()
    return render_template("index.html", theme_list=themes)
    

# @app.route("/question/<theme_id>", methods=['POST', 'GET'])
# def question():

#     themes = model.recuperer_themes()
#     return render_template("index.html", theme_list=themes)
    


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
 