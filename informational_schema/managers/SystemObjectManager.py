from django.db import models

from ..models import SystemObject


class SystemObjectManager(models.Manager):
    @classmethod
    def get_object_by_id(cls, id):
        try:
            entity = SystemObject.objects.get(pk=id)
        except SystemObject.DoesNotExist:
            entity = None
        return entity

    @classmethod
    def check_if_systemobject_exists_by_id(cls, obj_id):
        return SystemObject.objects.filter(id=obj_id).exists()
