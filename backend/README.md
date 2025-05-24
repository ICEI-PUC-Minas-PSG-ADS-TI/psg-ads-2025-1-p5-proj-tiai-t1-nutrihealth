# Nutrihealth API

Este projeto é uma API RESTful desenvolvida com [Flask](https://flask.palletsprojects.com/), utilizando [Docker](https://www.docker.com/) para conteinerização e [PostgreSQL](https://www.postgresql.org/) como banco de dados relacional. Usada pelo frontend do nutrihealth para consulta dos dados no banco de dados.

---

## Estrutura do Projeto

```
.
├── db/
│   ├── modelofisico.sql
│   └── README.md
├── src/
|   |-- models/
|   |   |-- user_model.py
|   │   └── vendas_model.py
|   |-- routes/
|   |   |-- user_route.py
|   │   └── vendas_route.py
│   ├── __init__.py
│   └── config.py
├── .env
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── app.py
```

---

## ⚙️ Tecnologias

- Python 3.13+
- Flask
- SQLAlchemy
- PostgreSQL
- Docker / Docker Compose
- dotenv
- psycopg2-binary

---

## Como Executar

### Pré-requisitos

- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/)

### 1. Clone o repositório

```bash
git clone https://github.com/ICEI-PUC-Minas-PSG-ADS-TI/psg-ads-2025-1-p5-proj-tiai-t1-nutrihealth.git
cd psg-ads-2025-1-p5-proj-tiai-t1-nutrihealth
```

### 2. Crie o arquivo `.env`

```env
FLASK_DEBUG=0 or 1 to active debug
FLASK_ENV=development or production
DATABASE_URL=postgresql://<user>:<password>@db:5432/<database>
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
```

### 3. Suba os containers

```bash
docker-compose up --build
```

> A API estará disponível em: http://localhost:5000

**Se não for a primeira vez rodando o projeto, siga esses passos:**

Se **qualquer um dos arquivos abaixo for modificado**:

- `Dockerfile`
- `docker-compose.yml`
- `requirements.txt`
- `.env`
- `app.py`

Execute:

```bash
docker-compose up --build
```

> Isso garante que todas as dependências e configurações sejam atualizadas corretamente.


Se **apenas arquivos dentro da pasta `src/`** forem modificados, basta rodar:

```bash
docker-compose up
```

> Isso é mais rápido e mantém os containers existentes.

---

## Rodar Testes

```bash
docker-compose exec web pytest
```

---

## 📬 Principais Endpoints

| Método | Rota           | Descrição                  |
|--------|----------------|----------------------------|
| GET    | /test   | Verifica se a API está online |
| GET    | /users         | Lista todos os usuários    |
| POST   | /users         | Cria um novo usuário       |
| GET    | /vendas   | Lista todas as vendas|
| POST   | /vendas         | Cria uma nova venda       |
| PUT    | /vendas/<id>    | Atualiza uma venda     |
| DELETE | /users/<id>    | Remove uma venda         |

---

## Docker Compose

```yaml
version: "3.8"

services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/app
    depends_on:
      - db
    environment:
      - FLASK_ENV=${FLASK_ENV}
      - DATABASE_URL=${DATABASE_URL}

  db:
    image: postgres:15
    restart: always
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - pgdata:/var/lib/postgresql/data
    ports:
      - "5433:5432"

volumes:
  pgdata:
```

---

## Notas de Desenvolvimento

- Variáveis sensíveis são armazenadas no `.env`
- Código organizado com Blueprints para facilitar expansão

---

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## Autor
Feito por:
- [Guilherme](https://github.com/guilhermehbs).
- [Yago]().
