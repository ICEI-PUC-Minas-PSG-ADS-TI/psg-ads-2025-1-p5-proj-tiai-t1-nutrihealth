import pytest
import os
from src import create_app, db
from src.models.user_model import User
from src.models.receita_model import Receita
from src.models.ingrediente_model import Ingrediente
from src.models.planejamento_sema_model import PlanejamentoSemanal

@pytest.fixture(scope="module")
def test_app():
    app = create_app(test_config={
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "TESTING": True,
        "SECRET_KEY": "chave-secreta-de-teste",
        "JWT_SECRET_KEY": "chave-secreta-jwt-de-teste"
    })
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture(scope="function")
def client(test_app):
    return test_app.test_client()

@pytest.fixture(scope="function")
def init_database(test_app):
    with test_app.app_context():
        db.drop_all()
        db.create_all()
        db.session.commit()
    return db

@pytest.fixture(scope="function")
def auth_headers(client, init_database):
    with client.application.app_context():
        user = User(name="Test User", email="test@example.com", tipo="Cliente")
        user.set_password("password123")
        db.session.add(user)
        db.session.commit()

    login_data = {"email": "test@example.com", "password": "password123"}
    response = client.post("/auth/login", json=login_data)
    token = response.json["access_token"]
    return {"Authorization": f"Bearer {token}"}

@pytest.fixture(scope="function")
def create_test_recipe(client, auth_headers):
    with client.application.app_context():
        ing_data = {
            "nome": "Tomate",
            "quantidade": 200,
            "unidade_de_medida": "g",
            "impacto_ambiental": "Baixo"
        }
        ing_response = client.post("/ingredientes", json=ing_data, headers=auth_headers)
        ingrediente_id = ing_response.json["id"]

        recipe_data = {
            "nome": "Salada de Tomate",
            "descricao": "Uma salada simples e refrescante.",
            "tempo_preparo": "00:15",
            "modo_preparo": "Fatie os tomates e tempere.",
            "impacto_ambiental": "Baixo",
            "tipo_dieta": "Vegana",
            "tipo_refeicao": "Almoço",
            "estilo_preparo": "Cru",
            "ingredientes": [{"id": ingrediente_id}]
        }
        response = client.post("/recipes", json=recipe_data, headers=auth_headers)
        return response.json["id"], recipe_data
