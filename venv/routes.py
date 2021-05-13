from flask import Flask, request
from functions import insertUser

app = Flask(__name__)

@app.route('/users', methods=["POST"])
def index():

    body = request.get_json()

    if 'name' not in body:
        return { "status" : 400, "mensagem" : "Parametro nome é obrigatório!" }

    if 'pass' not in body:
        return { "status" : 400, "mensagem" : "Parametro senha é obrigatório!" }

    if 'email' not in body:
        return { "status" : 400, "mensagem" : "Parametro email é obrigatório!" }
 
    user = insertUser(body['name'], body['pass'], body['email'])

    return user

app.run(debug=True)