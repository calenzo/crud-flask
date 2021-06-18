from flask import Flask, request
from app.Controller import getUserByName, insertUser, AllUser, getResponse

app = Flask(__name__)


@app.route('/users', defaults={'name':None}, methods=['GET'])
@app.route('/users/<name>', methods=['GET'])
def getUser(name):
    if name:
        return getUserByName(name)  

    return AllUser()


@app.route('/users/create', methods=['POST'])
def createUser(self):
    body = request.get_json()

    if 'name' or 'password1' or 'password2' or 'email' not in body: 
        return getResponse(400, "Bad Request", "Required", {  
            "name",
            "password1",
            "password2",
            "email"
        }) 

    self.name = body['name']
    self.password1 = body['password1']
    self.password2 = body['password2']
    self.email = body['email']

    if self.password1 != self.passowrd2: 
        return getResponse(400, "Bad Request", "It's not the same", {
            "password1",
            "password2"
        })
    return insertUser(self.name, 
        self.password1, 
        self.email
    )


app.run(debug=True)

 