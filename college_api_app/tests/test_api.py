from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from college_api_app.models import (
    College,
    Category,
    Country,
    City,
)

from college_api_app.serializers import CollegeSerializer


class CollegesApiTestCase(APITestCase):
    def setUp(self) -> None:
        self.category_1 = Category.objects.create(name='Tech')
        self.category_2 = Category.objects.create(name='IT')

        self.country_1 = Country.objects.create(name='Kazakhstan', code='+77')
        self.country_2 = Country.objects.create(name='Russian', code='+99')

        self.city_1 = City.objects.create(name='Kokshetau')
        self.city_2 = City.objects.create(name='Moscow')

        self.college_1 = College.objects.create(title='KAZGTK', category=self.category_1, street='Pushkina 3',
                                                email='kazgtk@gmail.com', type='PRV', country=self.country_1,
                                                city=self.city_1,
                                                budget=10000.231)
        self.college_2 = College.objects.create(title='VTK', category=self.category_2, street='Tajenova 88',
                                                email='VTK@mail.ru',
                                                type='NAT', country=self.country_2, city=self.city_2,
                                                budget=13213.231233)

    def test_get(self):
        url = reverse('api:college-list')
        response = self.client.get(url)
        serializer_data = CollegeSerializer([self.college_1, self.college_2], many=True).data
        self.assertEqual(serializer_data, response.data)

    def test_http_status_college_list(self):
        url = reverse('api:college-list')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
