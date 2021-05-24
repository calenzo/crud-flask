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
        return { "State" : 404, "Message" : "Parameter name is required" }

    if 'pass' not in body:
        return { "State" : 404, "Message" : "Parameter pass is required" }

    if 'email' not in body:
        return { "State" : 404, "Message" : "Parameter email is required" }       

    user = insertUser(body['name'], body['pass'], body['email'])

    return getResponse(200, "User create", "user", user)

@app.route('/<string>')
def undefined(string):
    return { "State" : 404, "Message" : 'URL "{}" invalid'.format(string) }

app.run(debug=True)

 