# -*- coding: utf-8 -*-
from flask import Flask,request,render_template,jsonify,abort, session, redirect
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
app.config["SESSION_PERMANENT"] = False
# import os
# secret_key = os.urandom(24)
# print(secret_key)
app.config['SECRET_KEY'] = 'lolilolprout'
CORS(app)

id_theme = 0

# infos_utilisateur={}
# liste_themes={}
# progression_globale=0
# liste_question={}

# @app.route("/")
# def index():
#     return render_template('index.html')
@app.route("/logout")
def logout():
	session["name"] = None
	return redirect("/")

@app.route("/question/<id>", methods=['GET', 'POST'])
def question(id):
    global id_theme
    id_theme = id
    print(id)
    return render_template('question.html')

@app.route("/api/v1/question", methods=['GET', 'POST'])
def create_question():
    if not session.get("name"):
        # if not there in the session then redirect to the login page
        return redirect("/connexion")
    quest = model.recuperer_questions(id_theme)
    return quest


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
        session["name"] = request.form.get("email")
        return theme()

    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred"
   

@app.route("/index", methods=['POST', 'GET'])
def theme():
    if not session.get("name"):
        return redirect("/connexion")
    themes = model.recuperer_themes()
    return render_template("index.html", theme_list=themes)

@app.route('/compte', methods=['POST', 'GET'])
def compte():
    if not session.get("name"):
        return redirect("/connexion")
    liste_donnees_user = model.donnees_user(session['name'])
    return render_template("compte.html", liste_donnees_user=liste_donnees_user)

@app.route("/progression",  methods=['POST', 'GET'])
def progression():
    if not session.get("name"):
        return redirect("/connexion")
    liste_dates_et_scores = model.progression_semaine(session['name']) 
    return render_template("progression.html", dates_et_scores = liste_dates_et_scores)

# @app.route("/question/<theme_id>", methods=['POST', 'GET'])
# def question():
#     themes = model.recuperer_themes()
#     return render_template("index.html", theme_list=themes)
    


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
 