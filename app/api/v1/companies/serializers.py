from pydantic import BaseModel, Field, EmailStr
from typing import Optional


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
    email: EmailStr = Field(
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
