from django.db import models

from ..models import Issue


class IssueManager(models.Manager):
    @classmethod
    def get_object_by_id(cls, id):
        try:
            """ CHECKME: cursor.execute("SELECT * FROM issue WHERE id = %s;", (id,))"""
            entity = Issue.objects.get(pk=id)
        except Issue.DoesNotExist:
            entity = None
        return entity

    @classmethod
    def get_object_by_title(cls, title):
        try:
            """ CHECKME: cursor.execute("SELECT * FROM issue WHERE title = %s;", (title,))"""
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
        """ CHECKME: cursor.execute("SELECT * FROM issue WHERE id = %s and title=%s and 
        category=%s;", (id, title, category,))"""
        if object_id:
            """ CHECKME: cursor.execute("SELECT * FROM issue WHERE id = %s;", (id,))"""
            issues = Issue.objects.filter(id=object_id)

        if title and issues:
            issues = issues.filter(title=title)
        elif title and not issues:
            """ CHECKME: cursor.execute("SELECT * FROM issue WHERE title = %s;", (title,))"""
            issues = Issue.objects.filter(title=title)

        if category and issues:
            issues = issues.filter(category=category)
        elif category and not issues:
            """ CHECKME: cursor.execute("SELECT * FROM issue WHERE category = %s;", (category,))"""
            issues = Issue.objects.filter(category=category)

        response = []
        for issue in issues:
            response.append(issue.to_representation())
        return response
