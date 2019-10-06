from django.test import TestCase
from faker import Faker
from rest_framework import status

from ...models import Issue
from ...models import Metric
from ...models import Product


class InformationalSystemTestCase(TestCase):
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
        # Product URLs.
        self.create_product = "/entity/{}".format('product')
        self.retrieve_product = "/entity/{}".format('product')
        self.update_product = "/entity/{}/{}".format(self.product.id, 'product')
        self.delete_product = "/entity/{}/{}".format(self.product.id, 'product')

        # Issue urls
        self.create_issue = "/entity/{}".format('issue')
        self.retrieve_issue = "/entity/{}".format('issue')
        self.update_issue = "/entity/{}/{}".format(self.issue.id, 'issue')
        self.delete_issue = "/entity/{}/{}".format(self.issue.id, 'issue')

        # Metric urls
        self.create_metric = "/entity/{}".format('metric')
        self.retrieve_metric = "/entity/{}".format('metric')
        self.update_metric = "/entity/{}/{}".format(self.metric.id, 'metric')
        self.delete_metric = "/entity/{}/{}".format(self.metric.id, 'metric')

    def test_create_product_with_valid_data(self):
        fake = Faker()

        data = {
            'title': fake.first_name(),
            'description': fake.text(max_nb_chars=200)
        }
        headers = {}
        response = self.client.post(self.create_product, data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_product_with_empty_title(self):
        fake = Faker()

        data = {
            'title': '',
            'description': fake.text(max_nb_chars=200)
        }
        headers = {}
        response = self.client.post(self.create_product, data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_product_with_no_title(self):
        fake = Faker()

        data = {
            'description': fake.text(max_nb_chars=200)
        }
        headers = {}
        response = self.client.post(self.create_product, data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_product_with_empty_description(self):
        fake = Faker()

        data = {
            'title': fake.first_name(),
            'description': ''
        }
        headers = {}
        response = self.client.post(self.create_product, data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_product_with_no_description(self):
        fake = Faker()

        data = {
            'title': fake.first_name()
        }
        headers = {}
        response = self.client.post(self.create_product, data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_product_with_already_existing_title(self):
        fake = Faker()

        data = {
            'title': self.product.title,
            'description': fake.text(max_nb_chars=200)
        }
        headers = {}
        response = self.client.post(self.create_product, data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_issue_with_valid_data(self):
        fake = Faker()

        data = {
            'title': fake.first_name(),
            'category': 'other'
        }
        headers = {}
        response = self.client.post(self.create_issue, data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_issue_with_empty_title(self):
        fake = Faker()

        data = {
            'title': '',
            'category': 'other'
        }
        headers = {}
        response = self.client.post(self.create_issue, data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_issue_with_no_title(self):
        fake = Faker()

        data = {
            'category': 'other'
        }
        headers = {}
        response = self.client.post(self.create_issue, data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_issue_with_empty_category(self):
        fake = Faker()

        data = {
            'title': fake.first_name(),
            'category': ''
        }
        headers = {}
        response = self.client.post(self.create_issue, data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_issue_with_no_category(self):
        fake = Faker()

        data = {
            'title': fake.first_name()
        }
        headers = {}
        response = self.client.post(self.create_issue, data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_issue_with_invalid_category(self):
        fake = Faker()

        data = {
            'title': fake.first_name(),
            'category': 'jhfgjhgfhj'
        }
        headers = {}
        response = self.client.post(self.create_issue, data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_issue_with_already_existing_title(self):
        fake = Faker()

        data = {
            'title': self.issue.title,
            'category': 'other'
        }
        headers = {}
        response = self.client.post(self.create_issue, data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_metric_with_valid_data(self):
        fake = Faker()

        data = {
            'title': fake.first_name(),
            'description': fake.text(max_nb_chars=200)
        }
        headers = {}
        response = self.client.post(self.create_metric, data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_metric_with_empty_title(self):
        fake = Faker()

        data = {
            'title': '',
            'description': fake.text(max_nb_chars=200)
        }
        headers = {}
        response = self.client.post(self.create_metric, data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_metric_with_no_title(self):
        fake = Faker()

        data = {
            'description': fake.text(max_nb_chars=200)
        }
        headers = {}
        response = self.client.post(self.create_metric, data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_metric_with_empty_description(self):
        fake = Faker()

        data = {
            'title': fake.first_name(),
            'description': ''
        }
        headers = {}
        response = self.client.post(self.create_metric, data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_metric_with_no_description(self):
        fake = Faker()

        data = {
            'title': fake.first_name()
        }
        headers = {}
        response = self.client.post(self.create_metric, data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_metric_with_already_existing_title(self):
        fake = Faker()

        data = {
            'title': self.metric.title,
            'description': fake.text(max_nb_chars=200)
        }
        headers = {}
        response = self.client.post(self.create_metric, data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_product_by_valid_id(self):
        headers = {}
        data = {
            'id': self.product.id
        }
        response = self.client.get(self.retrieve_product, params=data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_product_by_non_existing_id(self):
        headers = {}
        data = {
            'id': 676767
        }
        response = self.client.get(self.retrieve_product, params=data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_product_by_non_existing_title(self):
        headers = {}
        data = {
            'title': 'jkfgjkgf'
        }
        response = self.client.get(self.retrieve_product, params=data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_issue_by_valid_id(self):
        headers = {}
        data = {
            'id': self.issue.id
        }
        response = self.client.get(self.retrieve_issue, params=data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_issue_by_non_existing_id(self):
        headers = {}
        data = {
            'id': 87788778
        }
        response = self.client.get(self.retrieve_issue, params=data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_issue_by_non_existing_title(self):
        headers = {}
        data = {
            'title': 'kjfgjkgf'
        }
        response = self.client.get(self.retrieve_issue, params=data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_metric_by_valid_id(self):
        headers = {}
        data = {
            'id': self.metric.id
        }
        response = self.client.get(self.retrieve_metric, params=data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_metric_by_non_existing_id(self):
        headers = {}
        data = {
            'id': 87887878
        }
        response = self.client.get(self.retrieve_metric, params=data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_metric_by_non_existing_title(self):
        headers = {}
        data = {
            'title': 'jkfgjkgfjk'
        }
        response = self.client.get(self.retrieve_metric, params=data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_product_by_valid_title(self):
        headers = {}
        data = {
            'title': self.product.title
        }
        response = self.client.get(self.retrieve_product, params=data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_issue_by_valid_title(self):
        headers = {}
        data = {
            'title': self.issue.title
        }
        response = self.client.get(self.retrieve_issue, params=data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_metric_by_valid_title(self):
        headers = {}
        data = {
            'title': self.metric.title
        }
        response = self.client.get(self.retrieve_metric, params=data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_product_by_valid_id(self):
        fake = Faker()
        headers = {}
        data = {
            'title': fake.first_name(),
            'description': fake.text(max_nb_chars=200)
        }
        response = self.client.put(self.update_product, data, format='json', content_type='application/json', **headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_product_by_non_existing_id(self):
        fake = Faker()
        headers = {}
        data = {
            'title': fake.first_name(),
            'description': fake.text(max_nb_chars=200)
        }
        update_url = "/entity/{}/{}".format(788787, 'product')
        response = self.client.put(update_url, data, format='json', content_type='application/json', **headers)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_issue_by_valid_id(self):
        fake = Faker()
        headers = {}
        data = {
            'title': fake.first_name(),
            'category': 'other'
        }
        response = self.client.put(self.update_issue, data, format='json', content_type='application/json', **headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_issue_by_non_existing_id(self):
        fake = Faker()
        headers = {}
        data = {
            'title': fake.first_name(),
            'category': 'other'
        }
        update_url = "/entity/{}/{}".format(788787, 'issue')
        response = self.client.put(update_url, data, format='json', content_type='application/json', **headers)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_metric_by_valid_id(self):
        fake = Faker()
        headers = {}
        data = {
            'title': fake.first_name(),
            'description': fake.text(max_nb_chars=200)
        }
        response = self.client.put(self.update_metric, data, format='json', content_type='application/json', **headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_metric_by_non_existing_id(self):
        fake = Faker()
        headers = {}
        data = {
            'title': fake.first_name(),
            'description': fake.text(max_nb_chars=200)
        }
        update_url = "/entity/{}/{}".format(788787, 'metric')
        response = self.client.put(update_url, data, format='json', content_type='application/json', **headers)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_product_by_valid_id(self):
        data = {}
        headers = {}
        response = self.client.delete(self.delete_product, data=data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_product_by_non_existing_id(self):
        data = {}
        headers = {}
        delete_url = "/entity/{}/{}".format(788787, 'product')
        response = self.client.delete(delete_url, data=data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_issue_by_valid_id(self):
        data = {}
        headers = {}
        response = self.client.delete(self.delete_issue, data=data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_issue_by_non_existing_id(self):
        data = {}
        headers = {}
        delete_url = "/entity/{}/{}".format(788787, 'issue')
        response = self.client.delete(delete_url, data=data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_metric_by_valid_id(self):
        data = {}
        headers = {}
        response = self.client.delete(self.delete_metric, data=data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_metric_by_non_existing_id(self):
        data = {}
        headers = {}
        delete_url = "/entity/{}/{}".format(788787, 'metric')
        response = self.client.delete(delete_url, data=data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
