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

    def to_json(self, *args, **kwargs):
        return {
            "uuid": self.uuid,
            "name": self.name,
            "link": self.link,
            "country": self.country,
            "city": self.city,
            "contact": {
                "first_name": self.contact.first_name,
                "last_name": self.contact.last_name,
                "phone_number": self.contact.phone_number,
                "email": self.contact.email
            },
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at)
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
    link = StringField(
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

    def to_json(self, *args, **kwargs):
        return {
            "uuid": self.uuid,
            "position_name": self.position_name,
            "link": self.link,
            "salary": self.salary,
            "min_experience": self.min_experience,
            "max_experience": self.max_experience,
            "skills": self.skills,
            "company": self.company.to_json(),
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at)
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

    def to_json(self, *args, **kwargs):
        return {
            "company": self.company,
            "position_name": self.position_name,
            "start_date": self.start_date,
            "end_date": self.end_date
        }


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

    meta = {
        "collection": "users",
        "indexes": [
            "uuid",
            "email"
        ]
    }

    def to_json(self, *args, **kwargs):
        return {
            "uuid": self.uuid,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "years_experience": self.years_experience,
            "skills": self.skills,
            "previous_experience": [
                experience.to_json()
                for experience in self.previous_experience
            ],
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at)
        }
