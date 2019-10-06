from django.db import models

from .SystemObject import SystemObject


class Metric(SystemObject):
    title = models.CharField(max_length=255, db_index=True, unique=True)
    description = models.CharField(max_length=1024, blank=True, null=True)

    def to_representation(self):
        return {
            'type': self.object_type,
            'id': self.id,
            'title': self.title,
            'description': self.description
        }
