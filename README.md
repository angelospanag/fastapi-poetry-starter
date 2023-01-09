# fastapi-poetry-starter

A project starter for personal usage containing the following:

* [Python 3.11.*](https://www.python.org/)
* [FastAPI](https://fastapi.tiangolo.com/) web framework
* Structured logging using [structlog](https://www.structlog.org/en/stable/index.html)
* Dependency management using [Poetry](https://python-poetry.org/)
* [Python .gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore)
* Containerisation using a Dockerfile
* Linting using [ruff](https://github.com/charliermarsh/ruff)
* Formatting using [black](https://black.readthedocs.io/en/stable/) and [isort](https://pycqa.github.io/isort/)

## Prerequisites
* [Python 3.11.*](https://www.python.org/downloads/)
* [Poetry](https://python-poetry.org/)

### 1. Install Python 3 and Poetry

**MacOS (using `brew`)**
```bash
brew install python3 poetry
```

**Linux**
```bash
sudo apt install python3 python
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
uvicorn app.main:app --reload
```
## Linting

```bash
ruff app/*
```

## Formatting
```bash
black app/*
```

## Podman usage

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
