from flask import Blueprint, jsonify, request
from app.models import db, Highlight, User

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
        "user": {
            "id": h.user.id,
            "name": h.user.name
        }
    } for h in highlights]
    return jsonify(result)

@highlights_bp.route('', methods=['POST'])
def create_highlights():
    data = request.json

    if 'user_id' not in data:
        return jsonify({"error": "user_id is required"}), 400

    user = User.query.get(data['user_id'])
    if not user:
        return jsonify({"error": "User not found"}), 404

    if 'text' not in data or not data['text'].strip():
        return jsonify({"error": "text is required"}), 400

    highlight = Highlight(
        text=data['text'],
        source_url=data.get('source_url'),
        page_title=data.get('page_title'),
        user_id=data['user_id']
    )

    db.session.add(highlight)
    db.session.commit()
    return jsonify({
        "id": highlight.id,
        "text": highlight.text,
        "source_url": highlight.source_url,
        "page_title": highlight.page_title,
        "created_at": highlight.created_at.isoformat(),
        "user_id": highlight.user_id,
        "user": {
            "id": highlight.user.id,
            "name": highlight.user.name
        }
    }), 201