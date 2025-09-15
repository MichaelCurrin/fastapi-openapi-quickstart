# FastAPI OpenAPI Quickstart
> Basic Python app to combine FastAPI + OpenAPI spec + Swagger UI

## References

- [FastAPI features](https://fastapi.tiangolo.com/features/) in the documentation
- [OpenAPI specification](https://swagger.io/specification/) on Swagger website
- [OpenAPI specificaiton](https://github.com/OAI/OpenAPI-Specification) on GitHub
- [Swagger](https://swagger.io/) website
- [ReDoc](https://github.com/Redocly/redoc) on GitHub

## Install

Install Poetry globally with `pip` or `pipx`.

```sh
make install
```

## Usage

Start dev server:

```sh
make serve
```

Server with overrides:

```sh
make serve HOST=0.0.0.0 PORT=9000
```

## API Docs

These are builtin features for FastAPI:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc
- **OpenAPI (JSON)**: http://127.0.0.1:8000/openapi.json
