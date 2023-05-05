#!/usr/bin/env bash

if [ -z $1 ]; then
    echo "Please provide a revision message"
    exit 1
fi

echo "This will delete all postgres data."
read -p "Are you sure? Cancel for no, return for yes." -n 1 -r
docker-compose down
docker-compose -f docker-compose.dev.yml up -d
echo "Waiting for start..."
until nc -w 10 127.0.0.1 5432; do sleep 1; done
export DB_URI=postgresql://postgres:postgres@localhost:5432/bot
sudo rm -rf pg_data/
python -m alembic upgrade head
python -m alembic revision --autogenerate -m "$*"
unset DB_URI
docker-compose down
