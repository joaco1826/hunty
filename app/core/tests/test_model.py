from unittest import TestCase

from mongoengine import connect, disconnect

from ..models import (
    Company,
    Vacancy,
    User,
    Skills,
    Contact,
    PreviousExperience
)


class TestModel(TestCase):
    @classmethod
    def setUpClass(cls):
        disconnect()
        connect('mongoenginetest', host='mongomock://localhost')

    @classmethod
    def tearDownClass(cls):
        disconnect()

    def test_company_save(self):
        params = dict(
            uuid='1-b-3-d-5-f-7-h',
            name='test',
            link='https://example.com',
            country='ColExample',
            city='Baq',
            contact=Contact(
                first_name='test',
                last_name='test',
                phone_number='3111111111',
                email='test@test.com'
            )
        )

        company = Company(**params)
        company.save()

        result = Company.objects().first()

        self.assertIsInstance(result, Company)
        for key in params:
            self.assertEqual(getattr(result, key), params[key])

    def test_vacancy_save(self):
        company = Company.objects().first()
        params = dict(
            uuid='1-b-3-d-5-f-7-h',
            position_name='test',
            salary=10000,
            min_experience=1,
            max_experience=5,
            link='https://example.com',
            company=company,
            skills=[Skills.python.value]
        )

        vacancy = Vacancy(**params)
        vacancy.save()

        result = Vacancy.objects().first()

        self.assertIsInstance(result, Vacancy)
        for key in params:
            self.assertEqual(getattr(result, key), params[key])

    def test_user_save(self):
        params = dict(
            uuid='1-b-3-d-5-f-7-h',
            identification='1234',
            first_name='test',
            last_name='test',
            email='test@example.com',
            years_experience=5,
            previous_experience=[
                PreviousExperience(
                    company='test',
                    position_name='test',
                    start_date='2000-01-01',
                    end_date='2001-01-01',
                )
            ],
            skills=[Skills.python.value]
        )

        user = User(**params)
        user.save()

        result = User.objects().first()

        self.assertIsInstance(result, User)
