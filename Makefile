BASE_TAG=$(shell git rev-parse --short HEAD)

DB_TAG=postgres:9.6.5-alpine
REDIS_TAG=redis:3.2.10-alpine

WORK_DIR=/hello-django
DB_PORT=5432
REDIS_PORT=3000
APP_PORT=8000

DJANGO_IMAGE_NAME=hello-django/team2
DB_IMAGE_NAME=hellodjango/team2-db
REDIS_IMAGE_NAME=hellodjango/team2-redis

DJANGO_CONT_NAME=team2-django-cont
DB_CONT_NAME=team2-db-cont
REDIS_CONT_NAME=team2-redis-cont

BUILD_APP_ARGS=--build-arg IMAGE_NAME=$(DJANGO_IMAGE_NAME) --build-arg WORK_DIR=$(WORK_DIR) --build-arg PORT=$(APP_PORT)
BUILD_DB_ARGS=--build-arg IMAGE_NAME=$(DB_TAG) --build-arg PORT=$(DB_PORT)
BUILD_REDIS_ARGS=--build-arg IMAGE_NAME=$(REDIS_TAG) --build-arg PORT=$(REDIS_PORT)

#Building django images
django-images:
	@echo ":::Building Django Image"
	docker build --rm -f Django.Dockerfile $(BUILD_APP_ARGS) -t $(DJANGO_IMAGE_NAME):$(BASE_TAG) .

#Building all dependent images.
dep-images:
	@echo ":::Building Dependent Images"
	docker build --rm -f DB.Dockerfile $(BUILD_DB_ARGS) -t $(DB_IMAGE_NAME) .
	docker build --rm -f Redis.Dockerfile $(BUILD_REDIS_ARGS) -t $(REDIS_IMAGE_NAME) .	

dep-cont:
	@echo ":::Running dependents container"
	docker run -d -p 5433:5432 -v /var/lib/postgresql/data -v $(shell pwd)/database.sql:/docker-entrypoint-initdb.d/database.sql --env POSTGRES_USER=postgres --env POSTGRES_DBNAME=team2 --env POSTGRES_PASSWORD=mypass --env POSTGRES_PORT=5432 --name $(DB_CONT_NAME) $(DB_IMAGE_NAME)
	docker run -d -p 3000:3000 --name $(REDIS_CONT_NAME) $(REDIS_IMAGE_NAME)

app-cont:
	@echo ":::Running django app container"
	docker run -d -p 8000:8000 --link $(DB_CONT_NAME):db --link $(REDIS_CONT_NAME):redis --name $(DJANGO_CONT_NAME) $(DJANGO_IMAGE_NAME):$(BASE_TAG)

#Remove all dependent containers
remove-dep-cont:
	@echo ":::remove db container"
	-docker stop ${DB_CONT_NAME}
	-docker rm ${DB_CONT_NAME}
	@echo ":::remove redis container"
	-docker stop ${REDIS_CONT_NAME}
	-docker rm ${REDIS_CONT_NAME}
	-docker volume ls -qf dangling=true | xargs docker volume rm

remove-app-cont:
	@echo ":::remove app container"
	-docker stop ${DJANGO_CONT_NAME}
	-docker rm ${DJANGO_CONT_NAME}

remove-app-image:
	@echo ":::remove app image"
	-docker rmi $(DJANGO_IMAGE_NAME):$(BASE_TAG)

dep-up: dep-images dep-cont

app-up: django-images app-cont

app-logs:
	@echo ":::app logs"
	docker logs -f $(DJANGO_CONT_NAME)


build: remove-dep-cont remove-app-cont remove-app-image dep-up app-up
run-development: app-logs
