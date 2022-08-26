from app.core.helpers import GeneralHelpers
from app.core.models import Company, Vacancy, User


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


class VacancyQuerySet:
    @staticmethod
    def create(data: dict):
        company = Company.objects(uuid=data.pop("company_uuid")).first()
        data["company"] = company
        register = Vacancy(**data).save()
        return register.to_json()

    @staticmethod
    def list():
        vacancies = Vacancy.objects(deleted_at=None).all()
        return [vacancy.to_json() for vacancy in vacancies]

    @staticmethod
    def get(uuid: str):
        vacancy = Vacancy.objects(
            uuid=uuid,
            deleted_at=None
        ).first()

        if vacancy:
            return vacancy.to_json()
        return None

    @staticmethod
    def update(uuid: str, data: dict):
        vacancy = Vacancy.objects(
            uuid=uuid,
            deleted_at=None
        ).first()

        if vacancy:
            vacancy.modify(**data)
            return vacancy.to_json()

        return None

    @staticmethod
    def delete(uuid: str):
        vacancy = Vacancy.objects(
            uuid=uuid,
            deleted_at=None
        ).first()
        if vacancy:
            vacancy.deleted_at = GeneralHelpers.get_datetime()
            vacancy.save()
        return None


class UserQuerySet:
    @staticmethod
    def create(data: dict):
        register = User(**data).save()
        return register.to_json()

    @staticmethod
    def list():
        users = User.objects(deleted_at=None).all()
        return [user.to_json() for user in users]

    @staticmethod
    def get(uuid: str):
        user = User.objects(
            uuid=uuid,
            deleted_at=None
        ).first()

        if user:
            return user.to_json()
        return None

    @staticmethod
    def update(uuid: str, data: dict):
        user = User.objects(
            uuid=uuid,
            deleted_at=None
        ).first()

        if user:
            user.modify(**data)
            return user.to_json()

        return None

    @staticmethod
    def delete(uuid: str):
        user = User.objects(
            uuid=uuid,
            deleted_at=None
        ).first()
        if user:
            user.deleted_at = GeneralHelpers.get_datetime()
            user.save()
        return None
