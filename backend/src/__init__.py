from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from .routes.user_route import user_bp
        from .routes.venda_route import venda_bp

        app.register_blueprint(user_bp)
        app.register_blueprint(venda_bp)

        db.create_all()

    return app
