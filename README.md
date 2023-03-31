# fastapi-poetry-starter

- [fastapi-poetry-starter](#fastapi-poetry-starter)
  - [Description](#description)
  - [Prerequisites](#prerequisites)
    - [1. Install Python 3 and Poetry](#1-install-python-3-and-poetry)
    - [2. Create a virtual environment with all necessary dependencies](#2-create-a-virtual-environment-with-all-necessary-dependencies)
    - [3. Activate your virtual environment](#3-activate-your-virtual-environment)
  - [Run application](#run-application)
  - [Testing](#testing)
    - [With coverage](#with-coverage)
    - [With coverage and HTML output](#with-coverage-and-html-output)
  - [Linting](#linting)
  - [Formatting](#formatting)
  - [Containerisation](#containerisation)
    - [1. Build image and tag it as `fastapi-poetry-starter`](#1-build-image-and-tag-it-as-fastapi-poetry-starter)
    - [2. Run a container of the previously tagged image (`fastapi-poetry-starter`)](#2-run-a-container-of-the-previously-tagged-image-fastapi-poetry-starter)
    - [3. Check running containers](#3-check-running-containers)
    - [4. Hit sample endpoint](#4-hit-sample-endpoint)

## Description

A project starter for personal usage containing the following:

- [Python 3.11.\*](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/) web framework
- Structured logging using [`structlog`](https://www.structlog.org/)
- Dependency management using [`poetry`](https://python-poetry.org/)
- Containerisation using a Dockerfile
- Testing with [`pytest`](https://docs.pytest.org/) and optionally with coverage with [`pytest-cov`](https://pytest-cov.readthedocs.io/)
- Linting/formatting using [`ruff`](https://beta.ruff.rs/docs/) and [`black`](https://black.readthedocs.io/)
- [`.gitignore`](https://github.com/github/gitignore/blob/main/Python.gitignore)

## Prerequisites

- [Python 3.11.\*](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/)

### 1. Install Python 3 and Poetry

**MacOS (using `brew`)**

```bash
brew install python3 poetry
```

**Ubuntu/Debian**

```bash
sudo apt install python3 python3-venv
python3 -m pip install --user pipx
python3 -m pipx ensurepath
pipx install poetry
```

### 2. Create a virtual environment with all necessary dependencies

From the root of the project execute:

```bash
poetry install
```

### 3. Activate your virtual environment

From the root of the project execute:

```bash
poetry shell
```

## Run application

Runs the FastAPI web application on port `8000` using [uvicorn](https://www.uvicorn.org/):

```bash
uvicorn src.main:app --reload
```

## Testing

```bash
pytest
```

### With coverage

```bash
pytest --cov=app
```

### With coverage and HTML output

```bash
pytest --cov-report html --cov=app
```

## Linting

```bash
ruff app/* tests/*
```

## Formatting

```bash
black app/* tests/*
```

## Containerisation

The following `podman` commands are direct replacements of the Docker CLI. You can see that their syntax is identical:

### 1. Build image and tag it as `fastapi-poetry-starter`

```bash
podman image build -t fastapi-poetry-starter .
```

### 2. Run a container of the previously tagged image (`fastapi-poetry-starter`)

Run our FastAPI application and map our local port `8000` to `80` on the running container:

```bash
podman container run -d --name fastapi-poetry-starter -p 8000:80 --network bridge fastapi-poetry-starter
```

### 3. Check running containers

```bash
podman ps
```

```bash
CONTAINER ID  IMAGE                            COMMAND               CREATED         STATUS             PORTS                 NAMES
78586e5b4683  localhost/fastapi-poetry-starter:latest  uvicorn main:app ...  13 minutes ago  Up 5 minutes ago  0.0.0.0:8000->80/tcp  nifty_roentgen
```

### 4. Hit sample endpoint

Our FastAPI server now runs on port `8000` on our local machine. We can test it with:

```bash
curl -i http://localhost:8000/healthcheck
```

Output:

```bash
HTTP/1.1 200 OK
server: uvicorn
content-length: 0
```
