until nc -w 1 postgres 5432; do sleep 0.1; done
poetry run alembic upgrade head
poetry run task start
