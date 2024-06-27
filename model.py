from flask import jsonify

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
        password="root",
        database="quizoo",
    )
    return mydb

def insert_user(nom, prenom, email, date_naissance, mdp):
    mydb = acces_bdd()  
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


def recuperer_themes():
    mydb = acces_bdd()  
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
    # Execute the queries and fetch the results
    cursor.execute(nb_theme_query)
    nb_theme_result = cursor.fetchone()[0]  # Fetch the count result
    
    cursor.execute(id_theme_query)
    id_theme_results = cursor.fetchall()
    
    cursor.execute(libelle_theme_query)
    libelle_theme_results = cursor.fetchall()
    
    dict_theme= []
    for i in range(nb_theme_result):
        mon_theme= {"id": id_theme_results[i][0], "libelle": libelle_theme_results[i][0]}
        dict_theme.append(mon_theme)


    # on ferme le curseur et l'acces a la BDD
    cursor.close()
    mydb.close()
    print (dict_theme)
    
    return dict_theme


def recuperer_questions(id_theme):
    mydb = acces_bdd()  
     # Create cursor object to execute queries
    cursor = mydb.cursor()
    
    # Define the SQL query to count themes
    
    infos_questions_reponses_query ='''
    SELECT question.id_question, question.libelle, question.id_bonne_reponse, reponse.id, reponse.libelle, reponse.image 
    FROM question JOIN reponse ON reponse.id_question = question.id_question JOIN theme ON theme.id = question.id_theme 
    WHERE theme.id=%s ORDER BY question.id_question, reponse.id;
    '''
    
    cursor.execute(infos_questions_reponses_query, (id_theme,))
    infos_questions_reponses_result = cursor.fetchall()

    cursor.close()
    mydb.close()

    questions = {}
    for row in infos_questions_reponses_result:
        question_id = row[0]
        question_text = row[1]
        correct_answer_id = row[2]
        answer_id = row[3]
        answer_text = row[4]
        answer_image = row[5]
        
        if question_id not in questions:
            questions[question_id] = {
                'id_question': question_id,
                'libelle': question_text,
                'id_bonne_reponse': correct_answer_id,
                'reponses': []
            }
        
        questions[question_id]['reponses'].append({
            'id': answer_id,
            'libelle': answer_text,
            'image': answer_image
        })
    
    return jsonify(questions)
    
    print (infos_questions_reponses_query)
    
    return infos_questions_reponses_query

def verif_email(email):
    mydb = acces_bdd()  
    cursor = mydb.cursor()
    
    check_email_query = '''
    SELECT mail FROM utilisateur WHERE mail = %s;
    '''
    cursor.execute(check_email_query, (email,))
    check_email_result = cursor.fetchone()
    
    if check_email_result is None:
        result = False  # email pas trouvé dans la BDD
    else:
        result = True  


    mydb.commit()   
    cursor.close()
    mydb.close()

    print (result)
    return result

def verif_connexion(email, mot_de_passe):
    mydb = acces_bdd()  
    cursor = mydb.cursor()
    
    check_user_query = '''
    SELECT mdp FROM utilisateur WHERE mail = %s;
    '''
    
    cursor.execute(check_user_query, (email,))
    check_user_result = cursor.fetchone()
    
    if check_user_result and check_user_result[0] == mot_de_passe:
        known = True  # utilisateur connu de la BDD
    else:
        known = False  

    cursor.close()
    mydb.close()

    print (known)
    return known


# def trouver_question():
#     acces_bdd()
#     query = '''
#     SELECT libelle FROM question WHERE id_theme == {id_theme_choisi}
#     '''


# def trouver_bonne_reponse():
#     acces_bdd()
#     query = '''
#     SELECT libelle FROM reponse WHERE id_question == {id_question_en_cours}
#     '''



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
