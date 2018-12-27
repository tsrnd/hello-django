# make build app_open_port={your port}

# get argument(port)
ifdef app_open_port
	APP_OPEN_PORT=-p $(app_open_port):8000
else
	APP_OPEN_PORT=
endif

DB_TAG=postgres:9.6.5-alpine
REDIS_TAG=redis:3.2.10-alpine

WORK_DIR=/hello-django
DB_PORT=5432
APP_PORT=8000
REDIS_PORT=6379

APP_IMAGE_NAME=team1/app:latest
DB_IMAGE_NAME=team1/db:latest
REDIS_IMAGE_NAME=team1/redis:latest

APP_CONT_NAME=app-team1-cont
DB_CONT_NAME=db-team1-cont
REDIS_CONT_NAME=redis-team1-cont

BUILD_APP_ARGS=--build-arg IMAGE_NAME=$(APP_IMAGE_NAME) --build-arg WORK_DIR=$(WORK_DIR) --build-arg PORT=$(APP_PORT)
BUILD_DB_ARGS=--build-arg IMAGE_NAME=$(DB_TAG) --build-arg PORT=$(DB_PORT)
BUILD_REDIS_ARGS=--build-arg IMAGE_NAME=$(REDIS_TAG) --build-arg PORT=$(REDIS_PORT)

#Building app images
app-images:
	@echo ":::Building App Image"
	docker build --rm -f APP.Dockerfile $(BUILD_APP_ARGS) -t $(APP_IMAGE_NAME) .

#Building all dependent images.
dep-images:
	@echo ":::Building Dependent Images"
	docker build --rm -f DB.Dockerfile $(BUILD_DB_ARGS) -t $(DB_IMAGE_NAME) .
	docker build --rm -f Redis.Dockerfile $(BUILD_REDIS_ARGS) -t $(REDIS_IMAGE_NAME) .

dep-cont:
	@echo ":::Running dependents container"
	docker run -d -p 5432:5432 -v /var/lib/postgresql/data -v $(shell pwd)/database.sql:/docker-entrypoint-initdb.d/database.sql --env POSTGRES_USER=postgres --env POSTGRES_DBNAME=db_team1 --env POSTGRES_PASSWORD=mypass --env POSTGRES_PORT=5432 --name $(DB_CONT_NAME) $(DB_IMAGE_NAME)
	docker run -d --name $(REDIS_CONT_NAME) $(REDIS_IMAGE_NAME)

app-cont:
	@echo ":::Running app container"
	docker run -dit --env-file=app.env $(APP_OPEN_PORT) --link $(DB_CONT_NAME):db --link $(REDIS_CONT_NAME):redis --name $(APP_CONT_NAME) $(APP_IMAGE_NAME)

#Remove all dependent containers
remove-dep-cont:
	@echo ":::remove s3 container"
	-docker rm ${DB_CONT_NAME} -f
	-docker rm ${REDIS_CONT_NAME} -f
	-docker volume ls -qf dangling=true | xargs docker volume rm

remove-app-cont:
	@echo ":::remove app container"
	-docker rm ${APP_CONT_NAME} -f

dep-up: dep-images dep-cont

app-up: app-images app-cont

app-logs:
	@echo ":::app logs"
	docker logs -f $(APP_CONT_NAME)

build: remove-dep-cont remove-app-cont dep-up app-up app-logs
run-development: app-logs