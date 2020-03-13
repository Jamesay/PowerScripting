from flask import Blueprint
from flask_restful import Api
from resources.Index import Index, Welcome

api_bp = Blueprint('api', __name__) # creates a Blueprint which we'll register to the app later
api = Api(api_bp)

# Route
api.add_resource(Index, '/index')
api.add_resource(Welcome, '/')