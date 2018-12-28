FROM python:3.7

ARG WORK_DIR
ARG PORT

RUN mkdir -p ${WORK_DIR}
WORKDIR ${WORK_DIR}
ADD ./ ${WORK_DIR}
ENV PIPENV_YES=1

RUN pip install --upgrade pip && \
    pip install -U pipenv && \
    PYTHON_BIN_PATH="$(python3 -m site --user-base)/bin" && \
    PATH="$PATH:$PYTHON_BIN_PATH" && \
    pipenv install --three

EXPOSE ${PORT}

CMD pipenv run python team1/manage.py migrate && echo "from django.contrib.auth.models import User; \nif User.objects.filter(username='$DJANGO_NAME').count() == 0: User.objects.create_superuser('$DJANGO_NAME', '$DJANGO_EMAIL', '$DJANGO_PASSWORD')" | pipenv run python team1/manage.py shell && CMD pipenv run python team1/manage.py migrate && pipenv run python team1/manage.py runserver  0.0.0.0:8000 && pipenv run python team1/manage.py runserver  0.0.0.0:8000
