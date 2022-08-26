from app.core.process import CompanyProcess


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
