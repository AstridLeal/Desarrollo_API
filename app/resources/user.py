from flask import request
from flask_restful import Resource
from app.models import db, User

class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return {"id": user.id, "username": user.username, "email": user.email}
    
    def post(self):
        data = request.get_json()
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return {"message": "User created successfully"}, 201