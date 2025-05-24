# Flask API com PostgreSQL e Docker

Este projeto é uma API RESTful em Flask conectada a um banco PostgreSQL, dockerizada para facilitar o desenvolvimento e a implantação.

---

## Como rodar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/ICEI-PUC-Minas-PSG-ADS-TI/psg-ads-2025-1-p5-proj-tiai-t1-nutrihealth.git
cd psg-ads-2025-1-p5-proj-tiai-t1-nutrihealth
```

### 2. Criar arquivo .env

Na raiz do projeto, crie um arquivo .env com as variáveis de ambiente necessárias:

```bash
DATABASE_URL=postgresql://myuser:mypass@db:5432/mydb
FLASK_DEBUG=0
FLASK_ENV=development
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

**Ao fazer uma alteração nos aquivos app.py, Dockerfile, requirements.txt ou docker-compose.yml, rode o seguinte comando no terminal:**
```bash
docker-compose up --build
```

**Se quiser apenas rodar o codigo sem ter feito nenhuma alteração nesses arquivos, ou se a alteração foi apenas nos arquivos dentro de src, rode:**
```bash
docker-compose up
```

## Acesso à API

Após subir, a API estará disponível em:

```bash
http://localhost:5000/
```

Exemplo de endpoint:

```bash
GET http://localhost:5000/test
```

## Estrutura principal do projeto

```bash
/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── config.py
├── .env
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── app.py
```

## Problemas comuns

- Erro de conexão com o banco: \
Verifique se o serviço db está rodando e se o DATABASE_URL está correto no .env.

- Porta 5000 ocupada: \
Mude a porta no docker-compose.yml em ports: para outra disponível.