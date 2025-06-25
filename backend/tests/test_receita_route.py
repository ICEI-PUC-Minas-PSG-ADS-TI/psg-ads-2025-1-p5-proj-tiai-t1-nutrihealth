from tests.conftest import client, auth_headers, create_test_recipe
from src.models.receita_model import Receita, receitas_salvas
from src.models.user_model import User
from src import db
import pytest

def test_create_recipe_success(client, auth_headers):
    with client.application.app_context():
        ing_data = {
            "nome": "Cenoura", "quantidade": 150, "unidade_de_medida": "g", "impacto_ambiental": "Baixo"
        }
        ing_response = client.post("/ingredientes", json=ing_data, headers=auth_headers)
        ingrediente_id = ing_response.json["id"]
    
    recipe_data = {
        "nome": "Sopa de Cenoura",
        "descricao": "Uma sopa deliciosa.",
        "tempo_preparo": "00:30",
        "modo_preparo": "Cozinhe a cenoura e bata no liquidificador.",
        "impacto_ambiental": "Baixo",
        "tipo_dieta": "Vegetariana",
        "tipo_refeicao": "Almoço",
        "estilo_preparo": "Cozinhado",
        "ingredientes": [{"id": ingrediente_id}]
    }
    response = client.post("/recipes", json=recipe_data, headers=auth_headers)
    assert response.status_code == 201
    assert "id" in response.json
    with client.application.app_context():
        recipe = Receita.query.filter_by(nome="Sopa de Cenoura").first()
        assert recipe is not None
        assert len(recipe.ingredientes) == 1

def test_create_recipe_missing_data(client, auth_headers):
    recipe_data = {"nome": "Receita Incompleta"}
    response = client.post("/recipes", json=recipe_data, headers=auth_headers)
    assert response.status_code == 400
    assert "error" in response.json

def test_get_all_recipes(client, create_test_recipe):
    response = client.get("/recipes")
    assert response.status_code == 200
    assert len(response.json) >= 1
    assert "nome" in response.json[0]

def test_get_recipe_details_success(client, create_test_recipe):
    recipe_id, recipe_data = create_test_recipe
    response = client.get(f"/recipes/{recipe_id}")
    assert response.status_code == 200
    assert response.json["nome"] == recipe_data["nome"]
    assert "ingredientes" in response.json
    assert len(response.json["ingredientes"]) == 1

def test_get_recipe_details_not_found(client):
    response = client.get("/recipes/999")
    assert response.status_code == 404
    assert "error" in response.json

def test_save_recipe(client, auth_headers, create_test_recipe):
    recipe_id, _ = create_test_recipe
    response = client.post(f"/recipes/save/{recipe_id}", headers=auth_headers)
    assert response.status_code == 201
    assert "message" in response.json
    with client.application.app_context():
        # Corrigido o acesso ao objeto de usuário
        user = db.session.query(User).filter_by(email="test@example.com").first()
        assert user is not None
        assert len(user.receitas_salvas) == 1
        assert user.receitas_salvas[0].id == recipe_id

def test_get_saved_recipes(client, auth_headers, create_test_recipe):
    recipe_id, recipe_data = create_test_recipe
    client.post(f"/recipes/save/{recipe_id}", headers=auth_headers)
    response = client.get("/profile/saved_recipes", headers=auth_headers)
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]["id"] == recipe_id

def test_delete_recipe(client, auth_headers, create_test_recipe):
    recipe_id, _ = create_test_recipe
    response = client.delete(f"/recipes/{recipe_id}")
    assert response.status_code == 200
    assert "message" in response.json
    with client.application.app_context():
        deleted_recipe = Receita.query.get(recipe_id)
        assert deleted_recipe is None
