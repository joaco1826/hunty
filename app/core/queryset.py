from app.core.helpers import GeneralHelpers
from app.core.models import Company


class CompanyQuerySet:
    @staticmethod
    def create(data: dict):
        register = Company(**data).save()
        return register.to_json()

    @staticmethod
    def list():
        companies = Company.objects(deleted_at=None).all()
        return [company.to_json() for company in companies]

    @staticmethod
    def get(uuid: str):
        company = Company.objects(
            uuid=uuid,
            deleted_at=None
        ).first()

        if company:
            return company.to_json()
        return None

    @staticmethod
    def update(uuid: str, data: dict):
        company = Company.objects(
            uuid=uuid,
            deleted_at=None
        ).first()

        if company:
            company.modify(**data)
            return company.to_json()

        return None

    @staticmethod
    def delete(uuid: str):
        company = Company.objects(
            uuid=uuid,
            deleted_at=None
        ).first()
        if company:
            company.deleted_at = GeneralHelpers.get_datetime()
            company.save()
        return None
