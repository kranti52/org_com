from django.db import models

from ..models import Metric


class MetricManager(models.Manager):
    @classmethod
    def get_object_by_id(cls, id):
        try:
            """ CHECKME: cursor.execute("SELECT * FROM metric WHERE id = %s;", (id,))"""
            entity = Metric.objects.get(pk=id)
        except Metric.DoesNotExist:
            entity = None
        return entity

    @classmethod
    def get_object_by_title(cls, title):
        try:
            """ CHECKME: cursor.execute("SELECT * FROM metric WHERE title = %s;", (title,))"""
            entity = Metric.objects.get(title=title)
        except Metric.DoesNotExist:
            entity = None
        return entity

    @classmethod
    def filter_object_data(cls, request_data):
        """ CHECKME: cursor.execute("SELECT * FROM metric WHERE
        id = %s and title=%s;", (id, title,))"""
        metrics = []
        object_id = request_data.get('id')
        title = request_data.get('title')
        if object_id:
            metrics = Metric.objects.filter(id=object_id)

        if title and metrics:
            metrics = metrics.filter(title=title)
        elif title and not metrics:
            metrics = Metric.objects.filter(title=title)

        response = []
        for metric in metrics:
            response.append(metric.to_representation())
        return response
