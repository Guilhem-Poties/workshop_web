from flask import Flask, render_template, request
#moi
from flask_mysqldb import MySQL

# ############# si routeur.py est dans une autre dossier de modele.py
# # import sys
# # sys.path.append('../lol/routeur')
# ############
# #lié notre fichier actuel : modele.cpp avec routeur.cpp
# import routeur
# #importer une foncion qui est dans le fichier routeur
# from routeur import fonction1, fonction2


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'quizoo'

mysql = MySQL(app)
    

def insert_user(nom, prenom, email, date_naissance, mdp):
    cursor = mysql.connection.cursor()
    query = '''
    INSERT INTO utilisateur (nom, prenom, mail, date_naissance, mdp)
    VALUES (%s, %s, %s, %s, %s)
    '''
    values = (nom, prenom, email, date_naissance, mdp)
    cursor.execute(query, values)
    mysql.connection.commit()
    cursor.close()

# mydn = mysql.connect(
#     host = 'localhost',
#     user = 'root',
#     password = '',
#     database = 'quizoo'
# )

# @app.route("/index", methods = ['POST', 'GET'])
# def index():
#     # mycursor = mydb.cursor()
#     # mycursor.execute("SELECT * FROM question")
#     # allQuestions = mycursor.fetchall()
#     # print(allQuestions)

#     if request.method == 'GET':
#         return render_template('session.html')
#         # return "Login via the login Form"
     
    
#     if request.method == 'POST':
#             nom = request.form['nom']
#             prenom = request.form['prenom']
#             mail = request.form['email']
#             date_de_naissance = request.form['date_de_naissance']
#             mdp = request.form['mot_de_passe']
#             cursor = mysql.connection.cursor()
#             cursor.execute(''' INSERT INTO utilisateur VALUES(id,nom, prenom, mail, date_naissance, mdp)''',(nom, prenom, mail, date_de_naissance, mdp))
#             mysql.connection.commit()
#             cursor.close()
#             return f"Done!!"


# ##### INFOS SUR UN SITE 
# # mysql = MySQL(app)
 
# # #Creating a connection cursor
# # cursor = mysql.connection.cursor()
 
# # #Executing SQL Statements
# # cursor.execute(''' CREATE TABLE table_name(field1, field2...) ''')
# # cursor.execute(''' INSERT INTO table_name VALUES(v1,v2...) ''')
# # cursor.execute(''' DELETE FROM table_name WHERE condition ''')
 
# # #Saving the Actions performed on the DB
# # mysql.connection.commit()
 
# # #Closing the cursor
# # cursor.close()
