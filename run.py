from flask import Flask, request
from app.Controller import *

app = Flask(__name__)


@app.route('/users', defaults={'name':None}, methods=['GET'])
@app.route('/users/<name>', methods=['GET'])
def getUser(name):
    if name:
        return getUserByName(name)  

    return AllUser()


@app.route('/users/create', methods=['POST'])
def createUser():
    body = request.get_json()

    error = getErrorParams(body, "name", "password1", "password2", "email")
 
    if error != -1:
        return error

    name = body['name']
    password1 = body['password1']
    password2 = body['password2']
    email = body['email']

    if password1 != password2: 
        return getResponse(400, "Bad Request", "It's not the same", {
            "password1" : "password1",
            "password2" : "password2"
        })
        
    return insertUser(name, 
        password1, 
        email
    )



app.run(debug=True)

 