from flask import Blueprint, jsonify
from app.models import db, Highlight

highlights_bp = Blueprint('highlights', __name__, url_prefix='/highlights')