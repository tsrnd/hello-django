# Pull base image
FROM python:3.7-slim

ARG WORK_DIR
ARG PORT

ENV DJANGO_SU_NAME=admin
ENV DJANGO_SU_EMAIL=admin@team3.com
ENV DJANGO_SU_PASSWORD=mypass1

CMD cd /code  && python /code/manage.pcleary makemigrations snippets topics && python /code/manage.py migrate && python -c "import os; import django; \
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ddp.settings'); \
    django.setup(); \
    from django.contrib.auth.management.commands.createsuperuser import get_user_model; \
    get_user_model()._default_manager.create_superuser( \
    username='$DJANGO_SU_NAME', \
    email='$DJANGO_SU_EMAIL', \
    password='$DJANGO_SU_PASSWORD')"