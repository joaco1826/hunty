from pydantic import BaseModel, Field
from typing import Optional, Any


class MetaSerializer(BaseModel):
    message: str = Field(
        default="Success",
        description="Message to be returned to the user",
        title="Message"
    )


class VersionSerializer(BaseModel):
    version: str = Field(
        default="1.0.0",
        description="Version of the API",
        title="Version"
    )
    message: str = Field(
        default="Success",
        description="Message to be returned to the user",
        title="Message"
    )


class StatusSerializer(BaseModel):
    status: str = Field(
        default="OK",
        description="Status of the API",
        title="Status"
    )


class HealthSerializer(BaseModel):
    status_code: int = Field(
        default=200,
        description="Status code of the API",
        title="Status code"
    )
    content: StatusSerializer = Field(
        default=StatusSerializer(),
        description="content of the API",
        title="content"
    )


class ResponseSerializer(BaseModel):
    status: str = Field(
        default="OK",
        description="Status of the API",
        title="Status"
    )
    message: Optional[str] = Field(
        default=None,
        description="Message to be returned to the user",
        title="Message"
    )
    data: Optional[Any] = Field(
        default=None,
        description="Data to be returned to the user",
        title="Data"
    )


class ResponseNotFoundSerializer(BaseModel):
    status: str = Field(
        default="Not Found",
        description="Status of the API",
        title="Status"
    )
    message: Optional[str] = Field(
        default=None,
        description="Message to be returned to the user",
        title="Message"
    )


class ResponseBadRequestSerializer(BaseModel):
    status: str = Field(
        default="Bad Request",
        description="Status of the API",
        title="Status"
    )
    error: dict = Field(
        default=None,
        description="Error in process",
        title="Error"
    )
