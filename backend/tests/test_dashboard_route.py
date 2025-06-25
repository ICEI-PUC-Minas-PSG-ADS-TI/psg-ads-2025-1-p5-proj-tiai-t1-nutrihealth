from tests.conftest import client, auth_headers
import pytest

def test_get_monthly_report(client, auth_headers):
    response = client.get("/relatorio/mensal", headers=auth_headers)
    assert response.status_code == 200
    assert "total_refeicoes" in response.json
    assert "dica_do_mes" in response.json

def test_get_weekly_report(client, auth_headers):
    response = client.get("/relatorio/semanal", headers=auth_headers)
    assert response.status_code == 200
    assert "total_refeicoes" in response.json
    assert "dica_da_semana" in response.json

def test_get_report_invalid_token(client):
    headers = {"Authorization": "Bearer invalid_token"}
    response = client.get("/relatorio/mensal", headers=headers)
    assert response.status_code == 422