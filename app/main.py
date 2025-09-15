from datetime import datetime, timezone
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.exception_handlers import request_validation_exception_handler
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import JSONResponse

from app.models import (
    ErrorResponse,
    GreetRequest,
    GreetResponse,
    HealthResponse,
    TimeResponse,
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent


app = FastAPI(title="FastAPI OpenAPI Quickstart", version="1.0.0")


@app.exception_handler(RequestValidationError)
async def handle_request_validation_error(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    """
    Return FastAPI's standard validation error response using the built-in handler.

    :param request: The incoming request.
    :param exc: The validation error raised by FastAPI/Pydantic.

    :returns: JSON response with structured validation detail and HTTP 422 status.
    """
    return await request_validation_exception_handler(request, exc)


@app.get("/health", response_model=HealthResponse)
async def get_health() -> HealthResponse:
    """
    Return service health status.

    :returns: Health response with status 'ok'.
    """
    return HealthResponse(status="ok")


@app.get("/time", response_model=TimeResponse)
async def get_current_time() -> TimeResponse:
    """
    Return the current server time in ISO 8601 format.

    :returns: Time response with current UTC timestamp.
    """
    now_utc = datetime.now(timezone.utc)
    iso_utc = now_utc.isoformat().replace("+00:00", "Z")

    return TimeResponse(current_time=iso_utc)


@app.post(
    "/greet", response_model=GreetResponse, responses={400: {"model": ErrorResponse}}
)
async def post_greet(payload: GreetRequest) -> GreetResponse:
    """
    Return a greeting for the provided name.

    :param payload: Body containing the name to greet.

    :returns: Greeting message with the provided name.
    """
    return GreetResponse(message=f"hello {payload.name}!")


@app.get("/docs", include_in_schema=False)
async def get_swagger_ui() -> JSONResponse:
    """
    Return Swagger UI.

    :returns: Swagger UI HTML.
    """
    return get_swagger_ui_html(
        title="Swagger UI - YAML Spec",
    )
