# hello-django project team1
# install pienv
sudo -H pip install -U pipenv
# install django
cd HELLO-DJANGO
pipenv install django
# run project in your port if not set default 8000
cd team1
pipenv shell
pipenv run server {your_port}