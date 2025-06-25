from tests.conftest import client, auth_headers
from src.models.ingrediente_model import Ingrediente
import pytest

def test_create_ingrediente_success(client, auth_headers):
    data = {"nome": "Alface", "quantidade": 1, "unidade_de_medida": "unidade", "impacto_ambiental": "Baixo"}
    response = client.post("/ingredientes", json=data, headers=auth_headers)
    assert response.status_code == 201
    assert "id" in response.json
    with client.application.app_context():
        ingrediente = Ingrediente.query.filter_by(nome="Alface").first()
        assert ingrediente is not None
        assert ingrediente.quantidade == 1

def test_create_ingrediente_missing_data(client, auth_headers):
    data = {"nome": "Alface"}
    response = client.post("/ingredientes", json=data, headers=auth_headers)
    assert response.status_code == 400
    assert "error" in response.json

def test_get_all_ingredientes(client, auth_headers):
    client.post("/ingredientes", json={"nome": "Cebola", "quantidade": 2, "unidade_de_medida": "unidade", "impacto_ambiental": "Médio"}, headers=auth_headers)
    response = client.get("/ingredientes", headers=auth_headers)
    assert response.status_code == 200
    assert len(response.json) >= 1
    assert response.json[0]["nome"] == "Cebola"

def test_get_ingrediente_details_success(client, auth_headers):
    create_response = client.post("/ingredientes", json={"nome": "Pimentão", "quantidade": 1, "unidade_de_medida": "unidade", "impacto_ambiental": "Baixo"}, headers=auth_headers)
    ingrediente_id = create_response.json["id"]
    response = client.get(f"/ingredientes/{ingrediente_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json["nome"] == "Pimentão"

def test_get_ingrediente_details_not_found(client, auth_headers):
    response = client.get("/ingredientes/999", headers=auth_headers)
    assert response.status_code == 404
    assert "error" in response.json

def test_update_ingrediente(client, auth_headers):
    create_response = client.post("/ingredientes", json={"nome": "Batata", "quantidade": 500, "unidade_de_medida": "g", "impacto_ambiental": "Baixo"}, headers=auth_headers)
    ingrediente_id = create_response.json["id"]
    update_data = {"quantidade": 600, "unidade_de_medida": "g"}
    response = client.put(f"/ingredientes/{ingrediente_id}", json=update_data, headers=auth_headers)
    assert response.status_code == 200
    assert "message" in response.json
    with client.application.app_context():
        updated_ing = Ingrediente.query.get(ingrediente_id)
        assert updated_ing.quantidade == 600

def test_delete_ingrediente(client, auth_headers):
    create_response = client.post("/ingredientes", json={"nome": "Cebola Roxa", "quantidade": 1, "unidade_de_medida": "unidade", "impacto_ambiental": "Baixo"}, headers=auth_headers)
    ingrediente_id = create_response.json["id"]
    response = client.delete(f"/ingredientes/{ingrediente_id}", headers=auth_headers)
    assert response.status_code == 200
    assert "message" in response.json
    with client.application.app_context():
        deleted_ing = Ingrediente.query.get(ingrediente_id)
        assert deleted_ing is None