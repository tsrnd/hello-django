+ Build project:

    - Install framework:
        pip install Django
        pip install djangorestframework
    - move to project folder
    - Start command:
        docker-compose up -d --build
    - Case have no supper user for login admin, please:
        docker-compose run web python /code/manage.py createsuperuser


+ Test function with pytest.
    docker-compose run web py.test