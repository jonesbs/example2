test:
	poetry run pytest exercise

lint:
	poetry run pre-commit

prepare:
	poetry shell
	cp local.env .env
	poetry install
	poetry run python exercise/manage.py migrate

local-run:
	poetry run python exercise/manage.py runserver 0.0.0.0:8000

import:
	poetry run python exercise/manage.py import_csv movielist.csv

reset:
	poetry run python exercise/manage.py reset_db
	poetry run python exercise/manage.py migrate
