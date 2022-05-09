# senkalib

## docker

### for start

```
$ docker-compose up -d
```

### for access to shell in the container

```
$ docker-compose exec senkalib bash
```

### for end

```
$ docker-compose down
```

### for remove

```
$ docker-compose down --rmi all --volumes --remove-orphans
```

## for developers

1. Install poetry to set up python environment

```
If you have not yet installed poetry, first install poetry as follows
$ curl -sSL https://install.python-poetry.org | python3 -
Set the poetry path as the log shows.
$ export PATH="$HOME/.local/bin:$PATH"
Set up the python environment as follows.
$ poetry config virtualenvs.in-project true && poetry install
```

2. Install pre-commit

```
# Before committing, we use pre-commmit hook to check the code style.
# Install pre-commit in the following way
$ pre-commit install

# If you are using docker and the venv environment is not enabled, please do the following to enable it.
$ source /app/.venv/bin/activate

```

## for test

```
$ poetry shell
$ pytest --cov=src --cov-branch --cov-report=term-missing -vv
```
