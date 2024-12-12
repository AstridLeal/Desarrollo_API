from flask_restful import Api
from app.resources.user import UserResource

def initialize_routes(api):
    api.add_resource(UserResource, '/users', '/users/<int:user_id>')