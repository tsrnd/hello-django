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

## Deployment

### Local environment with Docker

Start Postgres database service

```
$ docker-compose up -d data
```

Start Hello-Django application service

```
$ docker-compose up --build app
```

### Testing (Staging) environment with Docker

### User Acceptance Testing (UAT) environment with Docker

### Production (PROD) environment with Docker
