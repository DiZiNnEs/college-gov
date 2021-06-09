from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from college_api_app.models import College, Category, Country, City
from college_api_app.serializers import CollegeSerializer


class CollegesApiTestCase(APITestCase):
    def test_get(self):
        category_1 = Category.objects.create(name='Tech')
        category_2 = Category.objects.create(name='IT')

        country_1 = Country.objects.create(name='Kazakhstan', code='+77')
        country_2 = Country.objects.create(name='Russian', code='+99')

        city_1 = City.objects.create(name='Kokshetau')
        city_2 = City.objects.create(name='Moscow')

        college_1 = College.objects.create(title='KAZGTK', category=category_1, street='Pushkina 3', email='kazgtk@gmail.com', type='PRV', country=country_1, city=city_1)
        college_2 = College.objects.create(title='VTK', category=category_2, street='Tajenova 88', email='VTK@mail.ru', type='NAT', country=country_2, city=city_2)

        url = reverse('api:college-list')
        response = self.client.get(url)
        serializer_data = CollegeSerializer([college_1, college_2], many=True).data
        self.assertEqual(serializer_data, response.data)

    def test_http_status_college_list(self):
        url = reverse('api:college-list')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_http_status_college_detail(self):
        url = reverse('api:college-detail')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
