from app.core.constants import NOT_FOUND
from app.core.queryset import CompanyQuerySet


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