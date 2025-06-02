from flask import Blueprint, jsonify
from .models import db, User

main = Blueprint('main', __name__)

@main.route('/api/test', methods=['GET'])
def test_route():
    return jsonify({
        'status': 'success',
        'message': 'Hello from the Flask test route!'
    })

@main.route('/', methods=['GET'])
def index():
    return jsonify({
        'status': 'success',
        'message': 'Welcome to the Highlight API',
        'test_endpoint': '/api/test'
    })

@main.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    result = [{"id": user.id, "name": user.name, "email": user.email} for user in users]
    return jsonify(result)
