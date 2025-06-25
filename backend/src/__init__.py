from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from .config import Config

db = SQLAlchemy()
jwt = JWTManager()

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(Config)

    if test_config:
        app.config.update(test_config)

    db.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        from .routes.user_route import user_bp
        from .routes.receita_route import receita_bp
        from .routes.ingrediente_route import ingrediente_bp 
        from .routes.planejamento_sema_route import planejamento_bp 
        from .routes.dashboard_route import dashboard_bp

        app.register_blueprint(user_bp)
        app.register_blueprint(receita_bp)
        app.register_blueprint(ingrediente_bp)
        app.register_blueprint(planejamento_bp)
        app.register_blueprint(dashboard_bp)

        db.create_all()

    return app
