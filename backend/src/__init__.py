from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from .config import Config

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        from .routes.user_route import user_bp
        from .routes.receita_route import receita_bp
<<<<<<< Updated upstream
        from .routes.dashboard_route import relatorio_bp

        app.register_blueprint(user_bp)
        app.register_blueprint(receita_bp)
        app.register_blueprint(relatorio_bp)
=======
        from .routes.ingrediente_route import ingrediente_bp 

        app.register_blueprint(user_bp)
        app.register_blueprint(receita_bp)
        app.register_blueprint(ingrediente_bp)
>>>>>>> Stashed changes

        db.create_all()

    return app
