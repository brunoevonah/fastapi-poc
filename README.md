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

### Adding more dependencies
```sh
poetry add starlette_prometheus

# To remove
poetry remove starlette_prometheus
```
## Common commands
Use these commands inside the root folder (fastapi-poc by default) to execute tasks for the project
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
### Run tests
```sh
poetry run pytest tests
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
