from pydantic import BaseModel, Field
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
    email: str = Field(
        description="Email of contact of the company",
        title="Email"
    )


class CreateOrUpdateVacancySerializer(BaseModel):
    position_name: str = Field(
        description="Position name of vacancy",
        title="Position Name"
    )
    company_uuid: str = Field(
        description="Company uuid",
        title="Company Uuid",
    )
    salary: int = Field(
        description="Salary of the vacancy",
        title="Salary"
    )
    min_experience: int = Field(
        description="Minimum experience of the vacancy",
        title="Minimum Experience"
    )
    max_experience: int = Field(
        description="Maximum experience of the vacancy",
        title="Maximum Experience"
    )
    link: str = Field(
        description="Link of the vacancy",
        title="Link"
    )
    skills: list = Field(
        description="Skills necessary for the vacancy",
        title="Skills"
    )