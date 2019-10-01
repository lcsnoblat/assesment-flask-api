from flask import Flask, request
from flask_cors import CORS
from flask_restful import Resource, Api
from flask_restful import reqparse
import requests
import random
import string
import os
import json

app = Flask(__name__)

CORS(app)
api = Api(app)

gim_url = 'https://node-api-assesment.herokuapp.com'


def get_user_from_node_api(email, user, password):
    data = {
        "firstName": user,
        "password": password,
        "email": email
    }

    return requests.post(gim_url + '/api/v1/users', data=data)


class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument("email", type=str)
        parser.add_argument("firstName", type=str)
        parser.add_argument("password", type=str)
        parser.add_argument("nameStarWars", type=str)

        args = parser.parse_args()

        gim_user = get_user_from_node_api(args.email, args.firstName, args.password)

        letters = ''.join(random.choice(string.ascii_lowercase) for i in range(20))

        if gim_user.status_code == 200 and gim_user.json() != None:

            starwars = requests.get("https://swapi.co/api/people/?search=" + args.nameStarWars)

            return starwars.json()
        else:
            return {"message": "Credencial não cadastrada"}


api.add_resource(Login, '/login')


port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
    app.run()
