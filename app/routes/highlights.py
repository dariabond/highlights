from flask import Blueprint, jsonify, request
from app.models import db, Highlight

highlights_bp = Blueprint('highlights', __name__, url_prefix='/highlights')

@highlights_bp.route('', methods=['GET'])
def get_highlights():
    user_id = request.args.get('user_id', type=int)

    highlights = Highlight.query.filter_by(user_id=user_id).all()

    result = [{
        "id": h.id,
        "text": h.text,
        "source_url": h.source_url,
        "page_title": h.page_title,
        "created_at": h.created_at.isoformat(),
        "user_id": h.user_id,
        "user": {
            "id": h.user.id,
            "username": h.user.username
        }
    } for h in highlights]
    return jsonify(result)