from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

# Extensões globais
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # Carregar variáveis de ambiente do .env
    load_dotenv()

    app = Flask(__name__)

    # Configurações do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar extensões
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar rotas
    from app.routes.user_routes import user_bp
    app.register_blueprint(user_bp, url_prefix="/api/users")

    return app
