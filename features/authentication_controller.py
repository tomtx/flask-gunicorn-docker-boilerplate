from flask import request
from flask_restplus import Resource

from features.api_blueprint import api

ns = api.namespace('authentication', path='/authentication', description='user authentication')


@ns.route('/token')
class Token(Resource):
    @api.response(201, "access token has been successfully created")
    @api.response(400, "bad request")
    @api.response(401, "unauthorized - access denied due to wrong user login credentials")
    def post(self):
        """
        placeholder for creating an access token
        """
        return {"access_token": "Hello Python Web App!"}, 201
