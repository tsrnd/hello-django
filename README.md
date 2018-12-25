# Hello Django

## Development

Make sure `pipenv` sticks the virtualenv in `project/.venv` by setting the `PIPENV_VENV_IN_PROJECT` environment variable.

```bash
# ~/.bashrc, ~/.bash_profile, ~/.zshrc
PIPENV_VENV_IN_PROJECT=1
```

Sync all dependencies

```bash
$ pipenv sync
$ pipenv sync --dev
```

Run server with local environment

```
$ pipenv run local
```

Run server with docker environment

```
$ pipenv run docker
```

## Deployment

Sync production dependencies

```bash
$ pipenv sync
```
