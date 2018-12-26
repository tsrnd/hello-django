FROM python:3.7

ARG WORK_DIR
ARG PORT

ENV DJANGO_SU_NAME=admin
ENV DJANGO_SU_EMAIL=admin@team2.com
ENV DJANGO_SU_PASSWORD=mypass1

RUN mkdir -p ${WORK_DIR}
WORKDIR ${WORK_DIR}
ADD ./ ${WORK_DIR}

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE ${PORT}

CMD python team2/manage.py migrate && cd team2 && python -c "import os; import django; \
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'team2.settings'); \
    django.setup(); \
    from django.contrib.auth.management.commands.createsuperuser import get_user_model; \
    get_user_model()._default_manager.create_superuser( \
    username='$DJANGO_SU_NAME', \
    email='$DJANGO_SU_EMAIL', \
    password='$DJANGO_SU_PASSWORD')" && cd .. && python team2/manage.py runserver 0.0.0.0:8000
