from app.core.constants import NOT_FOUND
from app.core.queryset import CompanyQuerySet, VacancyQuerySet, UserQuerySet


class CompanyProcess:
    @staticmethod
    def create(data: dict):
        company = CompanyQuerySet.create(data)
        return {
            "status": 201,
            "message": "Company created successfully!",
            "data": company
        }

    @staticmethod
    def list():
        companies = CompanyQuerySet.list()
        return {
            "status": 200,
            "message": "List companies successfully!",
            "data": companies
        }

    @staticmethod
    def get(uuid: str):
        company = CompanyQuerySet.get(uuid)

        if company:
            return {
                "status": 200,
                "message": "Get company successfully!",
                "data": company
            }

        return {
            "status": 404,
            "message": NOT_FOUND
        }

    @staticmethod
    def update(uuid: str, data: dict):
        company = CompanyQuerySet.update(uuid, data)

        if company:
            return {
                "status": 200,
                "message": "Company updated successfully!",
                "data": company
            }

        return {
            "status": 404,
            "message": NOT_FOUND
        }

    @staticmethod
    def delete(uuid: str):
        CompanyQuerySet.delete(uuid)
        return {
            "status": 204,
            "message": "Company deleted successfully!"
        }


class VacancyProcess:
    @staticmethod
    def create(data: dict):
        vacancy = VacancyQuerySet.create(data)
        return {
            "status": 201,
            "message": "Vacancy created successfully!",
            "data": vacancy
        }

    @staticmethod
    def list():
        vacancies = VacancyQuerySet.list()
        return {
            "status": 200,
            "message": "List vacancies successfully!",
            "data": vacancies
        }

    @staticmethod
    def get(uuid: str):
        vacancy = VacancyQuerySet.get(uuid)

        if vacancy:
            return {
                "status": 200,
                "message": "Get vacancy successfully!",
                "data": vacancy
            }

        return {
            "status": 404,
            "message": NOT_FOUND
        }

    @staticmethod
    def update(uuid: str, data: dict):
        vacancy = VacancyQuerySet.update(uuid, data)

        if vacancy:
            return {
                "status": 200,
                "message": "Vacancy updated successfully!",
                "data": vacancy
            }

        return {
            "status": 404,
            "message": NOT_FOUND
        }

    @staticmethod
    def delete(uuid: str):
        VacancyQuerySet.delete(uuid)
        return {
            "status": 204,
            "message": "Vacancy deleted successfully!"
        }


class UserProcess:
    @staticmethod
    def create(data: dict):
        user = UserQuerySet.create(data)
        return {
            "status": 201,
            "message": "User created successfully!",
            "data": user
        }

    @staticmethod
    def list():
        users = UserQuerySet.list()
        return {
            "status": 200,
            "message": "List vacancies successfully!",
            "data": users
        }

    @staticmethod
    def get(uuid: str):
        user = UserQuerySet.get(uuid)

        if user:
            return {
                "status": 200,
                "message": "Get user successfully!",
                "data": user
            }

        return {
            "status": 404,
            "message": NOT_FOUND
        }

    @staticmethod
    def update(uuid: str, data: dict):
        user = UserQuerySet.update(uuid, data)

        if user:
            return {
                "status": 200,
                "message": "User updated successfully!",
                "data": user
            }

        return {
            "status": 404,
            "message": NOT_FOUND
        }

    @staticmethod
    def delete(uuid: str):
        UserQuerySet.delete(uuid)
        return {
            "status": 204,
            "message": "User deleted successfully!"
        }