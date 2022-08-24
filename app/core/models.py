from mongoengine import (
    Document,
    EmbeddedDocument,
    EmbeddedDocumentField,
    ReferenceField
)
from enum import Enum
from mongoengine.fields import (
    DateField,
    DateTimeField,
    EmailField,
    IntField,
    ListField,
    StringField
)

from app.core.helpers import GeneralHelpers


class Skills(Enum):
    python = "python"
    aws = "aws"
    gcp = "gcp"
    java = "java"
    javascript = "javascript"
    mvc = "mvc"
    php = "php"
    azure = "azure"
    flask = "flask"
    django = "django"
    fast_api = "fast_api"
    laravel = "laravel"
    mongo = "mongo"
    firebase = "firebase"

    @staticmethod
    def values() -> list:
        return list(map(lambda e: e.value, Skills))


class TimeStamps:
    created_at = DateTimeField(
        default=lambda: GeneralHelpers.get_datetime()
    )
    updated_at = DateTimeField(
        default=lambda: GeneralHelpers.get_datetime()
    )
    deleted_at = DateTimeField()


class Contact(EmbeddedDocument):
    first_name = StringField(
        required=True
    )
    last_name = StringField(
        required=True
    )
    phone_number = StringField(
        required=True
    )
    email = EmailField(
        required=True
    )


class Company(Document, TimeStamps):
    uuid = StringField(
        default=lambda: GeneralHelpers.get_uuid()
    )
    name = StringField(
        required=True
    )
    link = StringField()
    country = StringField()
    city = StringField()
    contact = EmbeddedDocumentField(
        Contact
    )

    meta = {
        "collection": "companies",
        "indexes": [
            "uuid",
            "name"
        ]
    }


class Vacancy(Document, TimeStamps):
    uuid = StringField(
        default=lambda: GeneralHelpers.get_uuid()
    )
    position_name = StringField(
        required=True
    )
    salary = IntField(
        required=True
    )
    min_experience = IntField(
        required=True
    )
    max_experience = IntField(
        required=True
    )
    vacancy_link = StringField(
        required=True
    )
    company = ReferenceField(
        Company,
        required=True
    )
    skills = ListField(
        StringField(
            choices=Skills.values()
        ),
        required=True
    )

    meta = {
        "collection": "vacancies",
        "indexes": [
            "uuid",
            "position_name"
        ]
    }


class PreviousExperience(EmbeddedDocument):
    company = StringField(
        required=True
    )
    position_name = StringField(
        required=True
    )
    start_date = DateField(
        required=True
    )
    end_date = DateField(
        required=True
    )


class User(Document, TimeStamps):
    uuid = StringField(
        default=lambda: GeneralHelpers.get_uuid()
    )
    identification = StringField(
        required=True
    )
    first_name = StringField(
        required=True
    )
    last_name = StringField(
        required=True
    )
    email = EmailField(
        required=True
    )
    years_experience = IntField(
        required=True
    )
    previous_experience = ListField(
        EmbeddedDocumentField(PreviousExperience)
    )
    skills = ListField(
        StringField(
            choices=Skills.values()
        ),
        required=True
    )
