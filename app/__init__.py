from flask import Flask
from flask_migrate import Migrate
from .config import Config
from .models import db, User, Highlight
from app.routes.users import users_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)

    app.register_blueprint(users_bp)
    
    return app