FROM python:3.7-alpine

ENV PYTHONBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    INSIDE_DOCKER=1

ADD requirements.txt /

RUN set -ex \
    && apk add --no-cache --virtual .build-deps \
        gcc \
        make \
        libc-dev \
        musl-dev \
        linux-headers \
        pcre-dev \
        postgresql-dev \
    && pip install -r requirements.txt --no-cache-dir \
    && apk del .build-deps \
    && apk add --no-cache \
        postgresql-client \
        redis

ADD docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

RUN mkdir -p /code
WORKDIR /code

ENV DJANGO_MANAGEPY_MIGRATE=1 \
    DJANGO_MANAGEPY_COLLECTSTATIC=0

ENTRYPOINT [ "/docker-entrypoint.sh" ]
