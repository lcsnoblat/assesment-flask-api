from flask import Flask, request
from flask_cors import CORS
from flask_restful import Resource, Api
from flask_restful import reqparse
import requests
import random
import string


app = Flask(__name__)

CORS(app)
api = Api(app)
gim_url = "http://localhost:9090"


def get_user_from_node_api(user, password, email):
    data = {
        "firstName": user,
        "lastName": password,
        "email": email
    }

    return requests.post(gim_url + '/api/v1/users', data=data)


class Login(Resource):

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument("email", type=str)
        parser.add_argument("firstName", type=str)
        parser.add_argument("lastName", type=str)

        args = parser.parse_args()

        gim_user = get_user_from_node_api(args.email, args.firstName, args.lastName)

        letters = ''.join(random.choice(string.ascii_lowercase) for i in range(20))

        if gim_user.status_code == 200 and gim_user.content != "null":
            return {"token": letters}
        else:
            return {"Ops! Credenciais erradas!"}


api.add_resource(Login, '/login')

if __name__ == '__main__':
    app.run()
