# Hello Django

## Development

Make sure `pipenv` sticks the virtualenv in `./.venv` by setting the
 `PIPENV_VENV_IN_PROJECT` environment variable.

```bash
# ~/.bashrc, ~/.bash_profile, ~/.zshrc
PIPENV_VENV_IN_PROJECT=1
```

Install all dependencies (includes dev)

```bash
$ pipenv install --dev
```

Run app with local environment

```
$ pipenv run python manage.py runserver 0.0.0.0:8000
```

### Freeze Requirements

```
$ pipenv lock --requirements > requirements.txt
```

### Docker Supports

Run app with docker environment

```
$ docker-compose up
```

## Deployment

Install production dependencies

```bash
$ pipenv install
```
