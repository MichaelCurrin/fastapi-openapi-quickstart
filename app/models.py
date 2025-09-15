from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """
    Represent a health check response.
    """

    status: str = Field(description="Health status string, typically 'ok'.")


class TimeResponse(BaseModel):
    """
    Represent the current time response in ISO 8601 format.
    """

    current_time: str = Field(description="Current server time in ISO 8601 format.")


class GreetRequest(BaseModel):
    """
    Represent the request body for a greeting.
    """

    name: str = Field(min_length=1, description="Name to greet.")


class GreetResponse(BaseModel):
    """
    Represent the greeting message response.
    """

    message: str = Field(description="Greeting message including the provided name.")


class ErrorResponse(BaseModel):
    """
    Represent an error response payload.
    """

    error: str
