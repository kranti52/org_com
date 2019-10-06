from django.db import models

from .SystemObject import SystemObject


class Issue(SystemObject):
    ISSUE_CHOICES = (
        ('general', 'General'),
        ('random1', 'Random1'),
        ('random2', 'Random2'),
        ('other', 'Other')
    )
    title = models.CharField(max_length=255, db_index=True, unique=True)
    category = models.CharField(max_length=255, choices=ISSUE_CHOICES, db_index=True)

    def to_representation(self):
        return {
            'type': self.object_type,
            'id': self.id,
            'title': self.title,
            'category': self.category
        }
