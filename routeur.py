# -*- coding: utf-8 -*-
from flask import Flask,request,render_template,jsonify,abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#les absences, c'est pour un dictionnaire qui pour un entier donne le nom et le nombre d'absences
# structure absences : { 1:{'nom':'toto', 'abs':3}, 2:{'nom':'bob', 'abs':3} }
infos_utilisateur={}
liste_themes={}
progression_globale=0
liste_question={}

@app.route("/")
def saisie():
    return render_template('saisie.html')

@app.route("/index")
def index():
    return render_template('index.html')
   
   
""" @app.route("/")
def index():
    return render_template('liste.html', listeJeux = listeJeux)
""" 
@app.route("/saisie", methods=['POST'])
def new(): 
    nom = request.json['nom']
    # On vérifie d'abord si ce n'est pas déjà présent
    for joueur in liste_joueurs.values():
        if joueur['nom'] == nom:
            return "Account already existing",409
    # OK on ajoute
    global compte
    compte=compte+1 
    liste_joueurs[compte]={'nom':name, 'prenom':request.json['prenom'],'email':request.json['email'], 'date_de_naissance':request.json['date_de_naissance'],'mot_de_passe':request.json['mot_de_passe'],}

""" @app.route("/saisie", methods=['POST'])
def new():
    name = request.json['name']
    # On vérifie d'abord si ce n'est pas déjà présent
    for jeu in listeJeux.values():
        if jeu['name'] == name:
            return jsonify(absences),409
    # OK on ajoute
    global cpt
    cpt=cpt+1 
    listeJeux[cpt]={'name':name, 'price':request.json['price'], 'description':request.json['description']}
 """
""" @app.route("/liste", methods=['GET'])
def show():
    return jsonify(listeJeux) """

@app.route("/absence/<int:id>", methods=[ 'PUT', 'DELETE'])
def abs(id):
    if request.method == 'PUT':
        if id in absences:
            absences[id]['abs']=absences[id]['abs']+1
        else:
            abort(404)
    else:
        if id in absences:
            absences[id]['abs']=absences[id]['abs']-1
            if absences[id]['abs'] == 0:
                del(absences[id])
        else:
            abort(404)
    	# et au final on retourne tout le json    
    return jsonify(absences)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
