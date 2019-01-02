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

test:
	pipenv run pytest
