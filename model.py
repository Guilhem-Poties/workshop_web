import mysql.connector
# ############# si routeur.py est dans une autre dossier de modele.py
# # import sys
# # sys.path.append('../lol/routeur')
# ############
# #lié notre fichier actuel : modele.cpp avec routeur.cpp
# import routeur
# #importer une foncion qui est dans le fichier routeur
# from routeur import fonction1, fonction2

def acces_bdd():
    mydb= mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user="root",
        password="",
        database="quizoo",
    )

def insert_user(nom, prenom, email, date_naissance, mdp):
    acces_bdd()
    cursor = mydb.cursor()
    query = '''
    INSERT INTO utilisateur (nom, prenom, mail, date_naissance, mdp)
    VALUES (%s, %s, %s, %s, %s)
    '''
    values = (nom, prenom, email, date_naissance, mdp)
    cursor.execute(query, values)
    mydb.commit()
    if (mydb.is_connected()):
            cursor.close()
            mydb.close()
            print("MySQL connection is closed")


# def trouver_theme(){
#     ##FAIRE BOUTON ACTION DANS CHAQUE THEME 
#     query = '''
#     SELECT id_theme FROM theme WHERE question.id_theme == theme.id_theme 
#     '''
# }

def recuperer_themes():
    acces_bdd()
     # Create cursor object to execute queries
    cursor = mydb.cursor()
    
    # Define the SQL query to count themes
    nb_theme_query = '''
    SELECT COUNT(id) FROM theme;
    '''
    id_theme_query = '''
    SELECT id FROM theme;
    '''
    libelle_theme_query = '''
    SELECT libelle FROM theme;
    '''
     # Execute the query
    cursor.execute(nb_theme_query)
    cursor.execute(id_theme_query)
    cursor.execute(libelle_theme_query)
    # Fetch the count result
    nb_theme_result = cursor.fetchone()
    id_theme_query = cursor.fetchone()
    libelle_theme_query = cursor.fetchone()
    
    dict_theme= []
    for i in range(nb_theme_query):
        mon_theme= {"id": "id_theme_query[i]", "libelle":"libelle_theme_query[i]"}
        dict_theme.append(mon_theme)


   
    # Close cursor and database connection
    cursor.close()
    mydb.close()
    
    # Return the count of themes
    return dict_theme

    ##recuperer le nombre dans une variable

def trouver_question():
    acces_bdd()
    query = '''
    SELECT libelle FROM question WHERE id_theme == {id_theme_choisi}
    '''


def trouver_bonne_reponse():
    acces_bdd()
    query = '''
    SELECT libelle FROM reponse WHERE id_question == {id_question_en_cours}
    '''



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
