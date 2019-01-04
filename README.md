# Hello Django

[![Build Status](https://travis-ci.com/tsrnd/hello-django.svg?branch=master)](https://travis-ci.com/tsrnd/hello-django)

## Development

Make sure:
- `pipenv` sticks the virtualenv in `./.venv` by setting the
 `PIPENV_VENV_IN_PROJECT` environment variable.
- Tell Python don't generate `__pycache__` directory.

```bash
# ~/.bashrc, ~/.bash_profile, ~/.zshrc
export PIPENV_VENV_IN_PROJECT=1
export PYTHONDONTWRITEBYTECODE=1
```

Install all dependencies (includes dev).

```bash
$ make install
```

Clone environment from example file, update it by yourself if needed.

```
$ cp .env.example .env
```

or run application within Docker environment.

```
$ make up
```

View [the result](http://localhost:8000/api/foo/hello) on the browser.

### Debugging

Start PostgreSQL database service with Docker.

```
$ make up-data
```

And start debugging from Visual Code menu.

### Testing

Run all test cases.

```
$ make test
```
