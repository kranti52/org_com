from django.db import models


class SystemObject(models.Model):
    OBJECT_CHOICES = (
        ('issue', 'Issue'),
        ('product', 'Product'),
        ('metric', 'Metric'),
    )
    object_type = models.CharField(max_length=20, choices=OBJECT_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
