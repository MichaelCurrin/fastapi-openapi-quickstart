from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
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


app = FastAPI(title="Simple Python App API", version="1.0.0")


@app.exception_handler(RequestValidationError)
async def handle_request_validation_error(
    _: Request, exc: RequestValidationError
) -> JSONResponse:
    """
    Return a 400 error with a simplified message when request validation fails.

    :param _: Ignored request object.
    :param exc: The validation error raised by FastAPI/Pydantic.

    :returns: JSON response with error message and HTTP 400 status.
    """
    message = "invalid request"

    # Attempt to produce a friendly error for missing 'name' in /greet
    try:
        error_items: list[dict[str, Any]] = exc.errors()  # type: ignore[assignment]
        for item in error_items:
            loc = item.get("loc") or []
            msg = item.get("msg") or "invalid request"
            if isinstance(loc, (list, tuple)) and "body" in loc and "name" in loc:
                if "field required" in msg or "Input should be" in msg:
                    message = "name is required"
                    break
        else:
            # Fallback to first error message if available
            if error_items:
                message = error_items[0].get("msg", message)
    except Exception:
        message = "invalid request"

    return JSONResponse(
        status_code=400, content=ErrorResponse(error=message).model_dump()
    )


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
        openapi_url="/openafpi.yaml",
        title="Swagger UI - YAML Spec",
    )
