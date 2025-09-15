# FastAPI OpenAPI Quickstart
> Basic Python app to combine FastAPI + OpenAPI spec + Swagger UI

- [OpenAPI specification](https://swagger.io/specification/)
- [Swagger](https://swagger.io/) website

## Install

Install Poetry globally with `pip` or `pipx`.

```sh
make install
```

## Usage

### Run

Start dev server:

```sh
make serve
```

Server with overrides:

```sh
make serve HOST=0.0.0.0 PORT=9000
```

### API Docs

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`
- **OpenAPI (JSON)**: `http://127.0.0.1:8000/openapi.json` (from FastAPI)
