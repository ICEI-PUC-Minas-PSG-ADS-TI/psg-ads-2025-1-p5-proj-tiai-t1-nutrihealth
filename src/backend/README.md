# Flask API com PostgreSQL e Docker

Este projeto é uma API RESTful em Flask conectada a um banco PostgreSQL, dockerizada para facilitar o desenvolvimento e a implantação.

---

## Como rodar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

### 2. Criar arquivo .env

Na raiz do projeto, crie um arquivo .env com as variáveis de ambiente necessárias:

```bash
DATABASE_URL=postgresql://myuser:mypass@db:5432/mydb
FLASK_ENV=development
FLASK_APP=run.py
```

> Importante:
>
>   myuser, mypass, mydb devem ser iguais aos configurados no docker-compose.yml.
>
>   O host do banco é db (nome do serviço do PostgreSQL no Docker Compose).

### 3. Subir os containers com Docker Compose
```bash
docker-compose up --build
```

Esse comando irá:
- Construir a imagem Docker da API.

- Subir o container do PostgreSQL.

- Aguardar o banco ficar disponível.

- Aplicar automaticamente as migrations no banco.

- Iniciar a aplicação Flask.

## Acesso à API

Após subir, a API estará disponível em:

```bash
http://localhost:5000/
```

Exemplo de endpoint:

```bash
GET http://localhost:5000/api/users
```

## Desenvolvimento

- O código local está mapeado para o container, ou seja, alterações feitas no seu editor são refletidas na API sem rebuild (hot reload).

- Para aplicar alterações no banco de dados, gere novas migrations com:

```bash
docker-compose exec web flask db migrate -m "mensagem da migration"
docker-compose exec web flask db upgrade
```

## Sobre as migrations

- Toda vez que o container da API iniciar, ele executa flask db upgrade para garantir que o banco está atualizado.

- Se não houver migrations novas, nada será alterado.

- As migrations ficam na pasta migrations/.

## Estrutura principal do projeto

```bash
/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes/
│   │   └── user_routes.py
├── migrations/
├── .env
├── Dockerfile
├── docker-compose.yml
├── entrypoint.sh
├── requirements.txt
└── run.py
```

## Dicas importantes

Permissão do entrypoint.sh:

- No Linux/macOS, rode localmente:

```bash
chmod +x entrypoint.sh
```

> Se estiver no Windows e não puder, o Dockerfile já configura permissão.

- Atualização do código:
Sempre que fizer pull do GitHub, rode:

```bash
docker-compose up --build
para reconstruir a imagem com as últimas mudanças.
```

## Problemas comuns

- Erro de conexão com o banco: \
Verifique se o serviço db está rodando e se o DATABASE_URL está correto no .env.

- Porta 5000 ocupada: \
Mude a porta no docker-compose.yml em ports: para outra disponível.