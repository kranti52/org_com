from django.test import TestCase
from django.urls import reverse
from faker import Faker
from rest_framework import status

from ...models import Issue
from ...models import Metric
from ...models import Product


class MapTestCase(TestCase):
    def setUp(self):
        fake = Faker()
        self.product_title = fake.first_name()
        self.product_description = fake.text(max_nb_chars=200)
        self.product = Product.objects.create(**{'title': self.product_title,
                                                 'description': self.product_description})

        self.metric_title = fake.first_name()
        self.metric_description = fake.text(max_nb_chars=200)
        self.metric = Metric.objects.create(**{'title': self.product_title,
                                               'description': self.product_description})

        self.issue_title = fake.first_name()
        self.issue_category = 'other'
        self.issue = Issue.objects.create(**{'title': self.product_title,
                                             'category': self.issue_category})
        # Map URLs.
        self.map_url = reverse('entity-map')

    def test_create_map_with_valid_data(self):
        data = {
            'first_object_id': self.issue.id,
            'second_object_id': self.product.id
        }
        headers = {}
        response = self.client.post(self.map_url, data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_map_with_empty_first_object(self):
        data = {
            'first_object_id': '',
            'second_object_id': self.product.id
        }
        headers = {}
        response = self.client.post(self.map_url, data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_map_with_no_first_object(self):
        data = {
            'second_object_id': self.product.id
        }
        headers = {}
        response = self.client.post(self.map_url, data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_map_with_empty_last_object(self):
        data = {
            'second_object_id': '',
            'first_object_id': self.product.id
        }
        headers = {}
        response = self.client.post(self.map_url, data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_map_with_no_last_object(self):
        data = {
            'first_object_id': self.product.id
        }
        headers = {}
        response = self.client.post(self.map_url, data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_map_with_same_objects(self):
        data = {
            'first_object_id': self.product.id,
            'second_object_id': self.product.id
        }
        headers = {}
        response = self.client.post(self.map_url, data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_map_with_invalid_object(self):
        data = {
            'first_object_id': 5445545445,
            'second_object_id': self.product.id
        }
        headers = {}
        response = self.client.post(self.map_url, data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_map_with_valid_id(self):
        headers = {}
        data = {
            'first_object_id': self.issue.id,
            'second_object_id': self.metric.id
        }
        self.client.post(self.map_url, data, format='json', **headers)
        data = {
            'first_object_id': self.issue.id,
            'second_object_id': self.product.id
        }
        self.client.post(self.map_url, data, format='json', **headers)

        params = {
            'id': self.issue.id
        }

        response = self.client.get(self.map_url, params, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)
