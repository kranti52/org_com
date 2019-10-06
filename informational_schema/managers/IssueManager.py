from django.db import models

from ..models import Issue


class IssueManager(models.Manager):
    @classmethod
    def get_object_by_id(cls, id):
        try:
            entity = Issue.objects.get(pk=id)
        except Issue.DoesNotExist:
            entity = None
        return entity

    @classmethod
    def get_object_by_title(cls, title):
        try:
            entity = Issue.objects.get(title=title)
        except Issue.DoesNotExist:
            entity = None
        return entity

    @classmethod
    def filter_object_data(cls, request_data):
        issues = []
        object_id = request_data.get('id')
        title = request_data.get('title')
        category = request_data.get('category')

        if object_id:
            issues = Issue.objects.filter(id=object_id)

        if title and issues:
            issues = issues.filter(title=title)
        elif title and not issues:
            issues = Issue.objects.filter(title=title)

        if category and issues:
            issues = issues.filter(category=category)
        elif category and not issues:
            issues = Issue.objects.filter(category=category)

        response = []
        for issue in issues:
            response.append(issue.to_representation())
        return response
