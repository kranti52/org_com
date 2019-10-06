from django.db import models

from ..models import Product


class ProductManager(models.Manager):
    @classmethod
    def get_object_by_id(cls, id):
        try:
            entity = Product.objects.get(pk=id)
        except Product.DoesNotExist:
            entity = None
        return entity

    @classmethod
    def get_object_by_title(cls, title):
        try:
            entity = Product.objects.get(title=title)
        except Product.DoesNotExist:
            entity = None
        return entity

    @classmethod
    def filter_object_data(cls, request_data):
        products = []
        object_id = request_data.get('id')
        title = request_data.get('title')
        if object_id:
            products = Product.objects.filter(id=object_id)
        if title and products:
            products = products.filter(title=title)
        elif title and not products:
            products = Product.objects.filter(title=title)

        response = []
        for product in products:
            response.append(product.to_representation())
        return response
