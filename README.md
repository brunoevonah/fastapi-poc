# fastapi-poc
Python Fast API POC

## Dependencies
[Poetry](https://python-poetry.org/): Python packaging and dependency

## Project initial set up
`Init Python project`

```sh
poetry install
poetry run pre-commit install
```

## Common commands
### Lint check
```sh
poetry run flake8
poetry run black --check .
```
### Apply formating
```sh
poetry run isort .
poetry run black .
```

### Run locally
```sh
poetry run uvicorn app.main:create_app --factory --reload
```

### Build locally
```sh
docker build -t fastapipoc:latest .
```
### Run from docker
```sh
docker run -p 8000:8000 fastapipoc
```
### Swagger/OpenAPI access
http://localhost:8000/docs
