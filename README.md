# FastAPI quickstart
> Basic app to demonstrate use of FastAPI with SwaggerDocs

- [OpenAPI specification](https://swagger.io/specification/)
- [Swagger](https://swagger.io/) website

## Install

Install Poetry globally with `pip` or `pipx`.

```sh
make install
```

## Run

Start dev server:

```sh
make serve
```
Server with overrides:

```sh
make serve HOST=0.0.0.0 PORT=9000
```

## API Docs

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
- **OpenAPI (JSON)**: `http://localhost:8000/openapi.json` (from FastAPI)
