run:
	@echo '[Local] start app'
	export DATABASE_URL='postgres://hello:django@localhost:5432/default'
	pipenv run python manage.py runserver 0.0.0.0:8000

run-docker:
	@echo '[Docker] start data service'
	docker-compose up -d data
	$(MAKE) clean
	@echo '[Docker] rebuild & start app service'
	pipenv lock --requirements > requirements.txt
	docker-compose up --build app

clean:
	@echo '[Docker] clean up exited containers'
	docker ps -aq -f status=exited | xargs docker rm
	@echo '[Docker] clean up danging images'
	docker images -q --filter dangling=true | xargs docker rmi
