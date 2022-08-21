from flask_restx import Api
from flask import Blueprint

from main.controllers.math_controller import maths_api
from main.controllers.authrization_controller import login_api

blueprint= Blueprint("api",__name__)

api = Api(
    blueprint,
    title='Maths api',
    version='1.0',
    description='An api for maths operations'
)

api.add_namespace(maths_api,'/api/math')
api.add_namespace(login_api,'/api/auth')