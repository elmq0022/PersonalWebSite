runserver:
		pipenv run ./manage.py runserver

check:
		pipenv run ./manage.py check

makemigrations:
		pipenv run ./manage.py makemigrations

migrate:
		pipenv run ./manage.py migrate

shell:
		pipenv run ./manage.py shell

test:
		@echo "Not Implemented"

format:
		pipenv run isort -rc -tc --atomic .	
		@echo "Black Not Implemented"
		
lint:
		pipenv run pylint .
