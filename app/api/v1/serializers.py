from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from uuid import UUID


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


class ContactSerializer(BaseModel):
    first_name: str = Field(
        description="First name of contact of the company",
        title="First Name"
    )
    last_name: str = Field(
        description="Last name of contact of the company",
        title="Last Name"
    )
    phone_number: str = Field(
        description="Phone number of contact of the company",
        title="Phone Number"
    )
    email: str = Field(
        description="Email of contact of the company",
        title="Email"
    )


class CreateOrUpdateCompanySerializer(BaseModel):
    name: str = Field(
        description="Name of company",
        title="Name"
    )
    link: Optional[str] = Field(
        description="Link website company",
        title="Link",
    )
    country: Optional[str] = Field(
        description="Country of location of the company",
        title="Country"
    )
    city: Optional[str] = Field(
        description="City of location of the company",
        title="City"
    )
    contact: ContactSerializer = Field(
        description="Contact of the company",
        title="Contact"
    )