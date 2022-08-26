from app.core.process import CompanyProcess, VacancyProcess


class CompanyHandler:
    @staticmethod
    def create(data: dict):
        return CompanyProcess.create(data)

    @staticmethod
    def list():
        return CompanyProcess.list()

    @staticmethod
    def get(uuid: str):
        return CompanyProcess.get(uuid)

    @staticmethod
    def update(uuid: str, data: dict):
        return CompanyProcess.update(uuid, data)

    @staticmethod
    def delete(uuid: str):
        return CompanyProcess.delete(uuid)


class VacancyHandler:
    @staticmethod
    def create(data: dict):
        return VacancyProcess.create(data)

    @staticmethod
    def list():
        return VacancyProcess.list()

    @staticmethod
    def get(uuid: str):
        return VacancyProcess.get(uuid)

    @staticmethod
    def update(uuid: str, data: dict):
        return VacancyProcess.update(uuid, data)

    @staticmethod
    def delete(uuid: str):
        return VacancyProcess.delete(uuid)
