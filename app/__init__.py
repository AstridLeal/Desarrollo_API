from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

from app.resources import initialize_routes
initialize_routes(api)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the API!"})

@app.errorhandler(404)
def resource_not_found(e):
    return {"error": "Resource not found"}, 404

@app.errorhandler(500)
def internal_server_error(e):
    return {"error": "Internal server error"}, 500