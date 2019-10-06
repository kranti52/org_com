from django.db import models

from .SystemObject import SystemObject


class Map(models.Model):
    first_object = models.ForeignKey(SystemObject, related_name='map_first_object',
                                     on_delete=models.CASCADE)
    second_object = models.ForeignKey(SystemObject, related_name='map_second_object',
                                      on_delete=models.CASCADE)

    class Meta:
        unique_together = (('first_object', 'second_object'),)

    def to_representation(self):
        return {
            'first_object_id': self.first_object_id,
            'second_object_id': self.second_object_id,
        }
