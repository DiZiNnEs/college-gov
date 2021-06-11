from django.test import TestCase

from college_api_app.models import (
    College,
    Category,
    Country,
    City,
)
from college_api_app.serializers import CollegeSerializer


class SerializersTestCase(TestCase):
    def test_college_serializers(self):
        category_1 = Category.objects.create(name='Tech')
        category_2 = Category.objects.create(name='IT')

        country_1 = Country.objects.create(name='Kazakhstan', code='+77')
        country_2 = Country.objects.create(name='Russian', code='+99')

        city_1 = City.objects.create(name='Kokshetau')
        city_2 = City.objects.create(name='Moscow')

        college_1 = College.objects.create(title='KAZGTK', category=category_1, street='Pushkina 3',
                                           email='kazgtk@gmail.com', type='PRV', country=country_1, city=city_1,
                                           budget=1000.02302)
        college_2 = College.objects.create(title='VTK', category=category_2, street='Tajenova 88', email='VTK@mail.ru',
                                           type='NAT', country=country_2, city=city_2, budget=3545323.123493)
        data = CollegeSerializer([college_1, college_2], many=True).data
        college_1_data = CollegeSerializer(college_1, many=False).data
        college_2_data = CollegeSerializer(college_2, many=False).data
        expected_data_college_1 = {
            'id': college_1.id,
            'type': 'PRV',
            'title': 'KAZGTK',
            'category': category_1.pk,
            'street': 'Pushkina 3',
            'email': 'kazgtk@gmail.com',
            'country': country_1.id,
            'city': city_1.pk,
            'budget': '1000.0230200000',
        }
        expected_data_college_2 = {
            'id': college_2.id,
            'type': 'NAT',
            'title': 'VTK',
            'category': category_2.pk,
            'street': 'Tajenova 88',
            'email': 'VTK@mail.ru',
            'country': country_2.id,
            'city': city_2.pk,
            'budget': '3545323.1234930000',
        }

        self.assertEqual(expected_data_college_1, college_1_data)
        self.assertEqual(expected_data_college_2, college_2_data)
