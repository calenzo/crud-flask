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

    return { "Error" : 404, "Message" : "Do not user is exists" }

def insertUser(name, password, email):

    with connection.cursor() as cursor:
        cursor.execute(f'INSERT INTO `people` (`name`, `pass`, `email`) VALUES ("{name}", "{password}", "{email}")')
        connection.commit()

    return { "name" : name }

def getResponse(state, message, nameContent=False, content=False):
    
    response = {}
    response["state"] = state
    response["message"] = message

    if(nameContent and content):
        response[nameContent] = content

    return response        
