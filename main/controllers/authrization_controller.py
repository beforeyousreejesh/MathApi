from flask import request, Response,jsonify
from flask_restx import Resource,Namespace

from ..service.auth_service import login, validate

login_api=Namespace("Authentication","Authentication")

@login_api.route('/login/<authenticationToken>')
@login_api.param('authenticationToken','token for authentication')
class Login(Resource):
    @login_api.response(200,'Success')
    @login_api.response(401,'Unauthorized')
    @login_api.response(500,'Internal Server Error')
    def get(self,authenticationToken):

        if authenticationToken is None or len(authenticationToken)==0:
            return Response('Invalid token',401)
        try:
           token= login(authenticationToken)
           response_o={
            'status':'Success',
            'message':'you have logged in successfully',
            'Authorization':token.decode()
           }

           return response_o, 200
        except Exception as e:
            return str(e), 500
