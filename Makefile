# main commands

install:
	@if ! [[ -f '.env' ]]; then \
		cp .env.example .env; \
	fi
	@pipenv install -d

start:
	@make build
	@docker-compose up -d app
	@docker-compose logs -f app || true

stop:
	@docker-compose stop

test:
	@rm -rf ./.tmp/pytest
	@make build
	@docker-compose run app pytest

# additional commands

lock:
	@pipenv lock -r > requirements.txt
	@pipenv lock -d -r > requirements-dev.txt

build:
	@make lock
	@make migrations
	@docker-compose build app

up-data:
	@make load-env
	@docker-compose up -d data cache
	@bash ./scripts/wait-data.sh

up-app:
	@make build
	@docker-compose up -d app
	@docker-compose logs -f app

clean:
	@docker-compose down
	@docker ps -aq -f status=exited | xargs docker rm
	@docker images -q -f dangling=true | xargs docker rmi
	@find . -name "__pycache__" | xargs rm -rf

clean-data:
	@rm -rf ./.tmp/data

migrations:
	@make up-data
	@pipenv run python manage.py makemigrations

lint:
	@make build
	@docker-compose run app pylint myproject myapp

load-env:
	@export $$(cat .env | xargs echo)
