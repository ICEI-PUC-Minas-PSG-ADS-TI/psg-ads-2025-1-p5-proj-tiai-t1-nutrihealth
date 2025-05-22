#!/bin/bash
set -e

export FLASK_APP=run.py
export FLASK_ENV=development

echo "⏳ Aguardando o banco de dados ficar disponível..."
while ! nc -z db 5432; do
  sleep 1
done
echo "✅ Banco de dados disponível!"

echo "🚀 Rodando migrações..."
flask db upgrade

echo "🟢 Iniciando aplicação..."
exec flask run --host=0.0.0.0
