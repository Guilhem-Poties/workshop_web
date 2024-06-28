# -*- coding: utf-8 -*-
from flask import Flask,request,render_template,jsonify,abort, session, redirect
from flask_cors import CORS

import model

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
# import os
# secret_key = os.urandom(24)
# print(secret_key)
app.config['SECRET_KEY'] = 'architecturelogicielcherrier'
CORS(app)

id_theme = 0

@app.route("/logout")
def logout():
	session["name"] = None
	return redirect("/")

@app.route("/question/<id>")
def question(id):
    global id_theme
    id_theme = id
    return render_template('question.html')
        

@app.route("/api/v1/question", methods=['GET', 'PUT'])
def create_question():
    if not session.get("name"):
        # si il n'y a pas de session on redirige vers la page de connexion
        return redirect("/connexion")
    
    if request.method == 'GET':
        quest = model.recuperer_questions(id_theme)
        return quest
    
    if request.method == 'PUT':
        try:
            data = request.get_json()

            score = data['score']

            print("Session created succesfully")

            model.insert_session(id_theme, session.get("name"), score)

        except Exception as e:
            print(f"Error: {e}")
            return "An error occurred"
        data = request.get_json()

        if 'valeur' not in data:
            return jsonify({"error": "Missing 'value' in request body"}), 400
        
        score = data['value']


@app.route("/", methods=['GET'])
def connexion_get():
    return render_template('connexion.html', erreur="none")

@app.route("/inscription", methods=['POST'])
def inscription():
    try:
        nom = request.form['nom']
        prenom = request.form['prenom']
        email = request.form['email']
        date_naissance = request.form['date_de_naissance']
        mdp = request.form['mdp']

        if model.verif_email(email):
            print("Error: email already taken")
            return render_template('connexion.html', erreur = "inscription")

        print(f"Received data: {nom}, {prenom}, {email}, {date_naissance}, {mdp}")
        model.insert_user(nom, prenom, email, date_naissance, mdp)
        print("User inserted successfully!")
        return redirect("/index")

    except Exception as e:
        print(f"Error: {e}")
        return redirect("/")

@app.route("/connexion", methods=['POST'])
def connexion():
    try:
        email = request.form['email']
        mdp = request.form['mdp']

        if not model.verif_connexion(email, mdp):
            return render_template('connexion.html', erreur = "connexion")

        print("User connected successfully!")
        session["name"] = request.form.get("email")
        return redirect("/index")

    except Exception as e:
        print(f"Error: {e}")
        return redirect("/")
   

@app.route("/index", methods=['POST', 'GET'])
def theme():
    if not session.get("name"):
        return redirect("/")
    themes = model.recuperer_themes()
    return render_template("index.html", theme_list=themes)

@app.route('/compte', methods=['POST', 'GET'])
def compte():
    if not session.get("name"):
        return redirect("/")
    liste_donnees_user = model.donnees_user(session['name'])
    return render_template("compte.html", liste_donnees_user=liste_donnees_user)

@app.route("/progression",  methods=['POST', 'GET'])
def progression():
    if not session.get("name"):
        return redirect("/")
    liste_dates_et_scores = model.progression_semaine(session['name']) 
    # liste_themes_et_scores = model.moyenne_score_theme(id_user,session['name']) pas reussi
    return render_template("progression.html", dates_et_scores = liste_dates_et_scores)



if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
 