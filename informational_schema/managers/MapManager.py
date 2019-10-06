from django.db import models
from django.db.models import Q

from ..models import Map


class MapManager(models.Manager):
    @classmethod
    def get_object_mapping_by_id(cls, id):
        entities = Map.objects.filter(Q(first_object_id=id) | Q(second_object_id=id))
        response = []
        for entity in entities:
            data = {}
            if id != entity.first_object_id:
                if 'product' == entity.first_object.object_type:
                    data = entity.first_object.product.to_representation()
                elif 'issue' == entity.first_object.object_type:
                    data = entity.first_object.issue.to_representation()
                elif 'metric' == entity.first_object.object_type:
                    data = entity.first_object.metric.to_representation()
            elif id != entity.second_object_id:
                if 'product' == entity.second_object.object_type:
                    data = entity.second_object.product.to_representation()
                elif 'issue' == entity.second_object.object_type:
                    data = entity.second_object.issue.to_representation()
                elif 'metric' == entity.second_object.object_type:
                    data = entity.second_object.metric.to_representation()
            if data:
                response.append(data)
        return response

    @classmethod
    def check_if_mapping_exists_by_id(cls, first_id, second_id):
        return Map.objects.filter(
            Q(first_object_id=first_id, second_object_id=second_id) |
            Q(first_object_id=second_id, second_object_id=first_id)).exists()
