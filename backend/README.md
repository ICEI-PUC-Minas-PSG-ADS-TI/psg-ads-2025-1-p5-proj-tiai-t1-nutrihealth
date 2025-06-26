# Nutrihealth API

Este projeto é uma API RESTful desenvolvida com [Flask](https://flask.palletsprojects.com/), utilizando [PostgreSQL](https://www.postgresql.org/) como banco de dados relacional. Ela é utilizada pelo frontend do Nutrihealth para gerenciar dados como usuários, receitas, ingredientes e planejamento de refeições.

---

## Estrutura do Projeto

```
nutrihealth/
├── backend/
│ ├── .env
│ ├── app.py
│ ├── config.py
│ ├── requirements.txt
│ ├── Dockerfile
│ ├── docker-compose.yml
│ ├── README.md
│ ├── db/
│ │ ├── modelofisico.sql
│ │ └── README.md
│ └── src/
│ ├── init.py
│ ├── config.py
│ ├── models/
│ │ ├── user_model.py
│ │ └── vendas_model.py
│ └── routes/
│ ├── user_route.py
│ └── vendas_route.py
│
├── docs/
│ ├── apresentacao/
│ │ ├── 1-Contexto.md
│ │ ├── 2-Planejamento-Projeto.md
│ │ ├── 3-Especificação.md
│ │ ├── 4-Projeto-Solucao.md
│ │ ├── 5-Interface-Sistema.md
│ │ ├── 6-Conclusão.md
│ │ └── 7-Referências.md
│ └── images/
│
├── frontend/
│ ├── Criar-receita/
│ │ ├── index.html
│ │ ├── script.js
│ │ └── style.css
│ ├── Lista-de-itens/
│ │ ├── index.html
│ │ ├── script.js
│ │ └── style.css
│ ├── Login-e-registro/
│ │ ├── index.html
│ │ ├── script.js
│ │ └── style.css
│ ├── Planejamento-Semanal/
│ │ ├── index.html
│ │ ├── script.js
│ │ └── style.css
│ ├── Receitas-salvas/
│ │ ├── index.html
│ │ ├── script.js
│ │ └── style.css
│ ├── Relatorio-mensal/
│ │ ├── index.html
│ │ ├── script.js
│ │ └── style.css
│ ├── Tela-de-Perfil/
│ │ ├── index.html
│ │ ├── script.js
│ │ └── style.css
│ ├── Tela-inicial/
│ │ ├── index.html
│ │ ├── perfil.png
│ │ ├── script.js
│ │ └── style.css
│ └── Tela-Receita-Detalhada/
│ ├── index.html
│ ├── script.js
│ └── style.css
│
├── venv/
│ └── ...
├── .gitattributes
├── .gitignore
├── CITATION.cff
└── README.md
```

---

## Tecnologias

- Python 3.13+
- Flask
- SQLAlchemy
- PostgreSQL
- psycopg2-binary
- python-dotenv
- pytest

---

## Como Executar

### 1. Pré-requisitos

- Python 3.13+
- PostgreSQL
- Criar um banco de dados e usuário no PostgreSQL

### 2. Clone o repositório

```bash
git clone https://github.com/ICEI-PUC-Minas-PSG-ADS-TI/psg-ads-2025-1-p5-proj-tiai-t1-nutrihealth.git
cd psg-ads-2025-1-p5-proj-tiai-t1-nutrihealth/backend
```

3. Crie e ative um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

4. Instale as dependências

```bash
pip install -r requirements.txt
```

5. Configure o arquivo .env

Crie um arquivo .env na raiz do backend com:

```bash
FLASK_DEBUG=1  
FLASK_ENV=development  
DATABASE_URL=postgresql://<usuario>:<senha>@<host>:<porta>/<database>
```

6. Execute o script de criação do banco de dados

Utilize ferramentas como PgAdmin ou DBeaver para criar o banco de dados *nutrihealth_db*.

```bash
CREATE DATABASE IF NOT EXISTS nutrihealth_db
```

7. Rode a aplicação

Dentro da pasta backend, rode:

```bash
python app.py
```

> A API estará disponível em http://localhost:5000.

## Testes

Execute os testes com:

```bash
pytest
```

## Endpoints Principais

| Método | Rota                          | Descrição                        |
|--------|-------------------------------|----------------------------------|
| POST   | /auth/register                | Registra novo usuário            |
| POST   | /auth/login                   | Realiza login                    |
| GET    | /profile                      | Dados do usuário logado          |
| GET    | /users                        | Lista usuários                   |
| PUT    | /users/<id>                   | Atualiza usuário                 |
| DELETE | /users/<id>                   | Deleta usuário                   |
| POST   | /ingredientes                 | Cria ingrediente                 |
| GET    | /ingredientes                 | Lista ingredientes               |
| POST   | /recipes                      | Cria receita                     |
| GET    | /recipes                      | Lista receitas                   |
| GET    | /recipes/<id>                 | Detalhes da receita              |
| POST   | /recipes/save/<id>            | Salva receita                    |
| GET    | /profile/saved_recipes        | Receitas salvas                  |
| GET    | /relatorio/mensal             | Relatório mensal                 |
| GET    | /relatorio/semanal            | Relatório semanal                |
| POST   | /planejamento                 | Cria/atualiza planejamento       |
| GET    | /planejamento                 | Retorna planejamento semanal     |

---

## Notas de Desenvolvimento

- Arquitetura modular com models e routes separados
- Variáveis sensíveis isoladas via .env
- Organização em Blueprints para fácil manutenção

---

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## Autor
Feito por:
- [Guilherme](https://github.com/guilhermehbs)
- [Yago](https://github.com/yago-henrique29)
- [Luan](https://github.com/luanpabloj)
- [Gabriel](https://github.com/Gachaves)
- [Vitor](https://github.com/vitorxav)
