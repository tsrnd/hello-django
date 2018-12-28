FROM python:3.7-alpine

# Tell python not to produce any `__pycache__` and `*.pyc` files
ENV \
  PYTHONBUFFERED=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  INSIDE_DOCKER=1 \
  PIPENV_VENV_IN_PROJECT=1

# Install psql & redis cli
RUN apk add --no-cache \
    postgresql-client \
    redis

# Copy your application code to the container (make sure you create a
# .dockerignore file if any large files or directories should be excluded)
RUN mkdir -p /code
WORKDIR /code
ADD Pip* ./

# Install build deps, then run `pip install`, then remove unneeded build deps
# all in a single step. Correct the path to your production requirements file,
# if needed.
RUN set -ex \
    && apk add --no-cache --virtual .build-deps \
      gcc \
      make \
      libc-dev \
      musl-dev \
      linux-headers \
      pcre-dev \
      postgresql-dev \
    && pip install --upgrade pip \
    && pip install pipenv \
    && LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "pipenv install --deploy" \
    && run_deps="$( \
      scanelf --needed --nobanner --recursive /venv \
        | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
        | sort -u \
        | xargs -r apk info --installed \
        | sort -u \
    )" \
    && apk add --virtual .python-rundeps $run_deps \
    && apk del .build-deps

ADD . ./

ENV DJANGO_SETTINGS_MODULE=app.settings.dev

RUN chmod +x docker-entrypoint.sh
ENTRYPOINT [ "/code/docker-entrypoint.sh" ]
CMD [ "/code/.venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000" ]
