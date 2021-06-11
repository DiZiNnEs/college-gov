from django.test import TestCase

from college_api_app.models import (
    College,
    Category,
    Country,
    City,
)
from college_api_app.serializers import CollegeSerializer


class SerializersTestCase(TestCase):
    def setUp(cls):
        cls.category_1 = Category.objects.create(name='Tech')
        cls.category_2 = Category.objects.create(name='IT')

        cls.country_1 = Country.objects.create(name='Kazakhstan', code='+77')
        cls.country_2 = Country.objects.create(name='Russian', code='+99')

        cls.city_1 = City.objects.create(name='Kokshetau')
        cls.city_2 = City.objects.create(name='Moscow')

        cls.college_1 = College.objects.create(title='KAZGTK', category=cls.category_1, street='Pushkina 3',
                                           email='kazgtk@gmail.com', type='PRV', country=cls.country_1, city=cls.city_1,
                                           budget=1000.02302)
        cls.college_2 = College.objects.create(title='VTK', category=cls.category_2, street='Tajenova 88', email='VTK@mail.ru',
                                           type='NAT', country=cls.country_2, city=cls.city_2, budget=3545323.123493)
        data = CollegeSerializer([cls.college_1, cls.college_2], many=True).data
        cls.college_1_data = CollegeSerializer(cls.college_1, many=False).data
        cls.college_2_data = CollegeSerializer(cls.college_2, many=False).data

    def test_college_serializers(self):

        expected_data_college_1 = {
            'id': self.college_1.id,
            'type': 'PRV',
            'title': 'KAZGTK',
            'category': self.category_1.pk,
            'street': 'Pushkina 3',
            'email': 'kazgtk@gmail.com',
            'country': self.country_1.id,
            'city': self.city_1.pk,
            'budget': '1000.0230200000',
        }
        expected_data_college_2 = {
            'id': self.college_2.id,
            'type': 'NAT',
            'title': 'VTK',
            'category': self.category_2.pk,
            'street': 'Tajenova 88',
            'email': 'VTK@mail.ru',
            'country': self.country_2.id,
            'city': self.city_2.pk,
            'budget': '3545323.1234930000',
        }

        self.assertEqual(expected_data_college_1, self.college_1_data)
        self.assertEqual(expected_data_college_2, self.college_2_data)
