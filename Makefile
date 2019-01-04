install:
	@if ! [[ -f '.env' ]]; then \
		cp .env.example .env; \
	fi
	@pipenv install -d

up:
	@make build
	@docker-compose up -d app
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

load-images:
	@if [[ -d "$$HOME/.docker/images" ]]; then \
  	find "$$HOME/.docker/images" -name "*.tar.gz" | xargs -I {file} sh -c "zcat < {file} | docker load"; \
	fi

save-images:
	@mkdir -p "$$HOME/.docker/images"
	@docker images -a -f dangling=false --format '{{.Repository}}:{{.Tag}} {{.ID}}' \
  	| xargs -n 2 -t sh -c 'test -e $$HOME/.docker/images/$$1.tar.gz || docker save $$0 | gzip -2 > $$HOME/.docker/images/$$1.tar.gz';
