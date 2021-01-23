runserver:
		pipenv run ./manage.py runserver

check:
		pipenv run ./manage.py check

migrations:
		pipenv run ./manage.py makemigrations

migrate:
		pipenv run ./manage.py migrate

shell:
		pipenv run ./manage.py shell

test:
		@echo "Not Implemented"

format:
		pipenv run isort . 
		pipenv run black .
		
lint:
		pipenv run pylint ./apps
