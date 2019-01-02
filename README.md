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

Run application directly.
Note: the database url is 'postgres://hello:django@localhost:5432/default'

```
$ make run
```

Run application within Docker environment

```
$ make run-docker
```

View [the result](http://localhost:8000/api/foo/hello) on the browser.

### Other Makefile commands

Clean up Docker exited containers & dangling images.

```
$ make clean
```
