from flask_restful import Resource

class Index(Resource):
    def get(self):
        return{"message": "Index page!"}

class Welcome(Resource):
    def get(self):
        return "Welcome to my test python restful API"