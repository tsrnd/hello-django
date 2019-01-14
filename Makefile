install:
	@if ! [[ -f '.env' ]]; then \
		cp .env.example .env; \
	fi
	@pipenv install -d

up:
	@make build
	@docker-compose up -d app
	@docker-compose up -d vuejs
	@docker-compose logs -f app

lock:
	@pipenv lock -r > requirements.txt
	@pipenv lock -d -r > requirements-dev.txt

build:
	@make lock
	@make migrations
	@docker-compose build app

up-data:
	@docker-compose up -d data cache
	@sleep 3

up-app:
	@make build
	@docker-compose up -d app
	@docker-compose logs -f app

down:
	@docker-compose down

clean:
	@docker ps -aq -f status=exited | xargs docker rm
	@docker images -q -f dangling=true | xargs docker rmi
	@find . -name "__pycache__" | xargs rm -rf

migrations:
	@make up-data
	@pipenv run python manage.py makemigrations

test:
	@make build
	@docker-compose run app pytest

lint:
	@make build
	@docker-compose run app pylint myproject myapp
