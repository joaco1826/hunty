import uuid
from datetime import datetime


class GeneralHelpers:

    @staticmethod
    def get_datetime():
        """
        Method for getting time
        :return:
        """
        time = datetime.now()
        return time

    @staticmethod
    def get_iso_time():
        """
        Method for getting iso time
        :return:
        """
        time = datetime.now().isoformat()
        return time

    @staticmethod
    def get_uuid():
        """
        Method for generating uuid
        :return: uuid string
        """
        guid = uuid.uuid4()
        return str(guid)
