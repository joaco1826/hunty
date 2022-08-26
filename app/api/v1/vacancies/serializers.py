from pydantic import BaseModel, Field


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