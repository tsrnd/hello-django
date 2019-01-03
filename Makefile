run:
	pipenv run python manage.py runserver 0.0.0.0:8000

up:
	pipenv lock --requirements > requirements.txt
	docker-compose up --build

up-data:
	docker-compose up -d data

up-app:
	docker-compose up --build app

down:
	docker-compose down

clean:
	docker ps -aq -f status=exited | xargs docker rm
	docker images -q --filter dangling=true | xargs docker rmi

migrate:
	pipenv run python manage.py migrate

test:
	pipenv run pytest

load-images:
	if [[ -d "$$HOME/.docker/images" ]]; then \
  	find "$$HOME/.docker/images" -name "*.tar.gz" | xargs -I {file} sh -c "zcat < {file} | docker load"; \
	fi

save-images:
	mkdir -p "$$HOME/.docker/images"
	docker images -a --filter='dangling=false' --format '{{.Repository}}:{{.Tag}} {{.ID}}' \
  	| xargs -n 2 -t sh -c 'test -e $$HOME/.docker/images/$$1.tar.gz || docker save $$0 | gzip -2 > $$HOME/.docker/images/$$1.tar.gz';
