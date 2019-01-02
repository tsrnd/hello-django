# Hello Django

## Development

Make sure `pipenv` sticks the virtualenv in `./.venv` by setting the
 `PIPENV_VENV_IN_PROJECT` environment variable.

```bash
# ~/.bashrc, ~/.bash_profile, ~/.zshrc
PIPENV_VENV_IN_PROJECT=1
```

Install all dependencies (includes dev).

```bash
$ pipenv install --dev
```

Clone environment from example file, update it by yourself if needed.

```
$ cp .env.example .env
```

Run application directly

```
$ make run
```

or run application within Docker environment.

```
$ make up
```

View [the result](http://localhost:8000/api/foo/hello) on the browser.

### Debug

Start PostgreSQL database service with Docker.

```
$ make up-data
```

And start debuging from Visual Code menu.
