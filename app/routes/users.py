from flask import Blueprint, jsonify
from app.models import db, User

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('', methods=['GET'])
def get_users():
    users = User.query.all()
    result = [{"id": user.id, "name": user.name, "email": user.email} for user in users]
    return jsonify(result)