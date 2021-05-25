from app.Model import connection
from flask import jsonify

def AllUser():

    with connection.cursor() as cursor:
        cursor.execute(f'SELECT * FROM `people`')
        rows = cursor.fetchall()

    return jsonify(rows)

def getUserByName(name):
                                                               
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT * FROM `people` WHERE `name`="{name}"')
        rows = cursor.fetchall()

    for row in rows:
        return { "id" : row['id'], "name" : row['name'], "pass" : row['pass'], "email" : row['email'] }

    return getResponse(404, "Do not user is exists")

def insertUser(name, password, email):

    cursor = connection.cursor()

    cursor.execute(f'SELECT `name` FROM `people` WHERE `name`="{name}"')
    row = cursor.fetchall()
 
    if row:
        return getResponse(404, "User exists")

    cursor.execute(f'SELECT `email` FROM `people` WHERE `email`="{email}"')
    row = cursor.fetchall()

    if row:
        return getResponse(404, "Email exists")      

    cursor.execute(f'INSERT INTO `people` (`name`, `pass`, `email`) VALUES ("{name}", "{password}", "{email}")')
    connection.commit()

    return getResponse(200, "User create", "user", { "name" : name })     

def getResponse(state, message, nameContent=False, content=False):
    
    response = {}
    response["state"] = state
    response["message"] = message

    if(nameContent and content):
        response[nameContent] = content

    return response        
