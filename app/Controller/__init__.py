from app.Model import connection
from flask import jsonify

def AllUser():
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM `people`')
    rows = cursor.fetchall()

    if rows:
        return jsonify(rows)

    return getResponse(404, "Not found") 



def getUserByName(name):
    cursor = connection.cursor()                                        
    cursor.execute(f'SELECT * FROM `people` WHERE `name`="{name}"')
    rows = cursor.fetchall()

    if rows:
        return rows

    return getResponse(404, "Not found")



def insertUser(name, password, email):
    cursor = connection.cursor()
    cursor.execute(f'SELECT `name` FROM `people` WHERE `name`="{name}"')
    row = cursor.fetchall()

    if row:
        return getResponse(404, "User exists")

    cursor.execute(f'SELECT `email` FROM `people` WHERE `email`="{email}"')
    row = cursor.fetchall()

    if row:
        return getResponse(404, "email exists")      

    cursor.execute(f'INSERT INTO `people` (`name`, `pass`, `email`) VALUES ("{name}", "{password}", "{email}")')
    connection.commit()

    return getResponse(201, "success", "user", { 
        "name" : name 
    })     



def getResponse(state, message, nameContent=False, content=False):
    response = {}
    response["state"] = state
    response["message"] = message

    if(nameContent and content):
        response[nameContent] = content

    return response        



def getErrorParams(body, *params):
    for param in params:
        if param not in body: 
            return getResponse(400, "Bad Request", "Required", {  
                param : param
            }) 
    return -1;    