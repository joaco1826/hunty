from datetime import date

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List


class PreviousExperienceSerializer(BaseModel):
    company: str = Field(
        description="Name of company of the previous experience",
        title="Company"
    )
    position_name: str = Field(
        description="Position name of the previous experience",
        title="Position Name"
    )
    start_date: date = Field(
        description="Start date of the previous experience",
        title="Start date"
    )
    end_date: date = Field(
        description="End date of the previous experience",
        title="End date"
    )


class CreateOrUpdateUserSerializer(BaseModel):
    first_name: str = Field(
        description="First name of user",
        title="First Name"
    )
    last_name: str = Field(
        description="Last name of user",
        title="Last Name"
    )
    email: EmailStr = Field(
        description="Email of user",
        title="Email"
    )
    years_experience: int = Field(
        description="Experience of the vacancy",
        title="Experience"
    )
    skills: list = Field(
        description="Skills necessary for the vacancy",
        title="Skills"
    )
    previous_experience: Optional[List[PreviousExperienceSerializer]] = Field(
        description="Previous experience",
        title="Previous experience"
    )