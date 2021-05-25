from flask import Flask, request
from app.Controller import getUserByName, insertUser, AllUser, getResponse

app = Flask(__name__)

@app.route('/users', defaults={'name':None}, methods=['GET'])
@app.route('/users/<name>', methods=['GET'])
def getUser(name):
    if name:
        return getUserByName(name)  
    else:
        return AllUser()

@app.route('/users/create', methods=['POST'])
def createUser():

    body = request.get_json()

    if 'name' not in body:
        return getResponse(404, "Parameter name is required") 

    if 'pass' not in body:
        return getResponse(404, "Parameter pass is required") 

    if 'email' not in body:
        return getResponse(404, "Parameter email is required")  

    return insertUser(body['name'], body['pass'], body['email'])

app.run(debug=True)

 