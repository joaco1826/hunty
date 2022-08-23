from unittest import TestCase
from mongoengine import connect, disconnect

from app.core.process import Data
from app.core.models import DataDocument


class TestGetDataByCreditRequest(TestCase):

    @classmethod
    def setUpClass(cls):
        connect('mongoenginetest', host='mongomock://localhost')
        data = {
            'fake_key': 'fake_value'
        }
        DataDocument(
            credit_request_uid='credit_request_uid_1',
            identification='111',
            etl='fake_etl',
            section_uuid='fake_section',
            document_uuid='111',
            data=data
        ).save()
        DataDocument(
            credit_request_uid='credit_request_uid_1',
            identification='111',
            etl='fake_etl',
            section_uuid='fake_section',
            document_uuid='222',
            data=data
        ).save()
        DataDocument(
            credit_request_uid='credit_request_uid_1',
            identification='111',
            etl='fake_etl',
            section_uuid='fake_section',
            document_uuid='333',
            data=data
        ).save()
        DataDocument(
            credit_request_uid='credit_request_uid_2',
            identification='111',
            etl='fake_etl',
            section_uuid='fake_section',
            document_uuid='444',
            data=data
        ).save()


    @classmethod
    def tearDownClass(cls):
       disconnect()

    def test_get_data_by_credit_request(self):
        credit_request_uid = 'credit_request_uid_1'
        count_data_expected = 3

        list_of_data = Data().get_data_by_credit_request(credit_request_uid)

        assert len(list_of_data) == count_data_expected

    def test_get_data_by_credit_request_not_found(self):
        credit_request_uid = 'credit_request_uid_not_exists'
        count_data_expected = 0

        list_of_data = Data().get_data_by_credit_request(credit_request_uid)

        assert len(list_of_data) == count_data_expected


